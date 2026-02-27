#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Latihan 4: Kombinasi Huruf
# ===============================================

def kombinasi(n, hasil=""):
    #base case
    if len(hasil) == n:
        print(hasil)
        return
    # recursive case
    #masuk A
    kombinasi(n, hasil + "A")
    #keluar A dan masuk B
    kombinasi(n, hasil + "B")
    #keluar B

kombinasi(2)

# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
# fungsi rekursi akan mencetak hasil dari ujung rekursif
# pertama fungsi akan mengecek apakah panjang nya sudah tercapai dengan memilih fungsi paling atas ( kombinasi(n, hasil + "A") )
# jika belum, fungsi akan terus me-rekursi hingga panjangnya dicapai dan mencetak hasil : AAAA
# setelah itu, fungsi akan keluar dan masuk kembali ke fungsi ( kombinasi(n, hasil + "B") )
# kemudian mencetak kembali fungsi dengan output: AAAB