#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
# Praktikum 12 - Graph II: Shortest Path
#================================================
#Desc: Latihan 3 Implementasi Bellman-Ford
#================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}
def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
    # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
    # Jika jarak ke node saat ini sudah diketahui,
    # dan ditemukan jarak yang lebih kecil ke neighbor,
    # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances
hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Pertanyaan Analisis:
# 1. Berapa bobot langsung dari A ke B?
# 2. Berapa total bobot jalur A -> C -> B?
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

# Jawaban Analisis:
# 1. Bobot langsungnya 5
# 2. Bobotnya 2 (AC + CB)
# 3. Jalur A-C-B (2) dibanding dari A-B (5)
# 4. Karena Bellman-Ford memperbarui jalur terpendek secara bertahap
# 5. Memperbarui jarak terpendek dari awal ke sebuah node, jika menemukan jalur yang lebih pendek
# 6. Dijkstra lebih cepat tetapi hanya bisa menggunakan bobot positif, sedangkan Bellman-Ford lebih lambat tetapi bisa menggunakan bobot negatif