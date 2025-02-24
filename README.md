# 🚀 Computer Vision Projects

![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Powered%20by%20OpenCV-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow%20%7C%20PyTorch-orange)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 About This Repository

Welcome to **ComputerVisionProjects**! This repository contains a collection of real-time **Computer Vision** applications implemented using **OpenCV, Mediapipe, and Deep Learning**. Each project includes:

✅ **A ready-to-run script** for direct implementation.
✅ **A modular function file** to reuse the logic in your own projects.

🚀 These projects are designed for real-world applications like **gesture control, face detection, and pose estimation**.

## 📂 Project Structure

```
📦 ComputerVisionProjects
 ┣ 📂 FaceDetection
 ┃ ┣ 📜 face_detection.py  # Direct script to run face detection
 ┃ ┗ 📜 face_utils.py     # Modular functions for face detection
 ┣ 📂 HandDetection
 ┃ ┣ 📜 hand_tracking.py  # Finger counter & volume control script
 ┃ ┗ 📜 hand_utils.py     # Modular hand tracking functions
 ┣ 📂 FaceMeshDetection
 ┃ ┣ 📜 face_mesh.py      # Face mesh detection script
 ┃ ┗ 📜 mesh_utils.py     # Face mesh utility functions
 ┣ 📂 PoseEstimation
 ┃ ┣ 📜 pose_estimation.py # Human pose estimation script
 ┃ ┗ 📜 pose_utils.py     # Pose estimation helper functions
 ┗ 📜 README.md
```

## 🖥️ Projects Included

### 1️⃣ Face Detection 👦📷
- Detect human faces in real-time using OpenCV and Mediapipe.
- Works efficiently even in low-light conditions.
- **Run the script:**
  ```bash
  python FaceDetection/face_detection.py
  ```

### 2️⃣ Hand Detection & Finger Counter ✋🖐
- Detects hands and counts fingers using Mediapipe.
- Used for **gesture-based volume control**.
- **Run the script:**
  ```bash
  python HandDetection/hand_tracking.py
  ```

### 3️⃣ Face Mesh Detection 🕸️😃
- Creates a **468-point face mesh** in real time.
- Helps in applications like **AR filters and facial analysis**.
- **Run the script:**
  ```bash
  python FaceMeshDetection/face_mesh.py
  ```

### 4️⃣ Pose Estimation 🏃🧍
- Estimates full-body pose in real-time using **Mediapipe Pose**.
- Can be used for **fitness tracking, sports analytics, and gaming**.
- **Run the script:**
  ```bash
  python PoseEstimation/pose_estimation.py
  ```

## 🛠 Requirements & Installation

📌 Install dependencies before running the scripts:
```bash
pip install opencv-python mediapipe numpy
```

💡 For better performance, use a **GPU-enabled device**.

## 🤝 Contributions

Feel free to **fork** this repository, improve the implementations, or add new projects. Contributions are welcome! 🚀

🔗 **Stay Connected!** If you like this project, don’t forget to ⭐ star the repository!
