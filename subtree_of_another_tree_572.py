from BinaryTree import *

def isSubtree(s, t):

    def compare(s, t):
        if s is None and t is None: return True
        if s is None or t is None: return False
        # if s and t and s.val == t.val:
        return s.val == t.val and compare(s.left, t.left) and compare(s.right, t.right)
        # return False 


    if t is None: return True
    if s is None: return False

    if compare(s, t): return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)
if __name__ == "__main__":
    # s = listtoTreeNode([3, 4, 5, 1, 2])
    # t = listtoTreeNode([4, 1, 2])
    # prettyPrintTree(s)
    # prettyPrintTree(t)
    # print(isSubtree(s, t))

    s = listtoTreeNode([1])
    t = listtoTreeNode([0])
    prettyPrintTree(s)
    prettyPrintTree(t)
    print(isSubtree(s, t))
