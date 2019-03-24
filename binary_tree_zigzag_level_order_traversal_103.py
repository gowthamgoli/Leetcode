from BinaryTree import prettyPrintTree, listtoTreeNode

def zigzagLevelOrder(root):
    levels = []
    if root is None: return levels
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level = []
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        levels.append(level)

    for i, _ in enumerate(levels):
        if i % 2 == 1:
            levels[i] = levels[i][::-1]
    return levels

if __name__ == '__main__':
    # root = listtoTreeNode([3,9,20,4,6,15,7])
    # prettyPrintTree(root)
    # print(zigzagLevelOrder(root))
    root = listtoTreeNode([1,2,3,4,None,None,5])
    prettyPrintTree(root)
    print(zigzagLevelOrder(root))