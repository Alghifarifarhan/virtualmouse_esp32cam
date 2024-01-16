Tutorial program mouse virtual ESP32 CAM
cara menjalankan program:
1. siapkan alat & bahan yang dibutuhkan yaitu ESP32 CAM, Modul FTDI CP2102, 5 kabel jumper female to female, dan kabel micro-USB.
2. rangkai mikrokontroller menggunakan alat dan bahan diatas seperti pada gambar rangkaian file repository.
3. masuk ke software arduino, buka file web_camera_esp32.ino, lalu hubungkan mikrokontroller yang telah di rangkai menggunakan kabel micro-USB ke PC/Laptop.
4. compile code pada software arduino hingga selesai, setelah itu buka serial monitor, lalu cabut kabel jumper yang menghubungkan pin 100 dengan GND pada ESP32 CAM, lalu klik tombol reset pada ESP32 CAM, maka akan muncul ip kamera berserta resolusi nya.
5. copy ip kamera dan salah satu resolusi nya, kemudian buat folder yang di dalam nya berisi file deteksitangan.py dan virtualmouse.py, setelah itu buka folder menggunakan vscode atau kode editor yang kalian pakai.
6. pada file deteksitangan.py dan virtualmouse.py, masukan kode ip kamera yg telah di copy pada serial monitor arduino.
7. lalu jalankan kode python dan program akan berjalan.
