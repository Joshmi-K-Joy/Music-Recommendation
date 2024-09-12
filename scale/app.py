from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import librosa
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'test'
ALLOWED_EXTENSIONS = {'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def identify_chord(audio_file):
    y, sr = librosa.load(audio_file)

    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

    chroma_sum = np.sum(chroma, axis=1)

    root_note = np.argmax(chroma_sum)

    def classify_chord_quality(chroma_profile, root_note):
        third_interval = (root_note + 4) % 12
        fifth_interval = (root_note + 7) % 12

        if chroma_profile[(root_note + 3) % 12] > chroma_profile[(root_note + 4) % 12]:
            quality = 'm'  # Minor
        else:
            quality = 'Maj'  # Major

        return librosa.midi_to_note([root_note])[0] + quality

    chord = classify_chord_quality(chroma_sum, root_note)

    return chord

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        chord = identify_chord(filepath)
        return render_template('index.html', chord=chord, filename=filename)

    return render_template('index.html', error='Invalid file format')

if __name__ == '__main__':
    app.run(debug=True)
