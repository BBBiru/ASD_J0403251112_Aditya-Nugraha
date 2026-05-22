#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
# Praktikum 12 - Graph II: Shortest Path
#================================================
#Desc: Latihan 5 Studi Kasus dengan Program Shortest Path
#================================================
import heapq
graph = {
 'Bogor': {'Jakarta': 5, 'Depok': 2},
 'Depok': {'Jakarta': 2, 'Bandung': 6},
 'Jakarta': {'Bandung': 4},
 'Bandung': {}
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

hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for lokasi, jarak in hasil.items():
    print(f"{lokasi} = {jarak} jam")