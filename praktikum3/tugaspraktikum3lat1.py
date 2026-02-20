#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

class Node: #inisiasi class Node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: #inisiasi class LinkedList
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data) #menyimpan data pada node baru
        if not self.head: #mengecek apakah head kosong
            self.head = new_node #jika kosong maka head diisi dengan node baru
            return

        temp = self.head #tempat sementara untuk pindah, awal dari head
        while temp.next: #loop pindah
            temp = temp.next #selama di list berikutnya ada nilai, pindah ke selanjutnya
        temp.next = new_node #jika sudah sampai di akhir, tambahkan node baru

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            print("null")

    def	delete_node(self, key):
        temp = self.head
        if	temp and temp.data == key:
            self.head =	temp.next
            temp = None
            return

        prev = None
        while temp and temp.data !=	key:
            prev = temp
            temp = temp.next

        if	temp is None:
            return

        prev.next = temp.next
        temp = None
        print("Berhasil menghapus", key)

ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(29)
ll.insert_at_end(39)
ll.insert_at_end(10)
ll.display()
ll.delete_node(29)
ll.display()