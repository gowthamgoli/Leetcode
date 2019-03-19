from BinaryTree import prettyPrintTree, listtoTreeNode
def maxDepth(root):
    if root is None: return 0

    depth = 1 + max(maxDepth(root.left), maxDepth(root.right))
    return depth

if __name__ == '__main__':
    root = listtoTreeNode([3,9,20,None,None,15,7])
    prettyPrintTree(root)
    print(maxDepth(root))
