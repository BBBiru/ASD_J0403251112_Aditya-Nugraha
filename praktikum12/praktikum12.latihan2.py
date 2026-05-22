#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
# Praktikum 12 - Graph II: Shortest Path
#================================================
#Desc: Latihan 2 Implementasi Dijkstra
#================================================
import heapq
# Weighted graph dengan bobot positif
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
    # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
    # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
    # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
    # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Pertanyaan Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# 2. Berapa jarak terpendek dari A ke C?
# 3. Berapa jarak terpendek dari A ke D?
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4
# 2. Jarak terpendek dari A ke C adalah 2
# 3. Jarak terpendek dari A ke D adalah 3
# 4. Karena total bobot dari A-C-D memiliki bobot yang lebih kecil daripada A-B-D (2 + 1 < 4 + 5)
# 5. Digunakan untuk selalu mengambil node dengan jarak terpendek saat ini
# 6. Karena algoritma ini mengasumsikan bahwa semua bobot bernilai positif. Jika diberi nilai negatif, algoritma akan memberikan nilai yang tidak akurat atau bahkan infinite loop