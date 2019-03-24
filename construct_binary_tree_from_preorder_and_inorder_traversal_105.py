from BinaryTree import listtoTreeNode, TreeNode, prettyPrintTree

def buildTree(preorder, inorder):

    if not inorder: return None 
    if not preorder: return None 

    node = preorder[0]
    ind_root_in = inorder.index(node)
    len_left_tree = ind_root_in
    root_node = TreeNode(node)
    root_node.left = buildTree(preorder[1:len_left_tree+1], inorder[0:len_left_tree] )
    root_node.right = buildTree(preorder[len_left_tree+1:], inorder[ind_root_in + 1:])

    return root_node    

if __name__ == '__main__':
    root = buildTree([3,9,20,15,7], [9,3,15,20,7])
    prettyPrintTree(root)