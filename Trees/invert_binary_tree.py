#ref: https://www.youtube.com/watch?v=ijL0h6-1qbQ
#ref: https://www.youtube.com/watch?v=OnSn2XEQ4MY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=5
#ref: https://leetcode.com/problems/invert-binary-tree/solutions/1724494/python-3-30ms-recursive-4-line-node-swap-easy-to-understand/?page=2&languageTags=python3
class Solution:
    def invertTree(self, root):
        if not root: # same as if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    