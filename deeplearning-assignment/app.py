from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
import os
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Configuration
MODEL_PATH = 'models/face_recognition_model.h5'

# Load Model
model = None
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
    print("✓ Model Loaded.")
else:
    print("⚠ Model not found. Run notebook first.")

# === HARDCODED NAMES FOR 2 FRIENDS ===
# The model assigns ID based on alphabetical order of folder names
# Friend_1 comes before Friend_2, so 0 is Friend 1.
class_names = {
    0: 'Friend 1',
    1: 'Friend 2'
}

@app.route('/')
def index():
    return render_template('index.html', model_loaded=(model is not None))

@app.route('/predict', methods=['POST'])
def predict():
    if not model: return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.json
        image_data = data.get('image').split(',')[1]
        
        # Decode
        nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Preprocess
        img = cv2.resize(img, (150, 150))
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Predict
        preds = model.predict(img, verbose=0)
        class_idx = int(np.argmax(preds))
        confidence = float(np.max(preds)) * 100
        
        name = class_names.get(class_idx, "Unknown")
        
        # Format all probabilities
        all_preds = {}
        for idx, prob in enumerate(preds[0]):
            p_name = class_names.get(idx, f"Class {idx}")
            all_preds[p_name] = round(float(prob) * 100, 2)

        return jsonify({
            'success': True,
            'predicted_person': name,
            'confidence': round(confidence, 2),
            'all_predictions': all_preds
        })
        
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)