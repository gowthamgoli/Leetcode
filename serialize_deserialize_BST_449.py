from BinaryTree import TreeNode, listtoTreeNode, prettyPrintTree

def serialize_bfs(root):
    queue = []
    serialize = []
    if root is None: return ''
    queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        serialize.append('#' if curr is None else str(curr.val))
        if curr : 
            queue.append(curr.left)
            queue.append(curr.right)
    return ','.join(serialize)

def deserialize_bfs(data):
    if data == '': return None
    data = data.split(',')
    queue = [None if num == '#' else TreeNode(int(num)) for num in data]
    front = 0
    index = 1
    root = queue[front]
    while index < len(queue) and front < len(queue):
        curr = queue[front]
        front += 1
        if curr is None: continue

        if index >= len(queue): return root
        curr.left = queue[index]
        index += 1
        if index >= len(queue): return root
        
        curr.right = queue[index]
        index += 1

    return root
    
if __name__ == '__main__':
    tree = []
    root = listtoTreeNode(tree)
    prettyPrintTree(root)
    serialized = serialize_bfs(root)
    # print(root)
    root = deserialize_bfs(serialized)
    prettyPrintTree(root)