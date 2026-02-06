#######################################################################
#Aditya Nugraha
#J0403251112
#######################################################################
jumlah_baris = 0
print("---Membuka File---")
with open("data_mahasiswa.txt", "r", encoding = "UTF-8") as file : #membuka dan membaca file .txt
    for baris in file:
        jumlah_baris +=1
        baris = baris.strip() #menghilangkan spasi atau \n
        print("Jumlah baris =", jumlah_baris)
        print(baris)

#parsing menjadi data terpisah
with open("data_mahasiswa.txt", "r", encoding = "UTF-8") as file :
    for baris in file:
        baris = baris.strip() #menghilangkan spasi atau \n
        nim, nama, nilai = baris.split(",") #memasukan baris yang di split ke dalam 3 variabel beda
        print("NIM:", nim, "Nama:", nama, "Nilai:", nilai)

#memasukan ke dalam list
data_list = []
with open("data_mahasiswa.txt", "r", encoding = "UTF-8") as file :
    for baris in file:
        baris = baris.strip() #menghilangkan spasi atau \n
        nim, nama, nilai = baris.split(",") #memasukan baris yang di split ke dalam 3 variabel beda
        data_list.append([nim, nama, nilai])

print(data_list)
print("record ke-1", data_list[0])
print("jumlah record:", len(data_list))

data_dict = {}
with open("data_mahasiswa.txt", "r", encoding = "UTF-8") as file :
    for baris in file:
        baris = baris.strip() #menghilangkan spasi atau \n
        nim, nama, nilai = baris.split(",") #memasukan baris yang di split ke dalam 3 variabel beda
        data_dict[nim] = { #memasukan dictionary nama dan nilai ke dictionary data_dict
            "Nama" : nama,
            "Nilai" : int(nilai)
        }
print(data_dict)