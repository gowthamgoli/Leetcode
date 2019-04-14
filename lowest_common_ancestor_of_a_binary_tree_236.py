from BinaryTree import *

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root, path, node):
        if root is None: return
        path.append(root)
        if root.val == node.val:
            return path
        path_left = dfs(root.left, path, node)
        if path_left: return path_left
        path_right = dfs(root.right, path, node)
        if path_right: return path_right
        path.pop()

    path_p = dfs(root, [], p)
    path_q = dfs(root, [], q)
    n = min(len(path_p), len(path_q)) 
    i = 0
    while i < n and path_p[i].val == path_q[i].val:
        i += 1
    return path_p[i - 1]

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None: return None
    if root.val == p.val or root.val == q.val: return root
    
    lca_left = lowestCommonAncestor(root.left, p, q)
    lca_right = lowestCommonAncestor(root.right, p, q)

    if lca_left and lca_right: return root
    return lca_left if lca_left else lca_right

if __name__ == "__main__":
    root = listtoTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    prettyPrintTree(root)
