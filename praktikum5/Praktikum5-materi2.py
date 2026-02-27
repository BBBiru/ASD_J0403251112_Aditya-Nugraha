#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ===============================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai") # ujung rekursif
        return
    print("Masuk:", n) # fase stacking
    hitung(n - 1) # pemanggilan rekursif
    print("Keluar:", n) # fase unwinding

hitung(3)
