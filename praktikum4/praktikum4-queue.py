#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

#================================================
#Membuat queue
#================================================

#inisialisasi class node
class node:
    def __init__(self, data): #inisialisasi fungsi __init__
        self.data = data #menambah variable data ke object
        self.next = None #menambah variable next ke object

class queue: #inisialisasi queue
    def __init__(self):
        self.front = None #node depan
        self.rear = None #node belakang
    
    def is_empty(self): #cek queue kosong
        return self.front is None

    def enqueue(self, data): #enqueue
        new_node = node(data) #node baru mengambil class node
        if self.is_empty(): #mengecek jika kosong
            self.front = new_node #depan dan belakang menjadi satu node
            self.rear = new_node
            return
        self.rear.next = new_node #next dari belakang menjadi node baru
        self.rear = new_node #node baru menjadi belakang

    def display(self): #display
        temp = self.front #membuat temporary
        while temp is not None: #jika temporary tidak kosong
            print(temp.data, end=" --> ") #menampilkan data dari temp
            temp = temp.next #melanjutkan temp ke link berikutnya
        print("None")
    
    def dequeue(self): #dequeue
        if self.is_empty(): #mengecek jika kosong
            print("queue kosong")
            return
        temp = self.front #temp menjadi front
        print(temp.data) #mencetak temp
        self.front = temp.next #lanjutan temp menjadi front
        del temp #menghapus temp
        if self.front is None: #jika depan kosong, maka belakang juga kosog. membersihkan queue
            self.rear = None

queuesatu = queue()
queuesatu.enqueue(1)
queuesatu.enqueue(2)
queuesatu.enqueue(3)
queuesatu.display()
print("Mencoba dequeue")
queuesatu.dequeue()
queuesatu.display()
print("Mencoba dequeue hingga habis")
queuesatu.dequeue()
queuesatu.dequeue()
queuesatu.dequeue()