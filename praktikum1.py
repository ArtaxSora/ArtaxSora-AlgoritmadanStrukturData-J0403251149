#==================================================
#Praktikum 1 : Konsep adt dan file handling
#latihan dasar 1a : membaca seluruh isi file
#==================================================
#membuka file dengan mode read (r)

#membuka file dalam satu baris
with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("------Hasil Read-------")
print("Tipe Data", type(isi_file))
print("Jumlah karakter:", len(isi_file))
print("Jumlah baris:", isi_file.count("\n") + 1)

#membuka file per baris
print("------Membaca per baris-------")
jumlah_baris = 0
with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isi baris:", baris)

#==================================================
#Praktikum 1 : Konsep adt dan file handling
#latihan dasar 2 : Parsing baris menjadi kolom data
#==================================================
with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",") #mengambil dan parsing data berdasarkan karakter koma
        print("NIM", nim,"| Nama:", nama, "| Nilai:", nilai)
    

#==================================================
#Praktikum 1 : Konsep adt dan file handling
#latihan dasar 3 : membaca file dan menyimpan pada list
#==================================================
data_mahasiswa = [] #membuat list kosong untuk menampung data mahasiswa

with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")
        data_mahasiswa.append([nim,nama,int(nilai)]) #menambahkan data mahasiswa ke dalam list

print("====== Data Mahasiswa ======")
print(data_mahasiswa)

print("===== Jumlah Mahasiswa =====")
print("Jumlah Mahasiswa:", len(data_mahasiswa))

print("===== Menampilkan Data Record Tertentu ===========")
print("Data Mahasiswa ke-2:", data_mahasiswa[1]) #menampilkan data mahasiswa ke-2

#==================================================
#Praktikum 1 : Konsep adt dan file handling
#latihan dasar 4 : membaca file dan menyimpan pada dictionary
#==================================================

data_mahasiswa_dict = {} #membuat dictionary kosong untuk menampung data mahasiswa
with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")

        data_mahasiswa_dict[nim] = {"nama": nama, "nilai": int(nilai)} #menambahkan data mahasiswa ke dalam dictionary

print("====== Data Mahasiswa dalam Dictionary ======")
print(data_mahasiswa_dict)