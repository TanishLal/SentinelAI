# 🚀 SentinelAI – Real Time Threat and Emergency Detection System

---

## 📝 Overview
SentinelAI is an advanced, real-time emergency detection system that integrates multiple deep learning models to detect and alert emergency scenarios. It combines:
- **Fire Detection** (CNN-based)
- **Shoplifting Detection** (3D-CNN based)
- **Accident Detection** (CNN/LSTM-based)
- Existing **Theft, Assault, Road Incidents, Fire/Smoke** modules

The system uses computer vision and deep learning to process CCTV or live video feeds, identifying critical events and triggering alerts for rapid response.

---

## ✨ Highlights
- **Multi-Event Detection:** Fire, theft, assault, road accidents, shoplifting, and more.  
- **Real-Time Monitoring & Alerts:** Immediate notifications to the appropriate emergency services.  
- **Efficient & Lightweight:** Modular design deployable on edge devices and cloud.  

---

## 🎨 Architecture
Below are the architectures and flow:
[](https://github.com/TanishLal/SentinalAi/raw/main/DB_Sample/input/SentinelAI%20Architectural%20FlowChart.png)]
### Shoplifting Detection – 3D-CNN (SlowFast Inspired)
![3D-CNN](https://github.com/TanishLal/SentinalAi/blob/main/DB_Sample/input/Convolution%20Neural%20Network%20(CNN).png)  
**Description:** Splits input video into Fast and Slow paths. RGB and Optical Flow streams capture motion and semantics. Features are fused for final classification.

### Fire Detection – CNN
![CNN](https://github.com/TanishLal/SentinalAi/blob/main/DB_Sample/input/Long%20Short%20Term%20Memory%20(LSTM).png)  
**Description:** Lightweight CNN variants (FireNet, Inception-OnFire) optimized for real-time fire/smoke detection.

### Accident Detection – CNN + LSTM
![CNN-LSTM](https://github.com/TanishLal/SentinelAI/blob/702b6e85099cf036532792067d654fc79882bd22/521_2020_4867_Fig1_HTML.png)
**Description:** Combines spatial CNN layers and temporal LSTM units for accurate accident recognition.

---

## 📦 Pretrained Models
Download weights and place them in each module’s `weights/` folder:  
- [FireNet/InceptionVx-OnFire](https://drive.google.com/file/d/1nTl7TINusWG6gbvKHVWgpWUlAyydop5Y/view?usp=drive_link)  
- [Shoplifting Detection](https://drive.google.com/file/d/1bDHAqi3yy1-ziE6ySQcFZi2nqZ-puAEH/view?usp=sharing)  
- [Accident Detection](https://drive.google.com/file/d/1n1XN-RLfHcV8Zu7ef1IS6xz0vy1gS2hy/view?usp=sharing)  

---

## 🏋️ Model Training & Evaluation

### Training
- **Preprocessing:** Extract frames, resize, normalize. RGB + optical flow for SlowFast.  
- **Models:** 
  - Fire Detection: CNN (FireNet/Inception).  
  - Shoplifting: 3D-CNN SlowFast.  
  - Accident: CNN + LSTM sequence model.  
- **Frameworks:** TensorFlow/Keras, PyTorch, OpenCV.  
- **Optimizer:** Adam; **Loss:** Categorical Crossentropy.
---

## 🔔 Real-Time Alarming & Notification System

**This module ensures that each detected event triggers an immediate, automated response with location details:**

### 🔥 Fire Accidents
- Detects fire or smoke using CCTV feeds.  
- Sends **instant alerts to the nearest fire brigade**.  
- Shares **location of the CCTV camera** where the incident occurred.  
- Optionally triggers **voice calls/SMS** to emergency contacts.

### 🚑 Road Accidents
- Detects accidents from traffic or road cameras.  
- Notifies the **nearest hospital** and **emergency response team**.  
- **Calls an ambulance automatically** with the CCTV location.  
- Provides a short **video clip or snapshot** of the incident.

### 🥷 Shoplifting
- Detects theft or suspicious activity in retail environments.  
- Sends **real-time notifications to the store owner/manager** through:  
   - **Web dashboard alert**  
   - **SMS/WhatsApp message**  
   - **Optional phone call alert**  
- Includes **image snapshot and timestamp**.

---

## 🏗️ Tech Stack & Frameworks Used

**Core Languages & Libraries**
- **Python 3.x**  

**Deep Learning & Computer Vision**
- **TensorFlow, PyTorch, Keras** – Model development  
- **OpenCV, MediaPipe** – Video processing, tracking  

**Backend & APIs**
- **Flask / FastAPI** – REST APIs and service integration  
- **Google Maps API / Geolocation API** – Location tagging and address lookup  

**Notifications & Communication**
- **Twilio / WhatsApp API** – SMS and voice call alerts  
- **Firebase Cloud Messaging / Push Notifications** – Mobile and dashboard alerts  

**Deployment & Scaling**
- **Docker** – Containerized deployments  
- **Cloud Support:** AWS / Azure / GCP (optional)  
- **Database:** Firebase Realtime DB / MongoDB / PostgreSQL for event logs  

---


### Accuracy
```python
| Model                 | Accuracy | Precision | Recall | F1-score |
| --------------------- | -------- | --------- | ------ | -------- |
| Fire Detection (CNN)  | 95%      | 94%       | 93%    | 93%      |
| Shoplifting (3D-CNN)  | 92%      | 91%       | 90%    | 90%      |
| Accident (CNN + LSTM) | 90%      | 89%       | 88%    | 88%      |

```


## 👥 Team Members

* **Tanish Lal O**
* **Sijo Devassy V J**
* **Ruffino Rio Fernando J**
* **Dhanush G**
* **Singaravel G**
* **Syed Imthiyaz S**

---

## 📜 License

This project is licensed under the MIT License.
