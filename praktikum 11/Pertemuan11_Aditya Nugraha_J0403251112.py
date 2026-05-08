#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================
#Pertemuan 11
#Desc: Membuat jaringan sosial media dalam graph
#================================================

#================================================
#Orang sebagai vertex/node
#Hubungan follow sebagai edge
#Edge akan berarah karena hubungan follow 
#bersifat satu arah
#================================================

#================================================
#Adjacency List Berarah
#================================================

def createGraphList(names, edges):
    #fungsi mengambil list nama orang dan list hubungan follow

    graph_list_berarah = dict() 
    #baris diatas akan membuat dictionary kosong

    for u in names:
        graph_list_berarah[u] = []
    #baris diatas akan membuat key berdasarkan nama dan value berupa list kosong

    for u, v in edges:
        graph_list_berarah[names[u]].append(names[v])
    #baris diatas akan menambahkan nama v ke dalam list nama u

    return graph_list_berarah

#================================================
#Adjacency Matrix Berarah
#================================================

def createGraphMatrix(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    #Baris diatas akan membuat matriks dengan dimensi V x V yang diisi dengan nilai 0

    for u, v in edges:
        mat[u][v] = 1
        #Baris diatas akan membuat nilai 1 pada posisi (u,v)
    return mat


#================================================
#Uji Coba
#================================================
if __name__ == "__main__":
    Index_Nama = ["Adit", "Azmi", "Dimas", "Rizky", "Fajar", "Naufal"]
    #Nama dummy untuk uji coba sebagai vertex

    V = len(Index_Nama)
    #V menjadi banyaknya vertex

    Followed = [[0,1],[0,2],[1,2],[2,0],[3,4],[4,5],[5,3],[0,3],[1,4],[2,5],[3,5]]
    #Followed adalah hubungan antar nama dalam bentuk list. Disini akan menjadi edge
    #Disini nama akan diwakilkan oleh index
    #List akan menunjukan hubungan follow dalam bentuk berikut
    #[index User, index Orang yang difollow]
    #Contoh [0,1] berarti Adit mengikuti Azmi

    mat = createGraphMatrix(V,Followed)
    #menyimpan matriks. mengirimkan banyak vertex dan list hubungan follow
    graph_list = createGraphList(Index_Nama, Followed)
    #menyimpan list. mengirimkan list nama dan list hubungan follow

    #Dibawah ini adalah hasil representasi dari graph
    print("\nAdjacency List Representation:")
    for name in Index_Nama:
        print(f"{name} Followed: {graph_list[name]}")

    print("Adjacency Matrix Representation:")
    for i in range(V):
        print(f"{Index_Nama[i]} :", end=" ")
        for j in range(V):
            print(mat[i][j], end=" ")
        print()
    
    print("Nama node:")
    i = 1
    for name in Index_Nama:
        print(f"{i}. {name}")
        i+=1
    
    print("Hubungan antar node:")
    i = 1
    for x in Followed:
        print(f"{i}. {Index_Nama[x[0]]} --> {Index_Nama[x[1]]}")
        i+=1
#================================================
