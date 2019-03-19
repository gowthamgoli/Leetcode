from BinaryTree import TreeNode, listtoTreeNode, prettyPrintTree
def sortedArrayToBST(nums):

    def sortedArrayToBST_helper(nums, low, high):
        if low > high: return None
        if low == high:
            return TreeNode(nums[low])
        mid = (low + high) // 2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST_helper(nums, low, mid-1)
        root.right = sortedArrayToBST_helper(nums, mid+1, high)
        return root

    low = 0 
    high = len(nums) - 1
    root = sortedArrayToBST_helper(nums, low, high)
    return root

if __name__ == '__main__':
    root = sortedArrayToBST([1, 5, 6, 10, 11, 15, 17, 20, 22])
    prettyPrintTree(root)
    root = sortedArrayToBST([])
    prettyPrintTree(root)