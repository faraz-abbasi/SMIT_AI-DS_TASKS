# Face Recognition Web Application (CNN + Flask)

This project implements a Face Recognition system using **Convolutional Neural Networks (CNN)** and a **Flask-based web application**.  
It was developed as part of SMIT coursework to demonstrate the practical use of **ANNs, CNNs, and Machine Learning deployment**.

---

## 🔹 Technologies Used
- Python
- TensorFlow (CPU)
- OpenCV
- NumPy
- Flask
- HTML, CSS, JavaScript

---

## 🔹 Project Overview
The project is divided into three main tasks:

- **Task 1 – ANN:**  
  Introduction to Artificial Neural Networks and basic model implementation.

- **Task 2 – CNN:**  
  Image classification using Convolutional Neural Networks.

- **Task 3 – Face Recognition:**  
  CNN-based face recognition with real-time webcam input.

A Flask web application is used to capture webcam images, send them to the backend, and display prediction results in the browser.

---

## 🔹 Features
- Real-time webcam-based face recognition
- CNN model for face classification
- Flask REST API for predictions
- Simple and responsive frontend UI
- Modular project structure

---

## 🔹 Project Structure
.
├── app.py
├── requirements.txt
├── Task1_ANN.ipynb
├── Task2_CNN.ipynb
├── Task3_Face_Recognition.ipynb
├── templates/
│   └── index.html
└── static/
    ├── js/
    │   └── app.js
    └── css/
        └── style.css

---

## 🔹 Setup Instructions
```bash
conda create -n face_rec_env python=3.10
conda activate face_rec_env
pip install -r requirements.txt
python app.py
```

---

## 🔹 Open your browser and visit:
```
http://localhost:5000
```

---

## 🔹 Notes
- Trained model files are intentionally excluded from this repository.
- Run the provided notebooks to train and generate the face recognition model.
- This project uses TensorFlow CPU for stability on Windows systems.

---

## 🔹 Author
- Faraz Ali
  
---
