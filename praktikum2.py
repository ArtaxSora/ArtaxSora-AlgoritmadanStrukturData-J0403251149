nama_file = "dataMahasiswa.txt"
#========================
# Praktikum 2 - Python
# Latihan Dasar 1 - Membuat Fungsi Load Data
# ========================
def load_data_mahasiswa(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim] = {"nama": nama, "nilai": nilai_int}

    return data_dict

# buka_data = load_data_mahasiswa(nama_file)
# print("jumlah data mahasiswa:", len(buka_data))

#========================
# Praktikum 2 - Python
# Latihan Dasar 2 - membuat fungsi menampilkan data
# ========================
def tampilkan_data_mahasiswa(data_dict):
    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return
    # membuat Header Tabel
    print("\n====== Data Mahasiswa ======")
    print(f"{'NIM': <10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")
        # print("-" * 32)
# memanggil fungsi tampilkan data
# tampilkan_data_mahasiswa(buka_data)

#========================
# Praktikum 2 - Python
# Latihan Dasar 3 - membuat fungsi mencari data
# ========================
def cari_data_mahasiswa(data_dict):
    nim_cari = input("\nMasukkan NIM yang dicari: ")

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("\nData Mahasiswa Ditemukan:")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")
# cari_data_mahasiswa(buka_data)

#========================
# Praktikum 2 - Python
# Latihan Dasar 4 - membuat fungsi update data
# ========================
def update_data_mahasiswa(data_dict):
    nim = input("\nMasukkan NIM yang akan diupdate: ")

    if nim not in data_dict:
        print("Data dengan NIM tersebut tidak ditemukan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: "))
    except ValueError:
        print("Nilai harus berupa angka.")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100.")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil!{nim} - {data_dict[nim]['nama']}: {nilai_lama} -> {nilai_baru}")
# update_data_mahasiswa(buka_data)

#========================
# Praktikum 2 - Python
# Latihan Dasar 5 - membuat fungsi simpan data
# ========================

def simpan_data_mahasiswa(data_dict, nama_file):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data_mahasiswa(buka_data, nama_file)
print("Data mahasiswa telah disimpan ke file dataMahasiswa.txt")

#==================================================
# Praktikum 2 - Python
# Latihan Dasar 6 - membuat fungsi menu data
#==================================================
def menu_data_mahasiswa():
    data_mahasiswa = load_data_mahasiswa(nama_file)
    while True:
        print("\n===== Menu Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("0. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data_mahasiswa(data_mahasiswa)
        elif pilihan == "2":
            cari_data_mahasiswa(data_mahasiswa)
        elif pilihan == "3":
            update_data_mahasiswa(data_mahasiswa)
        elif pilihan == "4":
            simpan_data_mahasiswa(data_mahasiswa, nama_file)
            print("Data mahasiswa telah disimpan.")
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
if __name__ == "__main__":
    menu_data_mahasiswa()
