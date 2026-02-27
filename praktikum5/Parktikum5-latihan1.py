#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

# ===============================================
# Latihan 1: Rekursi Pangkat
# ===============================================
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    # Rekursi dengan variabel a dan n-1 untuk mencegah infinite recursion
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# Diskusi dan jelaskan alur program serta base case dan recursive call.
# Jawab: Alur program dimulai dengan mengecek apakah variabel n == 0
# jika variabel n == 0, fungsi akan mengembalikan 1
# jika variabel n != 0, fungsi akan mengembalikan a(bilangan yang akan dipangkatkan) dikali hasil funsi pangkat
# disini rekursi terjadi
# jika n == 4, fungsi rekursi akan dipanggil sebanyak 5 kali termasuk pemanggilan awal (print(pangkat(2,4)))
# jadi alur contoh diatas akan seperti berikut:
# 2 * 2 * 2 * 2 * 1
# (di ujung 1 karena n == 0)
