#Aditya Nugraha
#J0403251112

print("Nama : Aditya Nugraha")
print("NIM  : J0403251112")
print("---" * 10)
varData = [12, 42, 32, 32, 2, 22, 42, 47]
print("Root :", varData[0])
print("Variasi Data :", varData[1:])
print("---" * 10)

#----------------------------------------------------------
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
#----------------------------------------------------------
class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Insert data
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    # Inorder Traversal (Kiri, Root, Kanan)
    def inorderTraversal(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    # Preorder Traversal (Root, Kiri, Kanan )
    def preorderTraversal(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    # Postorder Traversal (Kiri, Kanan, Root)
    def postorderTraversal(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')
#----------------------------------------------------------

tree_data = BinarySearchTree()
for data in varData:
    tree_data.insert(data)

print("Inorder Traversal:", end=' ')
tree_data.inorderTraversal()

print("Preorder Traversal:", end=' ')
tree_data.preorderTraversal()

print("Postorder Traversal:", end=' ')
tree_data.postorderTraversal()