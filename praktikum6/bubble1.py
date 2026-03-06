#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

#================================================
# Bubble Sort: Ascending
#================================================

def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1): #for loop pertama, menyesuaikan panjang
        for i in range(passnum): #for loop kedua, membandingkan variable
            if data[i]>data[i+1]: #perbandingan variable
# Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)