from LinkedList import ListNode, listtoListNode, listNodeToList
def addTwoNumbers(l1, l2):
    carry = 0
    ptr_l1 = l1
    ptr_l2 = l2
    dummy_root = ListNode(0)
    ptr_res = dummy_root
    while ptr_l1 and ptr_l2:
        s = ptr_l1.val + ptr_l2.val + carry
        carry = int(s / 10)
        # print(s % 10, carry)
        ptr_res.next = ListNode(s % 10)
        ptr_res = ptr_res.next
        ptr_l1 = ptr_l1.next
        ptr_l2 = ptr_l2.next
    while ptr_l1:
        s = carry + (ptr_l1.val if ptr_l1 else 0)
        carry = int(s / 10)
        ptr_res.next = ListNode(s % 10)
        ptr_res = ptr_res.next
        ptr_l1 = ptr_l1.next
    while ptr_l2:
        s = carry + (ptr_l2.val if ptr_l2 else 0)
        carry = int(s / 10)
        ptr_res.next = ListNode(s % 10)
        ptr_res = ptr_res.next
        ptr_l2 = ptr_l2.next

    if carry:
        ptr_res.next = ListNode(carry)

    return dummy_root.next

def addTwoNumbers2(l1, l2):
    dummy_root = ListNode(0)
    ptr = dummy_root
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        s = l1_val + l2_val + carry
        ptr.next = ListNode(s % 10)
        carry = s // 10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        ptr = ptr.next
    # print(listNodeToList(dummy_root.next))
    return dummy_root.next

if __name__ == '__main__':
    l1 = listtoListNode([2,4,3])
    l2 = listtoListNode([5,6,4])
    res = addTwoNumbers2(l1, l2)
    print(listNodeToList(res))

    l1 = listtoListNode([2,4,9, 9, 9, 9])
    l2 = listtoListNode([5,6,4])
    res = addTwoNumbers2(l1, l2)
    print(listNodeToList(res))

    # l1 = listtoListNode([])
    # l2 = listtoListNode([])
    # res = addTwoNumbers(l1, l2)
    # print(listNodeToList(res))
