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

    def add_list(self, listlain):
        temp1 = self.head
        temp2 = listlain.head
        while temp1.next:
            temp1 = temp1.next
        while temp2:
            temp1.next = temp2
            temp1 = temp1.next
            temp2 = temp2.next

ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(19)
ll.insert_at_end(2)
ll.display()

print("TEST KOSONG")
ll3 = LinkedList()
ll3.display()

ll.add_list(ll3)
ll.display()

print("TEST")
#TEST
ll2 = LinkedList()
ll2.insert_at_end(1)
ll2.insert_at_end(2)
ll2.insert_at_end(3)
ll2.insert_at_end(4)
ll2.display()

ll.add_list(ll2)
ll.display()