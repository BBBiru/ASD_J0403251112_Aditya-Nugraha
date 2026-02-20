#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

#================================================
#Membuat linked list
#================================================

#inisialisasi class node
class node:
    def __init__(self, data): #inisialisasi fungsi __init__
        self.data = data #menambah variable data ke object
        self.next = None #menambah variable next ke object

#inisialisasi node
A = node("Aku")
B = node("Suka")
C = node("Mandi")

#menghubungkan node
A.next = B #membuat node selanjutnya dari A adalah B (A --> B)
B.next = C #membuat node selanjutnya dari B adalah C (B --> C)
head = A

#traversing node
current = head
while current is not None:
    print(current.data)
    current = current.next

