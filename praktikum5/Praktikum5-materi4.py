#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ===============================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    biner(n, hasil + "0") # Choose + Explore: tambah '0'
    
    biner(n, hasil + "1") # Choose + Explore: tambah '1'

biner(4)