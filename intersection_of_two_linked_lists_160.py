from LinkedList import listNodeToList, listtoListNode

def getIntersectionNode(headA, headB):

    def get_count_nodes(head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    countA = get_count_nodes(headA)
    countB = get_count_nodes(headB)
    if countB > countA:
        countA, countB = countB, countA
        headA, headB = headB, headA
    
    diff = countA - countB
    currA = headA
    currB = headB
    for i in range(diff):
        currA = currA.next
    while currA and currB:
        # print(currA.val, currB.val)
        if currA == currB: 
            # print(currA.val)
            return currA
        currA = currA.next
        currB = currB.next

    return None

if __name__ == '__main__':
    headA = listtoListNode([4,1,8,4,5])
    headB = listtoListNode([5,0,1])
    headB.next.next.next = headA.next.next
    print(listNodeToList(headA))
    print(listNodeToList(headB))
    getIntersectionNode(headA, headB)