# AI-Based Face Recognition Attendance System

## Overview

This project is an AI-powered face recognition attendance system that automates attendance tracking using computer vision. It captures images via webcam, encodes facial features, and matches faces in real time to mark attendance. All records are securely stored in a local SQLite database. The system is modular, with dedicated scripts for encoding, recognition, database management, and a simple web interface for user interaction.

---

## Features

- **Automated Attendance:** Real-time face recognition for marking attendance.
- **Student Data Encoding:** Encodes and stores facial features for each user.
- **Webcam Integration:** Captures live images for registration and recognition.
- **SQLite Database:** Stores attendance and user data securely.
- **Web Interface:** Simple dashboard for login, attendance marking, and reporting.
- **Scene Change Detection:** Improves recognition accuracy by detecting scene changes.
- **User Authentication:** Secure login system.
- **Easy Setup:** All dependencies managed via `requirements.txt`.

---

## Installation

1. **Clone the repository:**
```
git clone https://github.com/SarvagyaRastogi7/AI--Based-Face-Recognition-Attendance-System.git
cd AI--Based-Face-Recognition-Attendance-System
```

2. **Install dependencies:**
```
pip install -r requirements.txt
```


3. **(Optional) Prepare student encodings:**
- Place student images in the appropriate folder.
- Run:
  ```
  python encode_student_data.py
  ```

---

## Usage

- **Start the main application:**
```
python main.py
```
- **Access the web interface:**
- The dashboard will be available at the address shown in your terminal (if using Flask, typically `http://localhost:5000`).
- **Login:** Use your credentials to log in and access attendance features.
- **Mark Attendance:** The system will use your webcam to recognize your face and mark attendance automatically.

---

## Project Structure

```
AI--Based-Face-Recognition-Attendance-System/
│
├── attendance.db              # SQLite database for attendance records
├── camera.py                  # Webcam integration and image capture
├── database.py                # Database operations (insert, update, query)
├── encode_student_data.py     # Script to encode and store student face data
├── encodings.pickle           # Precomputed facial encodings for known faces
├── favicon.ico / .png         # Icon used in the browser tab
├── login.py                   # Handles user authentication and login logic
├── main.py                    # Main entry point of the application
├── photo.py                   # Photo capture and processing utility
├── SceneChangeDetect.py       # Detects scene changes to enhance recognition accuracy
├── requirements.txt           # List of required Python dependencies
├── web/                       # Web interface (HTML, CSS, JS, Flask app)
├── README.md                  # Project documentation
└── SE Project SRS.pdf         # Software Requirements Specification (SRS) document
```


---

## Technologies Used

- **Python 3**
- **OpenCV** – Image processing and webcam access
- **face_recognition** – Facial feature encoding and matching
- **Flask** (if web interface uses Flask) – Web framework
- **SQLite** – Lightweight database
- **Pickle** – Serialization of face encodings

---




