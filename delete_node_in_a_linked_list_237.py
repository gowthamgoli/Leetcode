from LinkedList import ListNode, listtoListNode, listNodeToList

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

if __name__ == '__main__':
    root = listtoListNode([4,5,1,9])
    print(listNodeToList(root))
    deleteNode(root.next)
    print(listNodeToList(root))

    root = listtoListNode([1,2])
    print(listNodeToList(root))
    deleteNode(root)
    print(listNodeToList(root))