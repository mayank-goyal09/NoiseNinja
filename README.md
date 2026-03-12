<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B0C10,50:1F2833,100:45A29E&height=200&section=header&text=NoiseNinja&fontSize=80&fontColor=66FCF1&fontAlignY=38&desc=Industrial%20Acoustic%20Anomaly%20Detection&descAlignY=60&descSize=22&animation=fadeIn" width="100%"/>

<!-- Animated Typing -->
<a href="https://mayank-goyal09.github.io/NoiseNinja/templates/index.html">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=66FCF1&center=true&vCenter=true&width=700&lines=Powered+by+Flask%2C+TensorFlow%2C+and+Vanilla+JS;Unsupervised+Autoencoder+AI+Engine;Live+Microphone+%26+Spectrogram+Dashboard;Defeating+the+Identity+Mapping+Trap!;%F0%9F%8E%A5+Listen+to+the+Machines...;%E2%98%95+Your+Acoustic+Sentinel+is+ready!" alt="Typing SVG" />
</a>

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-UI-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Hosted-181717?style=for-the-badge&logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

> **NoiseNinja** listens to the acoustic footprint of industrial machines and uses an unsupervised deep learning Autoencoder to detect microscopic mechanical anomalies before they become catastrophic failures.

### 🌐 [**Experience the Live Dashboard Here**](https://mayank-goyal09.github.io/NoiseNinja/templates/index.html)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Unsupervised AI Engine
- Powered by a **TensorFlow Autoencoder** trained *only* on healthy data
- Safely escapes the **"Identity Mapping Trap"** with compressed bottleneck
- Real-time **0.0036 MSE Loss Threshold** for pinpoint accuracy
- Catches unseen mechanical failures autonomously

</td>
<td width="50%">

### 🎛️ Acoustic Dashboard
- Sleek **Glassmorphism UI** with modern dark mode
- Real-time anomaly **Error Signal Charts** via Chart.js
- Extracted **Mel-Spectrogram Heatmaps** on the fly
- Dynamic Status Badges prioritizing industrial health

</td>
</tr>
<tr>
<td width="50%">

### 🎙️ Live Microphone Input
- Captures audio seamlessly via **MediaRecorder API**
- Explicitly disables browser audio filters (echo cancellation/noise suppression)
- Supports direct **.WAV File Uploads**
- Processes raw signals for ultimate integrity

</td>
<td width="50%">

### ⚙️ Simulation Mode
- Test logic instantly without breaking physical hardware
- Built-in **"Healthy"** and **"Bearing Wear"** toggles
- Observes the neural network spike in real-time
- Perfect for demonstrations and debugging

</td>
</tr>
</table>

---

## 🖥️ Dashboard Preview

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║  🎸 NoiseNinja   Live Recording   Upload File   Simulate ║
╠══════════════════════════════════════════════════════════╣
║                                    ┌──────────────────┐  ║
║  ANOMALY METER                     │  Status          │  ║
║                                    │                  │  ║
║  [Chart: Error Signal over Time]   │ 🔴 ANOMALY       │  ║
║                                    │                  │  ║
║                                    │ Confidence: 99%  │  ║
║                                    │                  │  ║
║  ─────────────────────────────     └──────────────────┘  ║
║  Mel-Spectrogram Heatmap                                 ║
║  ┌──────────────────────────────────────────────────┐    ║
║  │   [Heatmap Visualizing Raw Audio Frequencies]    │    ║
║  └──────────────────────────────────────────────────┘    ║
╚══════════════════════════════════════════════════════════╝
```

*☕ "Silence the noise, find the failures."*

</div>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[🎙️ Sound Source\nMic or WAV] --> B[Flask Server\napp.py]
    B --> C[Librosa Processing\nMel-Spectrogram]
    C --> D[Model Inference\nTF Autoencoder]
    D --> E{MSE > 0.0036?}
    E -->|Yes| F[🔴 Anomaly Detected]
    E -->|No| G[🟢 Healthy Machine]
    F --> H[🖥️ Dashboard UI\nindex.html]
    G --> H
    H --> I[Error Signal Chart]
    H --> J[Spectrogram Heatmap]
```

---

## 📁 Project Structure

```
NoiseNinja/
│
├── 📓 notebooks/
│   ├── 02_Model_Training_CNN.ipynb         # Initial CNN explorations
│   └── 03_Anomaly_Detection_Autoencoder.py # Autoencoder creation & training
│
├── 🌐 templates/
│   └── index.html             # Dashboard UI, Glassmorphism, Chart.js logic
│
├── 🧠 anomaly_detection_autoencoder.h5     # Trained Keras model
├── 🖥️ app.py                  # Flask backend (Audio processing & Inference)
├── 📋 requirements.txt        # Python dependencies
└── 📖 README.md               # You are here
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# 1. Clone the repo
git clone https://github.com/mayank-goyal09/NoiseNinja.git
cd NoiseNinja

# 2. Install dependencies
pip install -r requirements.txt
```

### Run

```bash
# Start the Flask backend server
python app.py

# Open in browser
# → http://127.0.0.1:5000/
```

---

## 🔌 API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves the NoiseNinja dashboard |
| `/predict` | POST | Submits audio data (file/blob) for AI inference |
| `/simulate/{status}` | GET | Tests response with "healthy" or "abnormal" dummy data |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask |
| **AI Model** | TensorFlow / Keras (Unsupervised Autoencoder) |
| **Audio Processing**| Librosa |
| **Frontend UI** | HTML5, CSS (Glassmorphism), Vanilla JS |
| **Data Viz** | Chart.js |

</div>

---

## 🗺️ Roadmap

- [x] Initial supervised CNN approach
- [x] Pivot to Unsupervised Autoencoder
- [x] Overcome the Identity Mapping Trap
- [x] Calibrate precise detection accuracy (Threshold: 0.0036)
- [x] Live dashboard with glassmorphism UI
- [x] Microphone integration with filter bypassing
- [ ] Connect physical IoT decibel/audio sensors
- [ ] Implement cloud data logging for anomalies
- [ ] Email/SMS alerts when an anomaly is detected

---
