from LinkedList import listNodeToList, listtoListNode
from copy import deepcopy
# O(1) space
def isPalindrome(head):
    rev = None
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = rev
        rev = slow
        slow = temp

    if fast:
        slow = slow.next
    while rev and slow:
        if rev.val != slow.val: return False
        rev = rev.next
        slow = slow.next
    return True

# O(n) space
def isPalindrome2(head):
    def reverseList(root):
        if root is None or root.next is None: return root
        next_node = root.next
        new_head = reverseList(next_node)
        next_node.next = root
        root.next = None
        return new_head

    rev_head = reverseList(deepcopy(head))
    while head and rev_head:
        if head.val != rev_head.val: return False
        head = head.next
        rev_head = rev_head.next
    return True

if __name__ == '__main__':
    head = listtoListNode([1, 2, 3, 3, 2, 1])
    print(listNodeToList(head))
    print(isPalindrome2(head))

    head = listtoListNode([])
    print(listNodeToList(head))
    print(isPalindrome(head))