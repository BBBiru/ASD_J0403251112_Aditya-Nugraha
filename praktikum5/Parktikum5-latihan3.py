#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Latihan 3: Mencari Nilai Maksimum
# ===============================================

def cari_maks(data, index=0):

 # Base case
    if index == len(data) - 1:
        return data[index]
    
 # Recursive case
 # Masuk
    maks_sisa = cari_maks(data, index + 1)
    # Keluar
    if data[index] > maks_sisa: # membandingkan data dengan yang paling besar dari rekursi sebelumnya
        return data[index] # jika lebih besar: mengambil data menjadi yang lebih besar
    else: 
        return maks_sisa # jika tidak: data yang lebih besar tidak diubah
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Diskusi dan jelaskan alur program serta base case dan recursive call.
# Base case
# base akan mengembalikan data di index nol jika panjang data hanyalah 1
# ini karena data hanya ada sendiri maka angka itu yang paling besar di kumpulan angka
# Recursive case
# recursive case akan mengmbalikan angka yang paling besar
# alurnya dengan menyimpan seluruh data di dalam kumpulan
# kemudian membandingkan semuanya sembari keluar dari fungsi