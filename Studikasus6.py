import json

file_data = "studikasus.json"

with open(file_data, "r", encoding="utf-8") as file:
    daftar_nilai = json.load(file)


def tambah_nilai():
    nama = input("Nama mahasiswa: ")
    nim = input("NIM mahasiswa: ")
    matkul = input("Mata kuliah: ")
    nilai = float(input("Nilai ujian: "))

    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "mata_kuliah": matkul,
        "nilai": nilai
    }

    daftar_nilai.append(mahasiswa)

    with open(file_data, "w", encoding="utf-8") as file:
        json.dump(daftar_nilai, file, indent=4)

    print("Nilai berhasil disimpan!")


def lihat_nilai():
    print("\n=== RIWAYAT NILAI MAHASISWA ===")

    if not daftar_nilai:
        print("Belum ada data nilai.")
    else:
        for nomor, mahasiswa in enumerate(daftar_nilai, 1):
            print(nomor, mahasiswa)


while True:
    print("\n=== SISTEM PENCATATAN NILAI ===")
    print("1. Lihat riwayat nilai")
    print("2. Tambah nilai")
    print("3. Keluar")

    menu = input("Masukkan pilihan: ")

    if menu == "1":
        lihat_nilai()

    elif menu == "2":
        tambah_nilai()

    elif menu == "3":
        print("Terima kasih.")
        break

    else:
        print("Menu tidak tersedia.")