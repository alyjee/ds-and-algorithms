from collections import deque

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

root = createTree(nodes, 0)

def getLevelsByIterativeBFS(root):
    if root == None:
        return 0
    
    level = 0
    
    q = deque([root])
    
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    
    return level
print(getLevelsByIterativeBFS(root))