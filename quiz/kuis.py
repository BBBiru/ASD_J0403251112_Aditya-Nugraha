# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Aditya Nugraha
# NIM     : J0403251112
# Kelas   : TPL-A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    # TODO: Implementasikan kode pembacaan file di sini
    database_buku = {} #inisialisasi database
    with open(nama_file, 'r', encoding= 'UTF-8') as file: #membuka file dengan 'r' untuk read dan encoding UTF-8
        for baris in file: #looping untuk setiap baris di file
            baris = baris.strip() #menghapus /n pada baris
            kode_buku, judul, harga = baris.split(',') #me-assign data ke variabel yang sesuai
            database_buku[kode_buku] = { #membuat buku dengan kode buku sebagai key dan dictionary baru sebagai value
                'Judul' : judul,
                'Harga' : int(harga) #mengganti harga menjadi integer
            }
    return database_buku #mengembalikan database buku dalam bentuk dictionary mentah

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul): #fungsi saat inisialisasi objek baru
        self.data = judul #mengambil judul dan dimasukan ke data objek
        self.next = None #pointer ke objek berikutnya

class LinkedListPromosi: 
    def __init__(self): #fungsi inisialisasi linked list baru
        self.head = None #me-assign head (karena belum ada, maka None)

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        # TODO: Implementasikan penambahan node
        node_baru = Node(judul) #menginisialisasi objek (sebut B1)
        temp = self.head #menjadikan head sebagai awal traversal

        if temp is None: #jika head kosong, maka tidak ada data sama sekali di linked list
            self.head = node_baru #maka B1 akan menjadi head linked list
            return
        
        while temp.next is not None: #loop traversal selama pointer temp berikutnya merujuk ke sesuatu
            temp = temp.next #perpindahan
        temp.next = node_baru #membuat pointer temp berikutnya merujuk ke B1

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # TODO: Implementasikan traversal linked list
        if self.head is None: #kondisi jika tidak ada buku di daftar promosi
            print("Tidak ada buku dalam daftar promosi")
            return
        
        temp = self.head #menjadikan head sebagai awal traversal
        while temp.next is not None: #loop traversal selama pointer temp berikutnya merujuk ke sesuatu
            print(temp.data, " >>> ", end="") #pertengahan/awal
            temp = temp.next #perpindahan
        print(temp.data, " >>> ", end="none") #akhir

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self): #fungsi inisialisasi antrean kasir
        self.antrean = [] #data sebagai list

    def tambah_antrean(self, nama_pelanggan): #fungsi menambah antrean
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO
        antrean = self.antrean #mengassign data antrean ke variabel antrean
        antrean.append(nama_pelanggan) #menambahkan nama pelanggan ke antrean

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO
        antrean = self.antrean #mengassign data antrean ke variabel antrean
        if len(antrean) == 0: #jika antrean kosong
            print("Tidak ada antrean") #keluar dari fungsi ini
        else:
            nama_pelanggan = antrean.pop(0) #mengambil index pertama antrean, memasukkannya kedalam nama_pelanggan dan menghapusnya
            print(f"Berhasil melayani {nama_pelanggan}") #printf dengan variabel nama_pelanggan

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga): #fungsi urutkan treansaksi, menggunakan Insertion Sort
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # TODO: Implementasikan algoritma sorting secara manual
    if list_harga is None: #jika list kosong
        return print("Tidak ada riwayat transaksi") #akan keluar dari fungsi
    
    for i in range(1,len(list_harga)): #loop i, dimulai dari index 1 karena menganggap index 0 telah diurutkan
        while i != 0: #selama index tidak sampai 0
            if list_harga[i] > list_harga[i-1]: #membandingkan harga dengan index sebelumnya
                list_harga[i], list_harga[i-1] = list_harga[i-1], list_harga[i] #jika lebih besar, menukar keduanya
                i -= 1 #memindahkan index, mengikuti data sebelumnya
            else:
                break #jika harga lebih kecil, menganggap sudah terurut
        
    return list_harga #mengembalikan list harga yang sudah terurut

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue/Dequeue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            pil_3 = True
            while pil_3 is True:
                pil_antrean = input("Ingin menambah atau melayani antrean? (1/2): ")
                if pil_antrean == "1":
                    nama = input("Nama Pelanggan: ")
                    antrean_toko.tambah_antrean(nama)
                    pil_3 = False
                    # Tambahkan logika untuk melayani jika diperlukan
                elif pil_antrean == "2":
                    antrean_toko.layani_pelanggan()
                    pil_3 = False
                else:
                    continue

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()