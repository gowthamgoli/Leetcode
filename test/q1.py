from LinkedBinaryTree import LinkedBinaryTree

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

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.data))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

def min_max(root):
    if root is None:
        return (float("inf"), float("-inf"))

    min_l, max_l = min_max(root.left)
    min_r, max_r = min_max(root.right)
    min_tree = min(min_l, min_r, root.data)
    max_tree = max(max_l, max_r, root.data)
    return (min_tree, max_tree)

def leaves_list(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        yield root.data

    yield from leaves_list(root.left)
    yield from leaves_list(root.right)

def is_height_balanced(root):

    def is_height_balanced_helper(root):
        if root is None:
            return (True, 0)

        is_balaned_left, left_height =  is_height_balanced_helper(root.left)
        is_balanced_right, right_height = is_height_balanced_helper(root.right)

        tree_height = max(left_height, right_height) + 1
        tree_balanced = is_balaned_left and is_balanced_right and abs(left_height - right_height) <= 1

        return (tree_balanced, tree_height)

    is_balanced, height = is_height_balanced_helper(root)
    return is_balanced

def create_expression_tree(prefix_exp_str):
    
    def create_expression_tree_helper(root, expr, index):
        if expr[index].isdigit():
            return LinkedBinaryTree.Node(expr[index]), index
        
        root = LinkedBinaryTree.Node(expr[index])
        l, l_index = create_expression_tree_helper(expr, index + 1)
        r, r_index = create_expression_tree_helper(expr, l + 1)
        root.left = l
        root.right = r
        return root, r_index

    root = None
    expr = prefix_exp_str.split()
    create_expression_tree_helper(root, expr, 0)

tree = [3, 2, 7, 9, None, 8, 4, 5, 1]
root = listtoTreeNode(tree)
prettyPrintTree(root)
bin_tree = LinkedBinaryTree(root=root)
print(min_max(bin_tree.root))

x = bin_tree.leaves_list()
print(list(x))

tree = [3, 2, 7, 9, None, 8, 4, 5, None, 5, 1]
root = listtoTreeNode(tree)
prettyPrintTree(root)
bin_tree = LinkedBinaryTree(root=root)
print(is_height_balanced(bin_tree.root))

prefix_exp_str = "* 2 + - 15 6 4"
create_expression_tree(prefix_exp_str)
