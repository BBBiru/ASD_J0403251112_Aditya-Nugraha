#================================================
#Nama: Aditya Nugraha
#NIM: J0403251112
#Kelas: TPL 62 A1
#================================================

#================================================
#Membuat stack
#================================================

#inisialisasi class node
class node:
    def __init__(self, data): #inisialisasi fungsi __init__
        self.data = data #menambah variable data ke object
        self.next = None #menambah variable next ke object

class stack: #inisialisasi stack
    def __init__(self):
        self.head = None

    def is_empty(self): #cek stack kosong
        return self.head is None

    def push(self, data): #node baru
        new_node = node(data) #class node baru = node
        new_node.next = self.head #menyimpan link node berikutnya
        self.head = new_node #mengubah head menjadi node baru

    def display(self): #menampilkan stack
        temp = self.head #membuat temporary variable dengan value head
        while temp: #looping traversing
            print(temp.data, end=" --> ")
            temp = temp.next #melanjutkan ke node berikutnya
        print("None") #akhir

    def peek(self):
        if self.is_empty():
            print("Stack kosong")
            return None
        print(self.head.data, end=" ")
        print("<-- Stack head")

    def pop(self): #mengambil data teratas
        if self.is_empty(): #mengecek jika stack kosong
            print("Stack kosong")
            return None
        temp = self.head #membuat temporary variable dengan value head
        print(temp.data) #mencetak data dari temp
        self.head = temp.next #membuat node berikutnya menjadi head
        del temp #menghapus node

#inisialisasi node

stack_baru = stack()
stack_baru.push("A")
stack_baru.push("B")
stack_baru.push("C")
stack_baru.push("D")
stack_baru.push("E")
stack_baru.push("F")
stack_baru.display()
print("Mencoba pop")
stack_baru.pop()
print("Mencoba display")
stack_baru.display()
print("Mencoba push")
stack_baru.push("Sigma")
print("Mencoba display")
stack_baru.display()
print("Mencoba pop")
stack_baru.pop()
stack_baru.pop()
stack_baru.pop()
print("Mencoba display")
stack_baru.display()

stack_beda = stack()
stack_beda.pop()

stack_beda.peek()
stack_baru.peek()