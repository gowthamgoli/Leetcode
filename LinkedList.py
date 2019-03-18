# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listtoListNode(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for num in numbers:
        ptr.next = ListNode(num)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToList(node):
    if not node:
        return []
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
