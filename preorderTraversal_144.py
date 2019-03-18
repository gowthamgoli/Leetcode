from BinaryTree import TreeNode, listtoTreeNode, prettyPrintTree

def preorderTraversal(root):
    preorder = []
    stack = []
    if root is None: return preorder
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        preorder.append(curr.val)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return preorder

if __name__ == '__main__':
    tree = [5, 4, 7, 3, 6, None, 2, None, -1, 2, None, None,  9]
    root = listtoTreeNode(tree)
    prettyPrintTree(root)
    preorder = preorderTraversal(root)
    print(preorder)