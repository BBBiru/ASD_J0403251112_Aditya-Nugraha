#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLingkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List kosong!")
            return
        
        print("Traversing:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("(kembali ke head)")
    
    def search(self, key):
        if not self.head:
            print("List kosong")
            return

        #inisialisasi variable untuk mencari
        key_found = False
        temp = self.head

        #bagian pencarian awal
        if temp.data == key: #cek apakah data = key
            key_found = True #merubah nilai key_found menjadi true
        temp = temp.next #selanjutnya

        #bagian pencarian loop
        while temp != self.head: #selama temp bukanlah head
            if temp.data == key: #cek apakah data = key
                key_found = True #merubah nilai key_found menjadi true
                break
            temp = temp.next #selanjutnya

        if key_found is True: #jika ketemu
            print("Key", key, "ditemukan di dalam CLL")
        else: #jika tidak
            print("Key", key, "tidak ditemukan")

cll = CircularSinglyLingkedList()

#TEST KOSONG
cll.search(15)

cll.insert_at_end(5)
cll.insert_at_end(10)
cll.insert_at_end(15)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()

#TEST
cll.search(5) #mengecek apakah head dibaca
cll.search(15) #mengecek apakah bagian head<node<tail terbaca
cll.search(30) #mengecek apakah tail dibaca
cll.search(35) #mengecek jika tidak ada nilai