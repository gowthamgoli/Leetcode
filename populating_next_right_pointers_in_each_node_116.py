from BinaryTree import prettyPrintTree, listtoTreeNode

def connect(root):
    levels = []
    if root is None: return None
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level = []
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            level.append(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        levels.append(level)

    for i in range(len(levels)):
        for j in range(0, len(levels[i]) - 1):
            levels[i][j].next = levels[i][j+1]

    return levels

def connect2(root):
    if root is None: return None
    
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

    connect2(root.left)
    connect2(root.right)
    return root

if __name__ == '__main__':
    root = listtoTreeNode([1,2,3,4,None,None,5])
    prettyPrintTree(root)
    print(connect(root))