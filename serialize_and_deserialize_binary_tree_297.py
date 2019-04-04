from BinaryTree import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            output.append(str(current.val) if current else '#')
            if current is None: continue
            queue.append(current.left)
            queue.append(current.right)
        return ','.join(output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(',')
        queue = [ None if val == '#' else TreeNode(val) for val in queue ]
        n = len(queue)
        front, index = 0, 1
        root = queue[front]
        while front < n and index < n:
            current = queue[front]
            front += 1
            if current is None:
                continue

            if index >= n: return root
            current.left = queue[index]
            index += 1

            if index >= n: return root
            current.right = queue[index]
            index += 1

        return root

if __name__ == "__main__":        
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    root = listtoTreeNode([1,2,3,None,None,4,5])
    prettyPrintTree(root)
    # print(codec.serialize(root))
    root = codec.deserialize(codec.serialize(root))
    prettyPrintTree(root)
