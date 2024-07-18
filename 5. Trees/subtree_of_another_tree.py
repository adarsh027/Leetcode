#ref: https://leetcode.com/problems/subtree-of-another-tree/solutions/3298882/572-solution-with-step-by-step-explanation/?languageTags=python3
#ref: https://leetcode.com/problems/subtree-of-another-tree/solutions/2932015/beats-95-codedominar-solution/
#ref: https://www.youtube.com/watch?v=E36O5SWp-LE
class Solution:
    def isSubtree(self, root, subRoot):
       def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            # If both values match continue to check if children also match
            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
       
       if not root:
            return False
       if not subRoot: 
            return True
        # If any of the node values in root match with subtree, we check for same tree
       if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        # Recurse in root's left and right subtree. Using "OR" since only need one match
       return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)