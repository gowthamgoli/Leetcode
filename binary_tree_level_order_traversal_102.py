from BinaryTree import listtoTreeNode, prettyPrintTree
def levelOrder(root):
    output = []
    if root is None: return output
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level_size = len(queue)
        nodes_in_level = []
        for _ in range(level_size):
            node = queue.pop(0)
            nodes_in_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(nodes_in_level)
    return output

if __name__ == '__main__':
    l = [3,9,20,None,None,15,7]
    root = listtoTreeNode(l)
    prettyPrintTree(root)
    print(levelOrder(root))
    l = []
    root = listtoTreeNode(l)
    prettyPrintTree(root)
    print(levelOrder(root))
