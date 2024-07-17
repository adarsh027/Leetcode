class BT:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Function to insert in BST
    def insert(self, data):
        
        if self.data is None:
            self.data = data
            return
        if self.data==data:
            return

        if data and data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = BT(data)     
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = BT(data)

    def levelOrder(self, root):
        from collections import deque
        if not root: 
            return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.leftChild: 
                    queue.append(node.leftChild)
                if node.rightChild: 
                    queue.append(node.rightChild)
            result.append(level)
        return result
    
    def printTree(self): # in order traversal
        if self.leftChild:
            self.leftChild.printTree()
        print( self.data),
        if self.rightChild:
            self.rightChild.printTree()

# creating root node and inserting values in a binary
# for the below insertion, you can visualize the tree by referring to the figure given here: https://www.askpython.com/python/examples/delete-a-binary-tree
root = BT(15)
root.insert(10)
root.insert(25)
root.insert(6)
root.insert(14)
root.insert(20)
root.insert(60)

root.printTree()
root.levelOrder(root)


#ref: https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/3293559/unprecedented-logic-python3/
#ref: https://www.youtube.com/watch?v=6ZnyEApgFYg
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res




