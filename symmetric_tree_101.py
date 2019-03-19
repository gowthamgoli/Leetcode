from BinaryTree import listtoTreeNode, prettyPrintTree

def isSymmetric(root):
    def isMirror(left, right):
        if left is None and right is None: return True
        if left is None or right is None: return False

        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

    if root is None: return True
    return isMirror(root.left, root.right)

if __name__ == '__main__':
    root = listtoTreeNode([1])
    prettyPrintTree(root)
    print(isSymmetric(root))