# WEEK 1
# Instalasi dan Konfigurasi Dasar Software Network Analyzer Wireshark

## Download Wireshark:
1. Buka situs resmi wireshark.org/download.html di browser, lalu download installer Wireshark versi Windows x64.

<img src="../asset/download.png" width="1000" height="500">

<img src="../asset/download2.png" width="1000" height="500">

## Menjalankan File:
2. Buka file .exe yang sudah selesai diunduh. Jika muncul notifikasi Microsoft Defender SmartScreen, klik tombol "Run" untuk melanjutkan.

<img src="../asset/menjalankan_file.png" width="1000" height="500">

## Setup Wireshark:
3. Setelah setup wireshark terbuka, klik "Next" untuk memulai proses instalasi.

<img src="../asset/setup.png" width="1000" height="500">

## Informasi Sertifikasi:
4. Pada halaman informasi mengenai Wireshark Certified Analyst (WCA), klik "Next" saja untuk lanjut ke tahap berikutnya.

<img src="../asset/setup2.png" width="1000" height="500">

## Menentukan Lokasi Instalasi:
5. Pilih folder tujuan instalasi. Secara default aplikasi akan terinstal di C:\Program Files\Wireshark. Pastikan space hardisk cukup, lalu klik "Next".

<img src="../asset/lokasi_instalasi.png" width="1000" height="500">

## Proses Instalasi:
6. Tunggu proses ekstraksi file dan instalasi background (seperti Visual C++ Redistributable) sampai bar progres terisi penuh.

<img src="../asset/install.png" width="1000" height="500">

## Selesai Instalasi:
7. Setelah instalasi selesai (Completed), klik "Next" lalu klik "Finish" untuk menutup wizard.

<img src="../asset/install2.png" width="1000" height="500">

<img src="../asset/install3.png" width="1000" height="500">

## Verifikasi:
8. Buka menu Start Windows dan cari "Wireshark". Jika aplikasi muncul di hasil pencarian, artinya Wireshark sudah berhasil terinstal dan siap digunakan.

<img src="../asset/buka_apk.png" width="1000" height="500">


## Pemilihan Interface Jaringan:
1. Saat membuka aplikasi, pilih interface yang aktif untuk menangkap paket. Pada percobaan ini, interface "Wi-Fi" dipilih karena perangkat menggunakan koneksi nirkabel.

<img src="../asset/cari_wifi.png" width="1000" height="500">

## Memulai Proses Capture:
2. Klik tombol Start (ikon sirip hiu) untuk memulai proses perekaman trafik. Wireshark akan mulai menampilkan paket data yang lewat secara real-time.

> klik stop
<img src="../asset/klik1.png" width="1000" height="500">

> klik option
<img src="../asset/klik2.png" width="1000" height="500">

> klik start
<img src="../asset/klik3.png" width="1000" height="500">

> klik bagian tengah 
<img src="../asset/klik4.png" width="1000" height="500">

## Akses Materi Praktikum:
3. Untuk menghasilkan trafik HTTP, buka web browser dan akses URL materi praktikum di gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html.

<img src="../asset/salin.png" width="1000" height="500">

4. Setelah halaman dimuat, Anda akan melihat pesan konfirmasi bahwa file lab telah terunduh.

<img src="../asset/hasil_salin.png" width="1000" height="500">

## Filter Paket:
5. Untuk mempermudah analisis, gunakan kolom display filter di bagian atas.
6. Ketikkan filter (misalnya "http") untuk menyaring tampilan agar hanya menunjukkan paket dengan protokol HTTP saja, sehingga paket data yang relevan lebih mudah diamati.

<img src="../asset/http.png" width="1000" height="500">

## Hasil:
7. Berdasarkan hasil capture menggunakan Wireshark, terlihat proses komunikasi HTTP antara client dan server yang terdiri dari HTTP Request (GET) dan HTTP Response (200 OK). File HTML berhasil dikirim dan isi konten dapat dianalisis karena protokol HTTP tidak menggunakan enkripsi.

<img src="../asset/hasil.jpeg" width="1000" height="500">

