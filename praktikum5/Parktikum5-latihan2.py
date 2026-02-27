#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Latihan 2: Tracing Rekursi
# ===============================================

def countdown(n):
    # Base Case
    if n == 0:
        print("Selesai")
        return
    # Recursion case
    print("Masuk:", n)
    countdown(n - 1) # output 'Masuk' dari 3 akan menjadi 2
    print("Keluar:", n)

countdown(3)

# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# fungsi akan menyimpan data dari sebelumnya yang merupakan n-1
# mencetak output keluar saat selesai dengan code sebelumnya yang dimana adalah fungsi rekursif
# disini fungsi mencetak output keluar dari data yang disimpan sendiri, bukan dari luar( coundown(3) )