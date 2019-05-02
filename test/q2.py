from BinarySearchTreeMap import BinarySearchTreeMap

def listtoTreeNode(tree_list):
    if not tree_list: return
    
    root = LinkedBinaryTree.Node(tree_list[0])
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
            node.left = LinkedBinaryTree.Node(left_child)
            node.left.parent = node
            queue.append(node.left)

        if index >= len(tree_list): break

        right_child = tree_list[index]
        index += 1
        if right_child is not None: 
            node.right = LinkedBinaryTree.Node(right_child)
            node.right.parent = node
            queue.append(node.right)

    return root

def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.item.key))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

def create_chain_bst(n):
    bst_map = BinarySearchTreeMap()
    for i in range(1, n + 1):
        bst_map.insert(i)
    return bst_map
    prettyPrintTree(bst_map.root)

def create_complete_bst(n):
    def add_items(low, high):
        if low > high:
            return

        mid = (low + high) // 2
        item = BinarySearchTreeMap.Item(mid, None)
        new_node = BinarySearchTreeMap.Node(item)
        root = new_node
        root.left = add_items(low, mid - 1)
        root.right = add_items(mid + 1, high)
        return root

    bst = BinarySearchTreeMap()
    root = add_items(1, n)
    bst.root = root
    return bst

def create_complete_bst2(n):
    def add_items(bst, low, high):
        if low > high:
            return
        
        mid = (low + high) // 2
        item = BinarySearchTreeMap.Item(mid, None)
        new_node = BinarySearchTreeMap.Node(item)
        bst.root = new_node

        bst_left = BinarySearchTreeMap()
        add_items(bst_left, low, mid - 1)
       
        bst_right = BinarySearchTreeMap()
        add_items(bst_right, mid + 1, high)

        bst.root.left = bst_left.root
        if bst_left.root: bst_left.root.parent = bst.root
        # bst.root.left.parent = bst_left.root
        bst.root.right = bst_right.root
        if bst_right.root: bst_right.root.parent = bst.root
        # bst.root.right.parent = bst_right.root

    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def restore_bst(prefix_list):
    # index = 0
    def restore_bst_helper(prefix_list, index, min_val, max_val):
        if index >= len(prefix_list):
            return None, len(prefix_list) - 1

        if not ( min_val <= prefix_list[index] <= max_val ):
            return None, index - 1

        # print(index, min_val, max_val)
        item = BinarySearchTreeMap.Item(prefix_list[index], None)
        root = BinarySearchTreeMap.Node(item)
        # index = index + 1

        root.left, left_index = restore_bst_helper(prefix_list, index + 1, min_val, prefix_list[index])
        if root.left: root.left.parent = root
        root.right, right_index = restore_bst_helper(prefix_list, left_index + 1, prefix_list[index], max_val)
        if root.right: root.right.parent = root

        return root, right_index

    bst = BinarySearchTreeMap()
    bst.root, index = restore_bst_helper(prefix_list, 0, float("-inf"), float("inf"))
    
    return bst

def min_abs_difference(bst):
    inorder = []
    for node in bst.inorder():
        inorder.append(node.item.key)
    print(inorder)
    print(list(zip(inorder, inorder[1:])))
# bst = create_chain_bst(10)
# prettyPrintTree(bst.root)
# bst = create_complete_bst2(15)
# prettyPrintTree(bst.root)
bst = restore_bst([10, 5, 1, 7, 40, 50])
prettyPrintTree(bst.root)
# bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
# prettyPrintTree(bst.root)
min_abs_difference(bst)