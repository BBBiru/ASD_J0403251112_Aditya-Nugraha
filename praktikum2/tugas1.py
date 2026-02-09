# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Aditya Nugraha
# NIM : J0403251112
# Kelas : TPL-A1
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file="stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """

    stok_dict = {}
    with open(nama_file, "r", encoding="UTF-8") as file: #membuka file dengan mode read
        for baris in file: #pengulangan mengambil baris
            baris = baris.strip() #memotong new line (\n) dari baris
            KodeBarang, NamaBarang, Stok = baris.split(",") #memasukkan value kedalam variabel temporary dan memisahkan setiap value
            stok_dict[KodeBarang] = { #assign kedalam dictionary utama
                "nama" : NamaBarang,
                "stok" : int(Stok)
                }

    # TODO: Buka file dan baca seluruh baris
    # Hint: with open(nama_file, "r", encoding="utf-8") as f:
    # TODO: Untuk setiap baris:
    # - gunakan strip() untuk menghilangkan \n
    # - split(",") untuk memisahkan kolom
    # - simpan ke dictionary  
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """

    with open(nama_file, "w", encoding="UTF-8") as file: #membuka file dengan mode write
        for KodeBarang in sorted(stok_dict.keys()): #mengambil setiap kode barang
            NamaBarang = stok_dict[KodeBarang]["nama"] #mengambil nama barang dari kode
            Stok = stok_dict[KodeBarang]["stok"] #mengambil jumlah stok dari kode
            file.write(f"{KodeBarang},{NamaBarang},{Stok}\n") #memasukan dictionary ke dalam file

    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """

    print("------------Stok Barang------------") #membuat header
    print(f"{'Kode':<8} | {'Nama':<16} | {'Stok':>4}")
    print("-"*35)

    for KodeBarang in sorted(stok_dict.keys()): #pengulangan mengambil setiap kode barang
        NamaBarang = stok_dict[KodeBarang]["nama"] #mengambil nama barang dari kode
        Stok = stok_dict[KodeBarang]["stok"] #mengambil jumlah stok dari kode
        print(f"{KodeBarang:<8} | {NamaBarang:<16} | {Stok:>4}") #menampilkan barang dengn print format

    # TODO: Jika kosong, tampilkan pesan stok kosong
    # TODO: Tampilkan dengan format rapi: kode | nama | stok

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """

    kode = input("Masukkan kode barang: ").strip() #masukkan kode barang
    if kode in stok_dict: #mengecek keberadaan kode dalam dictionary
        NamaBarang = stok_dict[kode]["nama"] #mengambil nama barang dari kode
        Stok = stok_dict[kode]["stok"] #mengambil stok barang dari kode
        print("-----------Detail Barang-----------") #menampilkan detail dari barang
        print(f"Kode barang : {kode}")
        print(f"Nama barang : {NamaBarang}")
        print(f"Jumlah stok : {Stok}")
    else:
        print("Barang tidak ditemukan :(") #eksekusi jika kode tidak ditemukan
        return
    # TODO: Cek apakah kode ada di dictionary
    # Jika ada: tampilkan detail barang
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip() #memasukkan kode barang baru
    if kode in stok_dict.keys(): #mengecek keberadaan kode duplikat dalam dictionary. akan return jika ditemukan duplikat
        print("Kode sudah digunakan")
        return
    
    nama = input("Masukkan nama barang: ").strip() #memasukkan nama barang baru
    
    while True: #pengulangan error handling untuk stok awal
        try:
            stok_awal = int(input("Masukkan stok barang: ")) #memasukkan stok awal barang
        except ValueError: #jika input bukan integer
            print("Berikan angka yang sesuai! >:(")
        else:
            break #keluar dari pengulangan jika input integer
    
    stok_dict[kode] = { #memasukkan data barang baru ke dalam dictionary
        "nama" : nama,
        "stok" : int(stok_awal)}

    print("Barang berhasil ditambahkan :)")
    # TODO: Validasi kode tidak boleh duplikat
    # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
    # TODO: Input stok awal (integer)
    # Hint: stok_awal = int(input(...))
    # TODO: Simpan ke dictionary

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() #masukkan kode barang
    if kode not in stok_dict.keys(): #mengecek keberadaan kode dalam dictionary
        print("Kode tidak ada di data barang :(") #ekseskusi jika kode tidak ditemukan
        return

    # TODO: Cek apakah kode ada di dictionary
    # Jika tidak ada: tampilkan pesan dan return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "1" or pilihan == "2": #mengecek jika pilihan adalah 1 atau 2
        pass
    else:
        print("Masukan pilihan dengan benar! >:(") #eksekusi jika pilihan bukan 1 atau 2
        return
    
    while True: #pengulangan error handling untuk perubahan 
        try:
            perubahan = int(input("Masukan jumlah modifikasi: ")) #memasukkan perubahan
        except ValueError:
            print("Berikan angka yang sesuai! >:(") #eksekusi jika input bukan integer
        else:
            break

    stok_lama = stok_dict[kode]["stok"] #membuat variabel sementara

    if pilihan == "1": #eksekusi jika pilihan = 1
        stok_dict[kode]["stok"] = stok_lama + perubahan
        print("Perubahan berhasil :)")
        print(f"Jumlah lama: {stok_lama} >>>>> Jumlah baru: {stok_dict[kode]['stok']}")
    elif pilihan == "2": #eksekusi jika pilihan = 2
        stok_dict[kode]["stok"] = stok_lama - perubahan
        print("Perubahan berhasil :)")
        print(f"Jumlah lama: {stok_lama} >>>>> Jumlah baru: {stok_dict[kode]['stok']}")


    # TODO: Input jumlah perubahan stok
    # Hint: jumlah = int(input("Masukkan jumlah: "))
    # TODO:
    # - Jika pilihan 1: stok = stok + jumlah
    # - Jika pilihan 2: stok = stok - jumlah
    # - Jika hasil < 0: batalkan dan tampilkan error

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    # Menjalankan program utama
    
    
if __name__ == "__main__":
    main()