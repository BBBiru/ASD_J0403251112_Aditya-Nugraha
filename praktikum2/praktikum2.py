#######################################################################
#Aditya Nugraha
#J0403251112
#######################################################################

nama_file = "data_mahasiswa.txt"
def baca_data(nama_file):
    data_dict = {} #inisialisasi data
    with open(nama_file,"r", encoding="UTF-8") as file:
        for baris in file:
            baris = baris.strip() #menghilangkan spasi atau \n
            nim, nama, nilai = baris.split(",") #memasukan baris yang di split ke dalam 3 variabel beda
            data_dict[nim] = { #memasukan dictionary nama dan nilai ke dictionary data_dict
                "Nama" : nama,
                "Nilai" : int(nilai)
                }
        return data_dict #mengembalikan hasil baca data
    
#buka_data = baca_data(nama_file) #memanggil baca data dan memasukannya ke buka data
#print("jumlah data terbaca =", len(buka_data)) #mencetak panjang buka data

#######################################################################
#---Menampilkan data---

def tampilkan_data(data_dict): #membuat header untuk penampilan data
    print("==========Data Mahasiswa==========")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}") #menggunakan < dan > sebagai perataan kiri kanan dan integer sebagai besar kolom
    print("----------------------------------")
    for nim in sorted(data_dict.keys()): #menampilkan data dan mengurutkannya berdasar nim
        nama = data_dict[nim]["Nama"]
        nilai = data_dict[nim]["Nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}") #print
#tampilkan_data(buka_data)

#######################################################################
#---Mencari data---

def cari_data(data_dict):
    nim_cari = input("Masukan NIM yang akan dicari: ")
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["Nama"]
        nilai = data_dict[nim_cari]["Nilai"]
        print("=======Data Mahasiswa Ditemukan=======")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan :(")

#cari_data(buka_data)

#######################################################################
#---Mengubah data---

def ubah_data(data_dict): #fungsi merubah data
    nim = input("Masukan NIM yang akan diubah datanya: ")
    if nim not in data_dict: #memastikan nim ada di data_dict
        print("NIM tidak ditemukan :(")
        return

    try: #memastikan nim adalah integer
        nilai_baru = int(input("masukan nilai yang baru 0-100: "))
    except ValueError:
        print("Nilai harus berupa angka")

    if nilai_baru <0 or nilai_baru >100: #memastikan nim adalah integer dari rentang 0-100
        print("nilai harus dari rentang 0-100")
    
    nilai_lama = data_dict[nim]["Nilai"]
    data_dict[nim]["Nilai"] = nilai_baru
    print(f"data nilai {nilai_lama} telah diganti menjadi {nilai_baru}")

#ubah_data(buka_data)

#######################################################################
#---Menyimpan data---

def simpan_data(nama_file, data_dict):
    with open(nama_file,"w", encoding="UTF-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["Nama"]
            nilai = data_dict[nim]["Nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file, buka_data)
print("data berhasil disimpan")

#######################################################################

buka_data = baca_data(nama_file)
def main(): #membuat main() yaitu kode blok yang akan pertama kali dijalankan
    while True:
        print("=====Menu data=====")
        print("1. tampilkan data")
        print("2. cari data")
        print("3. ubah data")
        print("4. simpan data")
        print("0. keluar")
        pilihan = input("Masukan pilihan: ") #menentukan pilihan menggunakan input
        match pilihan: #memilih perintah menggunakan match-case
            case "1":
                tampilkan_data(buka_data)
            case "2":
                cari_data(buka_data)
            case "3":
                ubah_data(buka_data)
            case "4":
                simpan_data(nama_file,buka_data)
            case "0":
                break

main()