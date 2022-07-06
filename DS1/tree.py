#     1
#    / \
#   2   3
#  / \
# 4   5
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nodes = [1,2,3,4,5]

def createTree(nodes, i):
    if i >= len(nodes):
        return None
    
    root = Node(nodes[i])
    root.left = createTree(nodes, 2 * i + 1)
    root.right = createTree(nodes, 2 * i + 2)
    return root

def preOrderTraversel(root):
    if root == None:
        return
    
    print(root.data)
    preOrderTraversel(root.left)
    preOrderTraversel(root.right)

def postOrderTraversel(root):
    if root == None:
        return
    
    postOrderTraversel(root.left)
    postOrderTraversel(root.right)
    print(root.data)

def inOrderTraversel(root):
    if root == None:
        return
    
    inOrderTraversel(root.left)
    print(root.data)
    inOrderTraversel(root.right)

root = createTree(nodes, 0)
