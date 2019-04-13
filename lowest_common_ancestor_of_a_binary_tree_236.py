from BinaryTree import *

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root, path, node):
            if root is None: return

            if root.val == node.val:
                return path + [root]
            # path.append(root.val)
            path_left = dfs(root.left, path + [root], node)
            path_right = dfs(root.right, path + [root], node)
            return path_left or path_right

    path_p = dfs(root, [], p)
    path_q = dfs(root, [], q)
    n = min(len(path_p), len(path_q)) 
    i = 0
    while i < n and path_p[i].val == path_q[i].val:
        i += 1
    return path_p[i - 1]

if __name__ == "__main__":
    root = listtoTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    prettyPrintTree(root)
