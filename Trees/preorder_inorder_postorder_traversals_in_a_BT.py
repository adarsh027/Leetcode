#recursive
#ref: https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line/?languageTags=python3
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
                return []
        return [root.val]  + self.preorderTraversal(root.left) +  self.preorderTraversal(root.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
                return []
        return self.inorderTraversal(root.left) + [root.val]  + self.inorderTraversal(root.right)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
                return []
        return  self.postorderTraversal(root.left) +  self.postorderTraversal(root.right) + [root.val]
    
#iterative
#ref: Comments of https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/713539/python-3-all-iterative-traversals-inorder-preorder-postorder-similar-solutions/?languageTags=python3
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        
        while stack: 
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    
#ref :https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/3187656/91-35-binary-tree-inorder-traversal-with-step-by-step-explanation/?page=2&languageTags=python3
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while stack or node: # As the stack is initially empty, we have include the node in the OR condition. It also takes care of the scenario when root is None.
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        
        return res
 
#ref: https://www.youtube.com/watch?v=QhszUQhGGlA
#ref: https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/713539/python-3-all-iterative-traversals-inorder-preorder-postorder-similar-solutions/?languageTags=python3
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()  
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res