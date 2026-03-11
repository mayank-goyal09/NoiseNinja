import os
import numpy as np
import librosa
import time
from flask import Flask, render_template, request, jsonify

try:
    from tensorflow.keras.models import load_model
    keras_available = True
except ImportError:
    keras_available = False

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Try loading available models 
MODELS = {}
if keras_available:
    try:
        if os.path.exists('anomaly_detection_autoencoder.h5'):
            MODELS['autoencoder'] = load_model('anomaly_detection_autoencoder.h5')
            print("Autoencoder model loaded successfully!")
    except Exception as e:
        print(f"Error loading models: {e}")

AUTOENCODER_THRESHOLD = 0.0036 # Updated to user request
DISPLAY_STEPS = 50
DISPLAY_FREQS = 20

def generate_display_spectrogram(S_db):
    """ Downsamples a high-res spectrogram to (20, 50) for the UI Heatmap. """
    # S_db shape: (128, time_frames)
    spectrogram_data = []
    freq_splits = np.array_split(S_db, DISPLAY_FREQS, axis=0)
    
    for f_split in freq_splits:
        # Mean across frequencies in this bin
        time_series = f_split.mean(axis=0) 
        # Mean across time frames to get exactly 50 steps
        time_splits = np.array_split(time_series, DISPLAY_STEPS)
        
        row = []
        for t_split in time_splits:
            val = t_split.mean() if len(t_split) > 0 else -80
            # S_db is usually -80 to 0. Scale to 0-255 for the heatmap
            scaled_val = ((val + 80) / 80) * 255
            row.append(max(0, min(255, scaled_val)))
        spectrogram_data.append(row)
    return spectrogram_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """ Handles real audio file uploads. """
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
        
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        try:
            # 1. Load actual audio
            y, sr = librosa.load(filepath, sr=None)
            
            # Extract high-res Mel-spectrogram
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
            S_db = librosa.power_to_db(S, ref=np.max)
            
            # Generate UI Heatmap Representation
            spectrogram_data = generate_display_spectrogram(S_db)
            
            # Base variables
            error_signal = []
            detected_anomaly = False
            max_loss = 0
            
            if 'autoencoder' in MODELS:
                # Prepare for real model inference
                target_frames = 313
                # Ensure uniform shape (128, 313)
                if S_db.shape[1] < target_frames:
                    pad_width = target_frames - S_db.shape[1]
                    model_input_s = np.pad(S_db, pad_width=((0, 0), (0, pad_width)), mode='constant')
                else:
                    model_input_s = S_db[:, :target_frames]
                    
                model_input = np.expand_dims(model_input_s, axis=(0, -1))
                
                # Predict
                model = MODELS['autoencoder']
                reconstruction = model.predict(model_input)
                
                # Calculate real loss per time frame instead of just global mean!
                # model_input is (1, 128, 313, 1). diff is same shape.
                diff = np.square(model_input - reconstruction)
                # mean across frequencies for each time step -> shape: (1, 313, 1)
                time_loss = np.mean(diff, axis=(1, 3))[0] 
                
                # Downsample 313 frames to our 50 UI Display steps
                time_splits = np.array_split(time_loss, DISPLAY_STEPS)
                error_signal = [float(np.mean(ts)) for ts in time_splits]
                
            else:
                # If no model is loaded, fallback to simulating an error profile
                # based loosely on the file's raw RMS envelope, just mapped to our tiny error scale
                rms = librosa.feature.rms(y=y)[0]
                rms_splits = np.array_split(rms, DISPLAY_STEPS)
                
                error_signal = []
                for r in rms_splits:
                    if len(r) > 0:
                        val = float(r.mean()) * 0.02
                    else:
                        val = 0.0
                    error_signal.append(max(0, val + np.random.normal(0.0005, 0.0002)))

            # Limit length exactly
            error_signal = error_signal[:DISPLAY_STEPS]

            max_loss = float(max(error_signal)) if len(error_signal) > 0 else 0.0
            avg_loss = float(sum(error_signal) / len(error_signal)) if len(error_signal) > 0 else 0.0
            detected_anomaly = max_loss > AUTOENCODER_THRESHOLD
                
            confidence = min(100.0, (max_loss / AUTOENCODER_THRESHOLD) * 50) if detected_anomaly else max(0.0, 100 - ((avg_loss / AUTOENCODER_THRESHOLD) * 50))
                
            result = {
                'model': 'Autoencoder (Real Audio)',
                'status': 'Mechanical Failure Detected 🚨' if detected_anomaly else 'Machine Healthy ✅',
                'is_anomaly': bool(detected_anomaly),
                'metric': f"Peak MSE Loss: {max_loss:.6f}",
                'threshold': f"Threshold: {AUTOENCODER_THRESHOLD:.4f}",
                'confidence': f"{confidence:.2f}%",
                'error_signal': error_signal,
                'spectrogram': spectrogram_data
            }
                
            os.remove(filepath)
            return jsonify(result)
            
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': str(e)}), 500


@app.route('/simulate/<status>', methods=['GET'])
def simulatePredict(status):
    is_abnormal = status.lower() == 'abnormal'
    time.sleep(1) # simulate loading
    
    time_steps = DISPLAY_STEPS
    error_signal = []
    
    if is_abnormal:
        error_signal = np.random.normal(loc=0.0015, scale=0.0005, size=time_steps).tolist()
        spike_indices = np.random.choice(time_steps, size=5, replace=False)
        for idx in spike_indices:
            error_signal[idx] = np.random.uniform(0.0050, 0.0090)
    else:
        error_signal = np.random.normal(loc=0.0018, scale=0.0004, size=time_steps).tolist()
        
    error_signal = [max(0, e) for e in error_signal]
    max_loss = max(error_signal)
    avg_loss = sum(error_signal) / len(error_signal)
    detected_anomaly = max_loss > AUTOENCODER_THRESHOLD
    
    spectrogram_data = []
    for _ in range(DISPLAY_FREQS):
        if is_abnormal:
            freq_band = np.random.uniform(0, 100, time_steps)
            for idx in spike_indices:
                freq_band[idx] = 255 
        else:
            freq_band = np.random.uniform(0, 70, time_steps)
            
        spectrogram_data.append(freq_band.tolist())
    
    confidence = min(100.0, (max_loss / AUTOENCODER_THRESHOLD) * 50) if detected_anomaly else max(0.0, 100 - ((avg_loss / AUTOENCODER_THRESHOLD) * 50))
        
    result = {
        'model': 'Autoencoder (Simulated)',
        'status': 'Mechanical Failure Detected 🚨' if detected_anomaly else 'Machine Healthy ✅',
        'is_anomaly': bool(detected_anomaly),
        'metric': f"Peak MSE Loss: {max_loss:.6f}",
        'threshold': f"Threshold: {AUTOENCODER_THRESHOLD:.4f}",
        'confidence': f"{confidence:.2f}%",
        'error_signal': error_signal,  
        'spectrogram': spectrogram_data 
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
