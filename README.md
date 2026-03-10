# NoiseNinja: Industrial Anomaly Detection 🎧⚙️

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green?style=for-the-badge&logo=flask)
![Librosa](https://img.shields.io/badge/Librosa-Audio%20Processing-lightgrey?style=for-the-badge)

NoiseNinja is an **end-to-end Industrial Acoustic Anomaly Detection** system. It essentially treats "sound as a visual problem." We ingest live sounds from industrial machinery (like fans, pumps, or turbines), transform their raw audio waves into Mel-Spectrogram heatmaps, and use a Deep Learning Autoencoder to detect mechanical failure before it happens.

The final product is a **Live Health Dashboard** functioning as a complete Industry 4.0 Decision Support System, capable of warning layman users when a machine starts making unfamiliar rattling, grinding, or wearing noises.

---

## 🚀 Features
- **Live Microphone Recording:** Directly captures real-time acoustic sounds via the browser using the native Web Audio API (with browser noise-suppression completely disabled to capture raw machine hums perfectly).
- **Deep Autoencoder Inference:** Squeezes audio data through a bottleneck architecture trained purely on "Healthy" machine sounds. Does not require examples of broken machines! 
- **Real-time Spectrogram Heatmaps:** Displays an acoustic "fingerprint" of the machine's high frequencies.
- **Dynamic Anomaly Meter:** Plots the MSE (Mean Squared Error) "Reconstruction Loss." If the machine emits unfamiliar sounds, it fails to reconstruct them, causing the error signal to spike above our calibrated `0.0036` threshold, triggering a mechanical failure warning!

---

## 🛠️ Architecture & Tech Stack
1. **Frontend:** HTML, Vanilla CSS (Glassmorphism & Dark Mode), JavaScript (Chart.js & Native MediaRecorder API).
2. **Backend:** Flask.
3. **Data Processing:** `librosa` for Mel-Spectrogram extraction and `numpy` for matrix transformations.
4. **Machine Learning:** `tensorflow` / `keras` (Unsupervised Autoencoder).

---

## 💽 Dataset Setup (IMPORTANT)

**We DO NOT store the heavy acoustic dataset in this repository.**

1. Download the MIMII / Industrial Machine Dataset from [Kaggle Dataset Link Here].
2. Extract the downloaded archive.
3. Create a folder named `data/` in the root of this project.
4. Place the audio `.wav` files inside the `data/` folder following this structure:
    ```text
    NoiseNinja/
    ├── data/
    │   ├── normal/
    │   │   ├── ... .wav
    │   ├── abnormal/
    │   │   ├── ... .wav
    ```

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/mayank-goyal09/NoiseNinja.git
cd NoiseNinja
```

### 2. Install Dependencies
Ensure you have Python 3 installed. Then run:
```bash
pip install -r requirements.txt
```
*(If you do not have a requirements.txt, manually install `flask`, `librosa`, `numpy`, and `tensorflow`)*.

### 3. Run the Dashboard
```bash
python app.py
```
- Open `http://127.0.0.1:5000` in your web browser.
- Have fun dragging & dropping `.wav` files, or use the **Live Microphone** button to test the AI on sounds in your own room!

---

## 🧠 Model Training Journey

Initially, we built a Supervised CNN. While it got great accuracy, this was unrealistic because in the real manufacturing world, you don't always have access to thousands of hours of perfectly labeled "broken" machine sounds.

We then pivoted to an Unsupervised Autoencoder. We ran into the "Identity Mapping Trap" (where the model reconstructed anomalies perfectly instead of failing!). We fixed this by aggressively shrinking the bottleneck layer, forcing the AI to compress and heavily memorize only the core frequencies of a healthy machine—this way, when thrown a completely novel broken noise, the mathematical loss skyrocketed organically, solving the problem.
