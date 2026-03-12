<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D2017,50:1C5D42,100:31A572&height=200&section=header&text=NoiseNinja&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Real-time%20Industrial%20Health%20Dashboard&descAlignY=60&descSize=22&animation=fadeIn" width="100%"/>

<!-- Animated Typing -->
<a href="https://mayank-goyal09.github.io/NoiseNinja/templates/index.html">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=31A572&center=true&vCenter=true&width=700&lines=Interactive+Diagnostic+Experience;Live+Mel-Spectrogram+Visualizer;Difference+Map+Highlights+Failing+Frequencies;%F0%9F%8E%A5+Listen+to+the+Machines...;%E2%98%95+Your+Acoustic+Sentinel+is+ready!" alt="Typing SVG" />
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

> The final output of your project will be a real-time industrial health dashboard that transforms raw machine sounds into an interactive diagnostic experience. Instead of a static file uploader, the app provides a Live Mel-Spectrogram visualizer that shows the machine's "acoustic fingerprint," a dynamic Anomaly Meter that tracks the reconstruction error against your 0.0036 threshold, and a Difference Map that highlights exactly which frequencies are failing. By using buttons to trigger "Normal" and "Abnormal" sound profiles, you demonstrate a functional Decision Support System that instantly flags mechanical instability, such as bearing wear or fan wobbles, through high-variance "spikes" in the error signal. This creates a professional, end-to-end Industry 4.0 solution that proves you can build, troubleshoot, and deploy a complex deep learning pipeline for real-world smart manufacturing.

### 🌐 [**Experience the Live Demo Here**](https://mayank-goyal09.github.io/NoiseNinja/templates/index.html)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Unsupervised AI Engine
- Powered by a **TensorFlow Autoencoder** trained *only* on normal sounds
- Bypasses the **Identity Mapping Trap** using specific bottlenecking
- Reconstructs audio effectively to isolate anomalies
- Calculates precise **MSE Reconstruction Loss**

</td>
<td width="50%">

### 📊 Real-Time Diagnostic Dashboard
- **Live Mel-Spectrogram Visualizer** detailing the machine's "acoustic fingerprint"
- **Difference Map** highlighting exactly which frequencies are failing
- **Dynamic Anomaly Meter** evaluating against the 0.0036 threshold
- Interactive, professional **Industry 4.0 Solution**

</td>
</tr>
<tr>
<td width="50%">

### 🎙️ Live Audio Streaming
- Captures sound through the **MediaRecorder API**
- Overrides harsh browser audio filters ensuring accuracy
- Accepts traditional **.WAV audio file** drops
- Full front-to-back integration with the AI backend

</td>
<td width="50%">

### ⚙️ Functional Decision Support
- Buttons to quickly trigger **"Normal"** and **"Abnormal"** sound profiles
- Simulate real-world instability like **bearing wear** or **fan wobbles**
- Identify instability instantly through high-variance "spikes"
- Real-world smart manufacturing reliability

</td>
</tr>
</table>

---

## 🖥️ Dashboard Preview

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║  ⚙️ NoiseNinja  Live Mic  Upload Audio  Dev Simulation    ║
╠══════════════════════════════════════════════════════════╣
║                                    ┌──────────────────┐  ║
║  ANOMALY METER                     │  System Status   │  ║
║                                    │                  │  ║
║      /\                            │ 🔴 ANOMALY       │  ║
║   /\/  \  Threshold 0.0036         │                  │  ║
║  /      \/\____                    │ Type: Fan Wobble │  ║
║                                    │                  │  ║
║  ─────────────────────────────     └──────────────────┘  ║
║  Live Mel-Spectrogram & Difference Map                   ║
║  ┌──────────────────────────────────────────────────┐    ║
║  │   [Acoustic Fingerprint Heatmap & Diff]          │    ║
║  └──────────────────────────────────────────────────┘    ║
╚══════════════════════════════════════════════════════════╝
```

*☕ "Silence the noise, find the failures."*

</div>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[🎙️ Acoustic Source] --> B[Flask API\napp.py]
    B --> C[Librosa\nMel-Spectrogram]
    C --> D[TensorFlow\nDeep Learning Pipeline]
    D --> E{Error Signal\n> 0.0036?}
    E -->|Yes| F[🔴 Flag Instability]
    E -->|No| G[🟢 Healthy Profile]
    F --> H[🖥️ Interactive Diagnostic Exp.\nindex.html]
    G --> H
    H --> I[Anomaly Meter & Diff Map]
    H --> J[Decision Support System]
```

---

## 📁 Project Structure

```
NoiseNinja/
│
├── 📓 notebooks/
│   ├── 02_Model_Training_CNN.ipynb         # Explored CNN
│   └── 03_Anomaly_Detection_Autoencoder.py # Autoencoder approach
│
├── 🌐 templates/
│   └── index.html             # Real-time industrial health dashboard
│
├── 🧠 anomaly_detection_autoencoder.h5     # Trained AI model weights
├── 🖥️ app.py                  # Flask endpoints & DL Pipeline
├── 📋 requirements.txt        # Deep learning dependencies
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
| `/` | GET | Serves the interactive diagnostic experience |
| `/predict` | POST | Audio processing through DL pipeline & difference mapping |
| `/simulate/{status}` | GET | Triggers "Normal" and "Abnormal" profiles (e.g., bearing wear) |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask |
| **Deep Learning** | TensorFlow / Keras (Unsupervised Autoencoder) |
| **Acoustic Pre-processing**| Librosa |
| **Frontend UI** | HTML5, CSS, Vanilla JS |
| **Data Visualization** | Chart.js |

</div>

---

## 🗺️ Roadmap

- [x] Initial supervised CNN approach
- [x] Pivot to Unsupervised Autoencoder
- [x] Overcome the Identity Mapping Trap
- [x] Calibrate precise detection accuracy (Threshold: 0.0036)
- [x] Real-time industrial health dashboard
- [x] Live Microphone & Difference Map integration
- [ ] Connect physical IoT decibel/audio sensors
- [ ] Implement cloud data logging for anomalies
- [ ] Email/SMS alerts when an anomaly is detected

---

## 👨‍💻 Author

<div align="center">

<a href="https://mayank-goyal09.github.io/">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D2017,100:1C5D42&height=60&text=Made%20with%20%E2%98%95%20by%20Mayank%20Goyal&fontColor=ffffff&fontSize=20&fontAlignY=65" width="500"/>
</a>

<br/><br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-mayank--goyal09.github.io-31A572?style=for-the-badge&logo=github&logoColor=white)](https://mayank-goyal09.github.io/)
[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mayank-goyal09)

</div>

---

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:31A572,100:0D2017&height=120&section=footer" width="100%"/>
