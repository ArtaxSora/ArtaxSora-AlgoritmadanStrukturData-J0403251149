#Praktikum 1 : Konsep adt dan file handling
#latihan dasar 1a : membaca seluruh isi file

#membuka file dengan mode read (r)

with open("dataMahasiswa.txt", "r",encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)