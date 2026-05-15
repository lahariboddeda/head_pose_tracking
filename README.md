# Real-Time Head Pose Tracking System

## 📌 Overview

This project is a real-time computer vision application that detects head movement using a webcam. The system estimates whether a user is attentive or looking away from the screen by tracking facial landmarks and monitoring head movement.

The project was developed using Python, OpenCV, MediaPipe, and NumPy.

---

# 🎯 Features

* Real-time webcam access
* Face detection
* Face mesh tracking
* Head movement detection
* Left/Right movement tracking
* Up/Down movement tracking
* Attention monitoring
* Looking-away detection
* Real-time visual feedback

---

# 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

# 📁 Project Structure

```text
head-pose-tracking/
│
├── main.py
├── pose_estimator.py
├── attention_tracker.py
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/lahariboddeda/head-pose-tracking.git
```

---

## 2️⃣ Open Project Folder

```bash
cd head-pose-tracking
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 📷 Output

The application displays:

* Webcam feed
* Face mesh landmarks
* Yaw movement
* Pitch movement
* Attention status
* Looking-away detection

Example:

```text
Status: ATTENTIVE
```

or

```text
Status: LOOKING AWAY
```

---

# 🧠 How It Works

The system uses MediaPipe Face Mesh to detect facial landmarks in real time.

The nose position is compared with the face center to estimate:

* Left/Right movement (Yaw)
* Up/Down movement (Pitch)

Threshold-based logic determines whether the user is looking away from the screen.

---

# 🧪 Test Cases

* Looking straight
* Looking left
* Looking right
* Looking up
* Looking down
* Wearing glasses
* Natural face movement

---

# 🚀 Applications

* Online Exam Proctoring
* Driver Attention Monitoring
* AI Surveillance Systems
* Interview Monitoring
* Human Attention Tracking
* Computer Vision Learning Projects

---

# 🔥 Future Improvements

* Eye gaze tracking
* Multiple face detection
* Recording suspicious events
* Dashboard visualization
* AI-based attention scoring
* Data logging system

---

# 👩‍💻 Author

Lahari

---

# 📚 References

* OpenCV Documentation
  https://opencv.org/

* MediaPipe Documentation
  https://developers.google.com/mediapipe

* NumPy Documentation
  https://numpy.org/

* Python Documentation
  https://docs.python.org/3/
