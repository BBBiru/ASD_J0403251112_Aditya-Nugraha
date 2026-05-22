#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
# Praktikum 12 - Graph II: Shortest Path
#================================================
#Desc: Latihan 1 Weighted Graph dan Perhitungan Jalur
#================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9.
# 2. Total bobot jalur A -> C -> D adalah 3.
# 3. A -> C -> D karena memiliki total bobot yang lebih kecil (3).
# 4. Karena bobot pada edge bisa jadi lebih besar walaupun jumlah edge lebih sedikit, atau sebaliknya.