# STUDIKASUS6_keyrani_alexa_putri_093

nama = keyrani alexa putri

nim = 2609116093

kelas = C 



  penjelasan json 


File `studikasus.json` digunakan untuk menyimpan data mahasiswa dalam bentuk JSON. Di dalamnya terdapat data seperti **nama, NIM, mata kuliah, dan nilai**.

* `"nama": "Eja"` → berisi nama mahasiswa.
* `"nim": "2609116062"` → berisi NIM mahasiswa.
* `"mata_kuliah": "Teknik Kimia"` → menunjukkan mata kuliah yang diambil.
* `"nilai": 100.0` → berisi nilai mahasiswa.

Tanda `[` dan `]` digunakan untuk menandakan bahwa data tersebut berbentuk **list**, sedangkan `{` dan `}` digunakan untuk menampung data satu mahasiswa.
<img width="1242" height="497" alt="Screenshot 2026-10-07 222040" src="https://github.com/user-attachments/assets/68f50989-c903-4dc2-bf89-bc17464d4246" />



penjelasan python.


Program ini digunakan untuk **mencatat dan menampilkan nilai mahasiswa**. Pertama, `import json` digunakan supaya program bisa membaca dan menyimpan data ke file JSON.

Pada bagian awal, file `studikasus.json` dibuka dan datanya dimasukkan ke dalam variabel `daftar_nilai`. Setelah itu ada fungsi `tambah_nilai()` untuk menambahkan data mahasiswa. User diminta memasukkan nama, NIM, mata kuliah, dan nilai ujian. Data tersebut kemudian dibuat dalam bentuk dictionary dan dimasukkan ke `daftar_nilai`.

Setelah data ditambahkan, program menyimpannya kembali ke file JSON menggunakan `json.dump()`. Lalu muncul pesan **"Nilai berhasil disimpan!"** sebagai tanda bahwa data sudah tersimpan.

Selanjutnya, fungsi `lihat_nilai()` digunakan untuk melihat data nilai yang sudah tersimpan. Kalau belum ada data, program akan menampilkan pesan **"Belum ada data nilai."**. Kalau sudah ada, data akan ditampilkan satu per satu menggunakan `enumerate()`.

Terakhir, terdapat menu utama yang berjalan dengan `while True`. Ada tiga pilihan, yaitu **melihat riwayat nilai, menambah nilai, dan keluar dari program**. Jika memilih menu 3, program menampilkan "Terima kasih." lalu berhenti dengan `break`. Kalau memasukkan pilihan yang tidak tersedia, program akan memberi pesan **"Menu tidak tersedia."**

<img width="1908" height="967" alt="Screenshot 2026-10-08 001536" src="https://github.com/user-attachments/assets/41b6d3cf-fb5c-4a83-a731-8c9eae61d97a" />
<img width="1841" height="791" alt="Screenshot 2026-10-08 001548" src="https://github.com/user-attachments/assets/702ca1eb-6e80-4d19-bdcf-0ddacf4a5539" />



penjelasan output


Pada output tersebut, program menampilkan menu **Sistem Pencatatan Nilai** yang memiliki tiga pilihan, yaitu melihat riwayat nilai, menambah nilai, dan keluar.

Pertama, saat memilih **menu 1**, program menampilkan data mahasiswa yang sudah tersimpan, yaitu nama Eja, NIM, mata kuliah Teknik Kimia, dan nilai 100.0.

Kemudian pada **menu 2**, program meminta pengguna memasukkan data mahasiswa. Setelah semua data diisi, muncul pesan **"Nilai berhasil disimpan!"**, yang berarti data berhasil ditambahkan dan disimpan ke file JSON.

Terakhir, pengguna memilih **menu 3** untuk keluar dari program. Program kemudian menampilkan **"Terima kasih."** dan kembali ke terminal.

<img width="1820" height="957" alt="Screenshot 2026-10-07 222705" src="https://github.com/user-attachments/assets/499e9b25-5040-4cc6-b5d7-f6b0518d09c4" />



**Penutup:**

Dari program yang sudah dibuat, dapat disimpulkan bahwa program ini dapat digunakan untuk mencatat, menyimpan, dan menampilkan data nilai mahasiswa dengan memanfaatkan file JSON. Program juga sudah dilengkapi dengan menu untuk menambah nilai, melihat riwayat nilai, dan keluar dari program. Dengan program ini, proses pencatatan nilai menjadi lebih mudah dan data dapat disimpan dengan lebih teratur.



