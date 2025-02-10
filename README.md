# Bike Sharing Dashboard

## 📌 Deskripsi
Dashboard interaktif ini dibuat menggunakan **Streamlit** untuk menganalisis data peminjaman sepeda berdasarkan musim dan suhu. Dashboard ini memungkinkan pengguna untuk memfilter data berdasarkan musim serta melihat hubungan antara suhu dan jumlah pengguna sepeda.

## 🚀 Fitur Utama
- **Visualisasi Penggunaan Sepeda Berdasarkan Musim**
- **Analisis Hubungan Temperatur dan Jumlah Pengguna**
- **Insight dari Data**

## 📂 Struktur Repository
```
submission/
├─── dashboard
   ├─── bike_sharing_full.csv
   ├─── dashboard.py
├─── data
   ├─── day.csv
   ├─── hour.csv     
├─── notebook.ipynb
├─── url.txt  
├─── requirements.txt      
└─── README.md             
```

## 🔧 Instalasi dan Menjalankan Secara Lokal
1. Clone repository ini:
   ```bash
   git clone https://github.com/Kenzao291108/bike-sharing-dashboard
   cd bike-sharing-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan dashboard:
   ```bash
   streamlit run dashboard.py
   ```
4. Buka browser dan akses **http://localhost:8501**

## ☁️ Deploy ke Streamlit Cloud
1. **Upload kode ke GitHub**
2. **Buka [Streamlit Cloud](https://share.streamlit.io/)**
3. **Klik "Deploy an app"**
4. **Pilih repository GitHub**
5. **Tentukan path aplikasi (dashboard.py)**
6. **Klik "Deploy" dan tunggu prosesnya selesai**

## 📌 Insight dari Analisis
- **Penggunaan sepeda meningkat pada musim panas dan menurun di musim dingin.**
- **Terdapat korelasi positif antara suhu dan jumlah pengguna sepeda.**

---
🚲 **Selamat menganalisis data Bike Sharing!** 🚀
