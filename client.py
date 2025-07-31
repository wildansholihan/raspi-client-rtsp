# client.py

import cv2
import os
import requests
import time
from config import RTSP_URL, SERVER_URL

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Buat folder penyimpanan kalau belum ada
os.makedirs("capture", exist_ok=True)

# Buka RTSP stream
cap = cv2.VideoCapture(RTSP_URL)

if not cap.isOpened():
    print("❌ Tidak dapat membuka RTSP stream.")
    exit()

print("📡 RTSP stream dibuka. Menunggu deteksi wajah...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Gagal membaca frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        timestamp = int(time.time())
        filename = f"capture/face_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Wajah terdeteksi, disimpan: {filename}")

        # Kirim ke server
        try:
            with open(filename, "rb") as img_file:
                response = requests.post(SERVER_URL, files={"image": img_file})
                if response.status_code == 200:
                    print("✅ Berhasil dikirim ke server.")
                else:
                    print(f"⚠️ Gagal upload. Status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Error saat upload: {e}")
        
        # Tunggu 5 detik agar tidak spam
        time.sleep(5)

cap.release()