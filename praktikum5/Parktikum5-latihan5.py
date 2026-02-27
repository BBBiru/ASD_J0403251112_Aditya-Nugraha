#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Studi Kasus: Generator PIN
# ===============================================

def buat_pin(panjang, hasil=""):

    # base case
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # recursive case
    for angka in ["0", "1", "2"]: #kumpulan angka yang akan dipakai
        buat_pin(panjang, hasil + angka) #menambah angka kedalam hasil

buat_pin(3)

# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# dengan mengecek apakah angka tersebut sudah ada di dalam hasil
# jika ada, syntax 'for' akan melanjutkan perulangan

print("Hasil Revisi =============================")

def buat_pin_revisi(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        if angka in hasil: # mengecek apakah angka ada di dalam hasil
            continue # jika ada, akan melanjutkan for ke undex berikutnya tanpa merekursi
        buat_pin_revisi(panjang, hasil + angka)

buat_pin_revisi(3)