from BinaryTree import TreeNode, listtoTreeNode, prettyPrintTree

def inorderTraversal(root):
    inorder = []
    stack = []
    curr = root
    while len(stack) > 0 or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        inorder.append(node.val)
        curr = node.right
    return inorder

if __name__ == '__main__':
    tree = [5, 4, 7, 3, None, 2, None, -1, None,  9]
    root = listtoTreeNode(tree)
    prettyPrintTree(root)
    inorder = inorderTraversal(root)
    print(inorder)