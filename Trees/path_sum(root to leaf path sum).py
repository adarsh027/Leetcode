#ref: https://leetcode.com/problems/path-sum/solutions/534122/python-bfs-dfs-recursive-dfs-iterative-solution/?page=2&languageTags=python3
#ref: https://www.youtube.com/watch?v=Hg82DzMemMI
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
             return False
                
        elif not root.left and not root.right and targetSum - root.val == 0: #this means we are at a leaf node
            return True
        
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
        
#ref: https://www.youtube.com/watch?v=LSKQyOz_P8I

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr_sum = 0
        def pathSum(node, curr_sum):
            if not node:
                 return False
             
            curr_sum += node.val
            
            if not node.left and not node.right and curr_sum == targetSum: #this means we are at a leaf node
                return True
            
            return pathSum(node.left, curr_sum) or pathSum(node.right, curr_sum)
        return pathSum(root, curr_sum)