\# raspi-client-rtsp



Client ringan untuk Raspberry Pi (atau QEMU) yang bertugas:

\- Mengambil video dari kamera RTSP (DVR/IP Camera)

\- Mendeteksi wajah menggunakan OpenCV (Haar Cascade)

\- Jika wajah terdeteksi: mengambil frame, menyimpannya sebagai gambar, dan mengirim ke server

\- Jika tidak ada wajah: tidak ada data yang dikirim

\- Validasi wajah \& antispoofing dilakukan di sisi server (misalnya dengan DeepFace)



---



\## 🔧 Requirements



Install dependencies dengan:



```bash

pip install -r requirements.txt

