import random

def quicksort(data):
    quick_convert(data, 0, len(data)-1)

def quick_convert(data, kiri, kanan):
    if kiri < kanan:
        partition_pos = (partition(data,kiri,kanan))
        quick_convert(data,kiri, partition_pos-1)
        quick_convert(data, partition_pos+1, kanan)

def partition(data,kiri,kanan):
    i = kiri
    j = kanan - 1
    pivot = data[kanan]

    while i < j:
        while i < kanan and data[i] < pivot:
            i += 1
        while j > kiri and data[j] >= pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    if data[i] > pivot:
        data[i], data[kanan] = data[kanan], data[i]
    return i

def random_insert(data, banyak):
    total = 0
    while total < banyak:
        x = random.randint(1,100)
        data.append(x)
        total += 1

skor = []
random_insert(skor,10)
print(skor)
quicksort(skor)
print(skor)