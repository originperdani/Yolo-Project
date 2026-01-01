TUGAS 8 - IMPLEMENTASI OBJECT DETECTION MENGGUNAKAN YOLO

Nama        : Origin Putramas Perdani
NIM         : 231011403299
Mata Kuliah : Machine Learning

================================================================================
DESKRIPSI PROYEK
================================================================================
Proyek ini bertujuan untuk mengimplementasikan sistem deteksi objek cerdas (Object Detection) yang berfokus pada identifikasi dan klasifikasi jenis tas. Sistem ini dirancang untuk mendeteksi dua kategori utama: Backpack (Tas Punggung) dan Suitcase (Koper). 

Menggunakan algoritma YOLOv8 model Medium (yolov8m.pt), sistem ini mampu mengenali objek dalam berbagai kondisi visual dengan tingkat akurasi yang tinggi. Proyek ini juga mencakup penyesuaian logika deteksi untuk mengelompokkan berbagai jenis tas jinjing (handbag) ke dalam kategori backpack sesuai dengan spesifikasi tugas, serta mampu memproses input berupa gambar statis maupun video secara otomatis.

================================================================================
TOOLS & LIBRARIES
================================================================================
Teknologi dan pustaka yang digunakan dalam pengembangan proyek ini meliputi:
1. Python (Bahasa Pemrograman Utama)
2. Ultralytics YOLOv8 
3. OpenCV 
4. OS & Re 

================================================================================
DATASET
================================================================================
Dataset yang digunakan dalam proyek ini dikurasi dari berbagai sumber untuk memastikan variasi data yang representatif:
1. Foto Pribadi
2. Pinterest 

Dataset dibagi menjadi dua jenis media input:
- Gambar (Format: .jpg, .png, .jpeg)
- Video (Format: .mp4)

================================================================================
STRUKTUR DIREKTORI
================================================================================
- dataset/
  - Gambar/      : Berisi kumpulan file gambar untuk diuji.
  - Video/       : Berisi file video untuk diuji.
- output/
  - hasil_gambar/ : Menyimpan hasil deteksi pada gambar (dengan bounding box).
  - hasil_video/  : Menyimpan hasil deteksi pada video.
- Tugas8_Yolo.py  : Script utama program.
- yolov8m.pt      : Model pre-trained YOLOv8 Medium.

================================================================================
CARA MENJALANKAN PROGRAM
================================================================================
1. Pastikan semua library yang dibutuhkan telah terinstal:
   pip install ultralytics opencv-python

2. Letakkan dataset gambar pada folder 'dataset/Gambar' dan video pada 'dataset/Video'.

3. Jalankan script utama menggunakan Python:
   python Tugas8_Yolo.py

4. Proses deteksi akan berjalan otomatis. Sistem akan memindai folder input dan menerapkan model YOLOv8 pada setiap file.

5. Hasil deteksi (Output) dapat dilihat pada direktori:
   - Gambar: output/hasil_gambar
   - Video : output/hasil_video
