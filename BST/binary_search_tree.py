class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = newNode
                    break
                else:
                    temp = temp.left
                    
            else:
                if data > temp.data:
                    if temp.right is None:
                        temp.right = newNode
                        break
                    else:
                        temp = temp.right
                        
                        
                        
                        
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)
        
        
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
        
    def preorder(self, node):
        if node is None:
            return
        print(node.data ,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
tree = BST()
n = int(input("Enter the Number of Nodes: "))
for i in range(n):
    tree.insert(int(input("Enter the Number: ")))
    
tree.inorder(tree.root)
tree.postorder(tree.root)
tree.preorder(tree.root)