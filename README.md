# Atomy Automation
Atomy Automation adalah proyek Python yang mengotomatisasi proses login dan pendaftaran pengguna di situs web Atomy menggunakan Selenium.

## Persyaratan
Sebelum memulai, pastikan Anda telah memenuhi persyaratan berikut:
- Instalasi Python 3.x
- Instalasi browser Chrome
- Instalasi Webdriver untuk Chrome (chromedriver)
- Instalasi paket Python yang diperlukan, Anda dapat menginstalnya dengan cara berikut.
  ```
  pip install -r requirements.txt
  ```
## Memulai
Untuk memulai proyek ini, ikuti langkah-langkah berikut:
1. Klon proyek ini:
   ```
   git clone https://github.com/RizkyRauf/Atomy_Automation.git
   ```
2. Pindah ke direktori proyek:
   ```
   cd Atomy_Automation
   ```
3. Pastikan Anda menempatkan data login dan registrasi Anda di direktori data sebagai login_data.xlsx dan registration_data.xlsx masing-masing.
4. Jalankan skrip utama untuk memulai otomatisasi:
   ```
   python main.py
   ```

## Penggunaan
- Modifikasi data login dan registrasi dalam direktori data sesuai kebutuhan.
- Jalankan skrip main.py untuk mengotomatisasi proses login dan pendaftaran.
- Periksa hasil dan data di direktori data.

## Struktur Direktori
Direktori proyek terstruktur sebagai berikut:

- config/: Berkas konfigurasi.
- data/: Berkas data untuk login dan registrasi.
- modules/: Modul Python untuk login dan registrasi.
- main.py: Skrip utama untuk menjalankan otomatisasi.
- requirements.txt: Daftar paket Python yang diperlukan.
