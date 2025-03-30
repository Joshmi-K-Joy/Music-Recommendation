# Music Recommendation



 📜Overview
 
This project focuses on music genre classification and scale analysis using a Convolutional Neural Network (CNN). The model is trained on the GTZAN dataset, a widely used dataset for music genre classification, and leverages Librosa for audio feature extraction. The system allows real-time classification of audio files through a Flask web application.


✨ Features

✅ Music Genre Classification: Identifies the genre of a given audio file.
✅ Scale Analysis: Extracts musical scales from an audio signal.
✅ Deep Learning-based Model: Utilizes a CNN for accurate genre prediction.
✅ Web Interface: Built with Flask for user-friendly interaction.
✅ Real-time Processing: Allows users to upload an audio file and classify it instantly.


📂 Dataset: GTZAN

The GTZAN dataset is a standard dataset used for music genre classification and consists of 1,000 audio tracks spanning 10 different genres:
Blues, Classical,Country,Disco,Hip-hop,Jazz,Metal,Pop,Reggae,Rock
Each genre contains 100 samples, each lasting 30 seconds and recorded in .wav format.

📌Programming Languages & Libraries

Python (Main Programming Language)
TensorFlow & Keras (Deep Learning Frameworks)
Librosa (Audio Processing & Feature Extraction)
NumPy & Pandas (Data Handling)
Matplotlib & Seaborn (Data Visualization)
Flask (Web Application Framework)
Jupyter Notebook & PyCharm (Development Environments)

📌Deploy the Model Using Flask

Open http://127.0.0.1:5000/ in your browser.
Upload an audio file to classify its genre and analyze its scale.

📊 Model Performance & Results

The CNN model achieves high accuracy on the GTZAN dataset. Some of the key performance metrics include:
Training Accuracy: ~95%
Validation Accuracy: ~90%
Confusion Matrix & Loss Graphs: Available in the evaluation output.

🏗️Future Enhancements

🔹 Improve accuracy using more advanced architectures (e.g., ResNet, LSTMs).🔹 Expand dataset to include more genres and diverse music samples.🔹 Implement real-time classification using live audio input.🔹 Enhance the Flask UI for a better user experience.

🏁 Conclusion

This project successfully implements music genre classification and scale analysis using a CNN-based deep learning approach. By leveraging the GTZAN dataset and audio processing techniques, the model achieves high accuracy in identifying music genres. Additionally, the Flask-based web interface makes it easy to interact with the model in real-time. Future improvements will focus on enhancing the model’s accuracy, incorporating more genres, and developing a real-time audio classification feature.

This work demonstrates the potential of deep learning in music analysis, providing a foundation for more advanced applications in the field of music recommendation, automatic DJ systems, and sound recognition.
