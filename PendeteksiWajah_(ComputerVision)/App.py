import cv2
from datetime import datetime
import time
import os
import mediapipe as mp
import numpy as np

# Membuat folder log & screenshot
os.makedirs("screenshots", exist_ok=True)

# Load model deteksi wajah dari OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

# Timer untuk deteksi wajah hilang
last_seen = time.time()
face_missing_start = None
look_away_start = None  # Tambahan: untuk mendeteksi menoleh

# Inisialisasi MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 1. Deteksi wajah hilang
    if len(faces) == 0:
        if face_missing_start is None:
            face_missing_start = time.time()
        elif time.time() - face_missing_start > 3:
            msg = f"[{now}] wajah tidak terlihat lebih dari 3 detik!"
            print(msg)
            with open("cheating_log.txt", "a") as log:
                log.write(msg + "\n")
            cv2.imwrite(f"screenshots/missing_{datetime.now().strftime('%H%M%S')}.jpg", frame)
            face_missing_start = None
    else:
        face_missing_start = None  # reset jika wajah terlihat

    # 2. Deteksi wajah tidak fokus (menoleh)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Ambil titik mata kiri (33), mata kanan (263), dan hidung (1)
        left_eye = np.array([landmarks[33].x, landmarks[33].y])
        right_eye = np.array([landmarks[263].x, landmarks[263].y])
        nose_tip = np.array([landmarks[1].x, landmarks[1].y])
        eye_center = (left_eye + right_eye) / 2
        nose_to_eye = nose_tip - eye_center

        # Threshold arah menyimpang horizontal = menoleh
        if abs(nose_to_eye[0]) > 0.02:
            if look_away_start is None:
                look_away_start = time.time()
            elif time.time() - look_away_start > 3:
                msg = f"[{now}] Wajah tidak fokus ke layar lebih dari 3 detik!"
                print(msg)
                with open("cheating_log.txt", "a") as log:
                    log.write(msg + "\n")
                cv2.imwrite(f"screenshots/lookaway_{datetime.now().strftime('%H%M%S')}.jpg", frame)
                look_away_start = None
        else:
            look_away_start = None
    else:
        look_away_start = None  # reset jika wajah tidak terdeteksi

    # Tampilkan kotak wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(frame, f"Detected Faces: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Ujian Online Deteksi Kecurangan", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
