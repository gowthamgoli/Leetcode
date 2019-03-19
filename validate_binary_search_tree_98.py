from BinaryTree import listtoTreeNode, prettyPrintTree
def isValidBST(root):
    def isValidBST_helper(root, MIN, MAX):
        if root is None: return True
        if (
            root.val > MIN and root.val < MAX
            and isValidBST_helper(root.left, MIN, root.val)
            and isValidBST_helper(root.right, root.val, MAX)
        ):
            return True
        return False
    
    MIN = float('-inf')
    MAX = float('inf')
    return isValidBST_helper(root, MIN, MAX)

if __name__ == '__main__':
    root = listtoTreeNode([1,0,2])
    print(isValidBST(root))