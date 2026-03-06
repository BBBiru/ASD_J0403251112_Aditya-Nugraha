#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

#================================================
# Latihan Sorting
#================================================

def bubble(data):
    data_temp = data.copy()
    for passnum in range(len(data_temp)-1,0,-1):
        for i in range(passnum):
            if data_temp[i]<data_temp[i+1]:
                temp = data_temp[i]
                data_temp[i] = data_temp[i+1]
                data_temp[i+1] = temp
    return data_temp

def top_5(data):
    terbesar = bubble(data)
    print(terbesar)
    for top in range(0,5):
        for i in range(0,len(kandidat)):
            if terbesar[top] == kandidat[i]:
                print(f"Pemenang ke-{top+1}, kandidat ke-{i+1} dengan skor: {terbesar[top]}")

kandidat = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
top_5(kandidat)
# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
# 2. Kandidat berapa saja yang lolos?