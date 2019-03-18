class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def listtoTreeNode(tree_list):
    if not tree_list: return
    
    root = TreeNode(tree_list[0])
    queue = [root]
    front = 0
    index = 1
    while True:
        node = queue[front]
        front += 1
        if index >= len(tree_list): return root
        
        left_child = tree_list[index]
        index += 1
        if left_child is not None: 
            node.left = TreeNode(left_child)
            queue.append(node.left)

        if index >= len(tree_list): break

        right_child = tree_list[index]
        index += 1
        if right_child is not None: 
            node.right = TreeNode(right_child)
            queue.append(node.right)

    return root


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

# tree_list = [5,4,7,3,None,2,None,-1,None,None,9]
# root = listtoTreeNode(tree_list)
# prettyPrintTree(root)