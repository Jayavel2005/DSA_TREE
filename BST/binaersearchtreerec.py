class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, temp, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        else:
            if data < temp.data:
                if temp.left is None:
                    temp.left = Node(data)
                else:
                    self.insert(temp.left, data)
            else:
                if temp.right is None:
                    temp.right = Node(data)
                else:
                    self.insert(temp.right, data)
        return temp
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
    
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

bst = BST()


n = int(input("How many values do you want to insert into the BST? "))
print("Enter the values:")

for i in range(n):
    value = int(input())
    bst.insert(bst.root, value)


print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)
