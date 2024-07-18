# Note: As per given definition in the problem,
# Diameter = No. of edges between longest path between any two nodes
#  We know that the diameter may or may not pass through the root node. Since it
#  does pass though a node,we can express it in terms of height of its left subtree and right subtree.
         
# Thus, considering height is calculated based upon the no. of nodes based definition instead of no. of edges based definition, we have the following relation
# between diameter and heights of left and right subtree
 
# Diameter of tree passing through a node(may or may not be a root node) 
#                     = left subtree height + right subtree height
#                     = No. of edges between longest path between the leaf nodes of left and right subtree


# Thus, for each node in the binary tree, 
# we calculate the length of the longest length going through the node. Then, the diamter of the binary tree will be the maximum
# of all such lengths computed for all the nodes in the tree.


#ref: https://leetcode.com/problems/diameter-of-binary-tree/solutions/574778/python3-dfs-bottom-up-to-calculate-the-height-of-the-node/?languageTags=python3
class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0 # variable to store the maximum diameter found so far
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        # base case:
        if not node:
            return 0
		# recursive cases
        left_ht = self.dfs(node.left)
        right_ht = self.dfs(node.right)
        possible_res = left_ht + right_ht # computing longest path passing through a node. This could be a our possible result, ie, diameter of the tree.
        self.res = max(self.res,possible_res )
        return 1 + max(left_ht,right_ht)
 
 
#using nested helper method dfs()
# ref: https://leetcode.com/problems/diameter-of-binary-tree/solutions/3294669/543-space-97-96-solution-with-step-by-step-explanation/?languageTags=python3   
class Solution:
    def diameterOfBinaryTree(self, root):
        self.res  = 0  # variable to store the maximum diameter found so far 
        def dfs(node):
            if not node:
                return 0
            left_ht = dfs(node.left)
            right_ht = dfs(node.right)
            possible_res = left_ht + right_ht # computing longest path passing through a node. This could be a our possible result, ie, diameter of the tree.
            self.res = max(self.res, possible_res) 
            return 1 + max(left_ht, right_ht)
            
        dfs(root)
        return self.res
    
# using nonlocal keyword
#ref: https://leetcode.com/problems/diameter-of-binary-tree/solutions/2222455/recursive-dfs-solution-in-python-with-detailed-comments-explanation/?languageTags=python3   
class Solution:
    def diameterOfBinaryTree(self, root):
        res  = 0  
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_ht = dfs(node.left)
            right_ht = dfs(node.right)
            possible_res = left_ht + right_ht # computing longest path passing through a node. This could be a our possible result, ie, diameter of the tree.
            res = max(res, possible_res) 
            return 1 + max(left, right)
            
        dfs(root)
        return res
