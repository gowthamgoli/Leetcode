from BinaryTree import *

def constructMaximumBinaryTree(nums):
    def get_max(nums):
        if len(nums) == 0: return None, -1
        num_max, i_max = float("-inf"), -1
        for i, num in enumerate(nums):
            if num > num_max:
                num_max, i_max = num, i
        return num_max, i_max
    
    if len(nums) == 0: return None
    root_val, index = get_max(nums)

    root = TreeNode(root_val)
    root.left = constructMaximumBinaryTree(nums[:index])
    root.right = constructMaximumBinaryTree(nums[index + 1: ])
    return root

if __name__ == "__main__":
    root = constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    prettyPrintTree(root)

