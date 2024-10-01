class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.left is None:
                current_node.left = Node(data)
                break
            else:
                queue.append(current_node.left)
            
            if current_node.right is None:
                current_node.right = Node(data)
                break
            else:
                queue.append(current_node.right)

    # In-order traversal to display the tree
    def display(self, node):
        if node is None:  
            return
        self.display(node.left)  
        print(node.data, end=" ")  
        self.display(node.right)  
    
    # In-order traversal (alternative)
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    # Pre-order traversal
    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    # Post-order traversal
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
    
    # Breadth-first search (BFS) / Level-order traversal
    def bfsdisplay(self, node):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.data, end=" ")
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

rootElement = int(input("Enter the root: "))
tree = BinaryTree(rootElement)

Nodes = int(input("Enter the number of nodes: "))
for i in range(Nodes):
    tree.insert(int(input("Enter the value: ")))

print("\nIn-order traversal:")
tree.display(tree.root)

print("\nPre-order traversal:")
tree.preorder(tree.root)

print("\nPost-order traversal:")
tree.postorder(tree.root)

print("\nBreadth-first search (Level-order traversal):")
tree.bfsdisplay(tree.root)
