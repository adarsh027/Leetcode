#ref: https://leetcode.com/problems/validate-binary-search-tree/solutions/974147/python-js-java-go-c-o-n-by-dfs-and-rule-w-hint/?languageTags=python3
#ref: https://leetcode.com/problems/validate-binary-search-tree/solutions/3249901/python3-simple-solution-uwu/?languageTags=python3
#ref: https://www.youtube.com/watch?v=s6ATEkipzow&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=6

#notes:
# start with root, for it to satisfy BST, root's value should lie between -infinity and +infinity.
# Check for left subtree. the right boundary should be be updated to root's value.
# Check for right subtree, the left boundary should be updated to root's value.
# If both left and right subtrees are valid BST, the given tree is a valid BST.
class Solution:
    
    def isValidBST(self, root):
        
        # Define an inner function that checks whether a binary tree is a valid binary search tree
        def isValid(root, low, high):
            
            if not root:
                return True
            
            # If the value of the root node is not between low and high, return False
            if not (low < root.val < high):
                return False
            
            # Recursively check the left and right sub-trees
            left_subtree = isValid(root.left, low, root.val )
            right_subtree = isValid(root.right, root.val, high)

            return left_subtree and right_subtree # Return True only if both sub-trees are valid binary search trees

        return isValid(root,  float("-inf"), float("inf"))
