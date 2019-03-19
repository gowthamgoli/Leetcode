from BinaryTree import listtoTreeNode, prettyPrintTree

def isSymmetric(root):
    def isMirror(left, right):
        if left is None and right is None: return True
        if left is None or right is None: return False

        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

    if root is None: return True
    return isMirror(root.left, root.right)

def isSymmetric2(root):
    if root is None: return True
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        if left is None and right is None: continue
        if left is None or right is None: return False
        if left.val != right.val: return False
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    return True

if __name__ == '__main__':
    root = listtoTreeNode([1,2,2,None,4,4,None])
    prettyPrintTree(root)
    print(isSymmetric2(root))