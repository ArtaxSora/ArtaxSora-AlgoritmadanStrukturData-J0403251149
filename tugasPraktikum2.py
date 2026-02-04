# Nama file penyimpanan data barang
nama_file = "Stock_barang.txt"


# ========================
# Fungsi Load Data Barang
# ========================
def load_data_barang(nama_file):
    # Dictionary untuk menampung data barang
    data_dict = {}

    # Membuka file dalam mode baca
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            # Menghapus spasi dan newline di akhir baris
            baris = baris.strip()

            # Memisahkan data berdasarkan koma
            parts = baris.split(",")

            # Validasi: harus ada 3 bagian data
            if len(parts) != 3:
                continue

            # Menyimpan ke variabel
            kode, nama, jumlah_str = parts

            # Mengubah jumlah dari string ke integer
            jumlah_int = int(jumlah_str)

            # Menyimpan data ke dictionary
            data_dict[kode] = {"nama": nama, "jumlah": jumlah_int}

    # Mengembalikan dictionary data barang
    return data_dict


# ========================
# Fungsi Tampilkan Data
# ========================
def tampilkan_data_barang(data_dict):
    # Jika data kosong
    if len(data_dict) == 0:
        print("Data barang kosong.")
        return

    # Header tabel
    print("\n====== Data Barang ======")
    print(f"{'Kode':<10} | {'Nama':<12} | {'Jumlah':>6}")
    print("-" * 34)

    # Menampilkan data yang sudah diurutkan berdasarkan kode
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        jumlah = data_dict[kode]["jumlah"]
        print(f"{kode:<10} | {nama:<12} | {jumlah:>6}")


# ========================
# Fungsi Cari Data
# ========================
def cari_data_barang(data_dict):
    # Input kode barang yang dicari
    kode_cari = input("\nMasukkan kode barang: ")

    # Jika ditemukan di dictionary
    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        jumlah = data_dict[kode_cari]["jumlah"]

        print("\nData Barang Ditemukan:")
        print(f"Kode  : {kode_cari}")
        print(f"Nama  : {nama}")
        print(f"Jumlah: {jumlah}")
    else:
        print("Data tidak ditemukan.")


# ========================
# Fungsi Update Data
# ========================
def update_data_barang(data_dict):
    # Input kode yang ingin diupdate
    kode = input("\nMasukkan kode barang yang akan diupdate: ")

    # Jika kode tidak ada
    if kode not in data_dict:
        print("Data tidak ditemukan.")
        return

    # Input jumlah baru dengan validasi angka
    try:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    # Validasi jumlah tidak boleh negatif
    if jumlah_baru < 0:
        print("Jumlah tidak boleh negatif.")
        return

    # Menyimpan jumlah lama
    jumlah_lama = data_dict[kode]["jumlah"]

    # Update jumlah baru
    data_dict[kode]["jumlah"] = jumlah_baru

    print(f"Update berhasil! {kode} - {data_dict[kode]['nama']}: {jumlah_lama} -> {jumlah_baru}")


# ========================
# Fungsi Tambah Data Barang
# ========================
def tambah_data_barang(data_dict):
    # Input kode barang baru
    kode = input("\nMasukkan kode barang baru: ")

    # Cek apakah kode sudah ada
    if kode in data_dict:
        print("Kode barang sudah ada. Gunakan kode lain.")
        return

    # Input nama barang
    nama = input("Masukkan nama barang: ")

    # Input jumlah dengan validasi angka
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    # Validasi jumlah tidak negatif
    if jumlah < 0:
        print("Jumlah tidak boleh negatif.")
        return

    # Menambahkan data baru ke dictionary
    data_dict[kode] = {"nama": nama, "jumlah": jumlah}

    print("Data barang berhasil ditambahkan.")


# ========================
# Fungsi Simpan Data
# ========================
def simpan_data_barang(data_dict, nama_file):
    # Membuka file dalam mode tulis (menimpa file lama)
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            jumlah = data_dict[kode]["jumlah"]

            # Menulis data ke file
            file.write(f"{kode},{nama},{jumlah}\n")


# ========================
# Menu Utama Program
# ========================
def menu_data_barang():
    # Memuat data dari file saat program dimulai
    data_barang = load_data_barang(nama_file)

    # Loop menu agar terus berjalan sampai user keluar
    while True:
        print("\n===== Menu Data Barang =====")
        print("1. Tampilkan Data")
        print("2. Cari Data")
        print("3. Update Data")
        print("4. Tambah Data")
        print("5. Simpan Data")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        # Menjalankan fungsi sesuai pilihan user
        if pilihan == "1":
            tampilkan_data_barang(data_barang)
        elif pilihan == "2":
            cari_data_barang(data_barang)
        elif pilihan == "3":
            update_data_barang(data_barang)
        elif pilihan == "4":
            tambah_data_barang(data_barang)
        elif pilihan == "5":
            simpan_data_barang(data_barang, nama_file)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")


# Menjalankan program jika file dieksekusi langsung
if __name__ == "__main__":
    menu_data_barang()
