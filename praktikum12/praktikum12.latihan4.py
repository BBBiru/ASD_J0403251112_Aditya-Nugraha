#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
# Praktikum 12 - Graph II: Shortest Path
#================================================
#Desc: Latihan 4 Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
#================================================
import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
 'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
 'Perpustakaan': {'Lab': 3},
 'Kantin': {'Lab': 4, 'Aula': 7},
 'Lab': {'Aula': 1},
 'Aula': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Pertanyaan Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban Analisis:
# 1. Kantin (2 menit), dari Gerbang ke Kantin (tidak melewati node lain)
# 2. Tujuh menit, dari Gerbang ke Kantin ke Lab ke Aula
# 3. Tidak, karena jarak tidak ditentukan melalui hubungan langsung, tetapi dengan bobot nilai edge
# 4. Selain kasus ini tidak memiliki bobot negatif, algoritma Dijkstra lebih cepat dari Bellman-Ford