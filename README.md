# SentinelAI 🚀

SentinelAI is an open-source deep learning project designed to revolutionize public and private safety by automatically detecting and notifying for a wide range of emergency and illegal activities in real time. Originally built for shoplifting detection, SentinelAI has evolved into a comprehensive surveillance solution capable of identifying events such as shoplifting, robbery, assault, abuse, vandalism, fighting, shooting, road accidents, explosions, and fire/smoke incidents.

---

## Table of Contents 📅
- [Project Highlights](#project-highlights)
- [Introduction](#introduction)
- [Problem Statement & Goals](#problem-statement--goals)
- [Data Collection](#data-collection)
- [Model Architecture](#model-architecture)
- [Model Training & Evaluation](#model-training--evaluation)
- [System Overview & Pipeline Demo](#system-overview--pipeline-demo)
- [Input-Output Examples](#input-output-examples)
- [Setup](#setup)
- [References](#references)

---

## Project Highlights ✨
- **Multi-Event Detection:**  
  Combines advanced computer vision with deep learning (using both CNN and LSTM) to capture spatial and temporal features for detecting a wide range of incidents.
  
- **Real-Time Monitoring & Alerts:**  
  Designed for deployment on edge devices with extremely low inference time. The system provides immediate notifications to the appropriate emergency services:
  - **Fire/Smoke:** Alerts the nearest fire department.
  - **Road Accidents:** Notifies ambulance services.
  - **Violence & Crime (assault, robbery, fighting, shooting):** Triggers alerts to local police.
    
- **Efficient and Lightweight:**  
  Utilizes a novel two-stream (SlowFast) architecture with a dual-path design that minimizes parameters while maintaining high accuracy and speed.

---

## Introduction 📜
### Computer Vision & Human Action Recognition
Recent innovations in deep learning have made computer vision one of the most effective AI fields. Human Action Recognition (HAR) is especially challenging since it requires understanding both the spatial details in individual frames and the temporal evolution across frames. Traditional 2D-CNN approaches can misclassify similar-looking actions; hence, SentinelAI extends the analysis into the temporal domain with 3D-CNN and LSTM layers, ensuring robust and distinctive recognition even under complex conditions.

---

## Problem Statement & Goals 🎯
- **The Challenge:**  
  Continuous monitoring of CCTV footage is exhaustive for human operators, and critical incidents such as theft, violence, or emergencies can be easily missed.
- **Our Goal:**  
  Provide a comprehensive, automated solution for real-time detection and alerting. By capturing subtle temporal cues and spatial features, SentinelAI aims to significantly reduce response times and enhance public safety.

---

## Data Collection 🗃️
- **Dataset:**  
  Videos collected from security cameras in supermarkets and convenience stores. Theft scenarios were enacted by actors under various conditions and camera angles.
- **Scenarios Include:**  
  - Routine customer actions (item picking, returning, or examining)  
  - Criminal lapses (concealing an item in clothing or a bag)

*Over 4000 video clips were curated after extensive filtering.*

---

## Model Architecture 🎨
### Network Name: **Gate_Flow_SlowFast**
Inspired by the SlowFast Networks and MobileNet-SSD, our architecture splits the visual processing into two complementary channels:
- **Slow Path:**  
  Processes a down-sampled input (e.g., 4 frames) to extract deep spatial features.
- **Fast Path:**  
  Processes full-resolution input (e.g., 64 frames) and is further divided into:
  - **RGB Channel:**  
    Extracts detailed visual appearance using 3D-CNN layers with ReLU activation.
  - **Optical Flow Channel:**  
    Captures motion dynamics using 3D-CNN layers with Sigmoid activation.
- **Fusion & Classification:**  
  Lateral connections merge features from both channels, and subsequent CNN layers combined with LSTM modules capture temporal dynamics. Fully connected layers generate final class probabilities for targeted notifications.

![SentinelAI Architecture FlowChart](https://github.com/TanishLal/SentinalAi/blob/main/DB_Sample/input/SentinelAI%20Architectural%20FlowChart.png)

---

## Model Training & Evaluation 📑
- **Training Environment:**  
  AWS SageMaker on EC2 p3.2xlarge instances.
- **Frameworks:**  
  TensorFlow, Keras, Python, CNN, LSTM and OpenCV.
- **Optimization:**  
  Utilized the Adam optimizer with standard parameters.
- **Performance:**  
  Achieved an F1-score of ~87% on our curated dataset, significantly outperforming baseline models.

![Convolution Neural Network (CNN)](https://github.com/TanishLal/SentinalAi/blob/main/DB_Sample/input/Convolution%20Neural%20Network%20(CNN).png)
![Long Short Term Memory (LSTM) ](https://github.com/TanishLal/SentinalAi/blob/main/DB_Sample/input/Long%20Short%20Term%20Memory%20(LSTM).png)

---

## System Overview & Pipeline Demo 🎥
SentinelAI is designed for real-time deployment. Once an incident is detected, the system immediately processes the input, classifies the event, and sends alerts to the designated emergency services.
Below are examples of the system in action, showing real-time alerts with annotated video recordings:

**Demo Videos:**  

![SL_event_record_1](https://user-images.githubusercontent.com/34807427/172144654-730d19a4-8f04-4a7c-940a-dacf8586973c.gif)  
![SL_event_record_4](https://user-images.githubusercontent.com/34807427/172144715-94d3b4af-5343-4e2c-bb8c-4a23562e0802.gif)

*Additional input-output examples are available in the repository.*

---

## Setup 🔽
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/SentinelAI.git

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Configure Your Environment:**
   Set up your AWS SageMaker or local environment with GPU support for model training and inference.

4. **Run the Demo:**
   Follow the instructions in the *docs* folder to start the real-time surveillance demo.
   
---

## References 🗞️
-  **https://scontent.ftlv7-1.fna.fbcdn.net/v/t39.8562-6/240838925_377595027406519_956785818926520821_n.pdf**
   
-  **https://arxiv.org/abs/1704.04861**

-  Additional academic and industry publications on HAR and real-time surveillance systems.

  
