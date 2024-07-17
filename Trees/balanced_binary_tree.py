# top-down approach: not efficient, please don't use this as time complexity is O(n^2)
#ref: https://www.techiedelight.com/check-given-binary-tree-is-height-balanced-not/
# Note: The time complexity of this solution is O(n^2) as there are n nodes in the tree, and for every node, we are calculating the height of its left and right subtree that takes O(n) time.
# ref: https://www.youtube.com/watch?v=OgdYyBT8iU8&t=192s
#ref: https://www.youtube.com/watch?v=icxndJkKUuc
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        left_ht= self.height(root.left)
        right_ht= self.height(root.right)
        if abs(left_ht-right_ht)<2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
    def height(self,root):
        if not root:
                return 0
        left_ht= self.height(root.left)
        right_ht= self.height(root.right)
        return 1 +  max(left_ht, right_ht)
    
#bottom-up approach : recomended approach, time complexity is O(n)   
# note: The reason for calling this approach bottom-up is that we keep going into recursive calls until we reach the leftmost node.
# ref: https://www.youtube.com/watch?v=OgdYyBT8iU8&t=192s
# ref: https://www.youtube.com/watch?v=nOcFiGl5Vy4

class Solution:
    def isBalanced(self, root):
        if self.getHeight(root) >= 0: # FYI, this if else portion of code can be replaced by a single statement: return self.getHeight(root) >= 0
            return True
        else:
            return False
    def getHeight(self,node): # here, getHeight() is an instance method
        if node is None:
            return 0
        left_ht= self.getHeight(node.left)
        right_ht = self.getHeight(node.right)
        if left_ht == -1 or right_ht == -1 or abs(left_ht - right_ht) > 1:
            return -1
        return 1 + max(left_ht, right_ht)  
      

# Alternatively, the above code can be written in the following manner where getHeight() is defined as an inner/nested function.
#ref: https://www.freecodecamp.org/news/nested-functions-in-python/
# ref : functions v/s methods article here https://techvidvan.com/tutorials/python-methods-vs-functions/
#ref: https://leetcode.com/problems/balanced-binary-tree/solutions/3191981/convert-sorted-list-to-binary-search-tree-with-step-by-step-explanation/?languageTags=python3
class Solution:
    def isBalanced(self, root):
        def getHeight(node):  # here, getHeight() is an inner/nested function
            if node is None:
                return 0
            left_ht = getHeight(node.left)
            right_ht = getHeight(node.right)
            if left_ht == -1 or right_ht == -1 or abs(left_ht - right_ht) > 1:
                return -1
            return 1 + max(left_ht, right_ht)
        if getHeight(root) >= 0:
            return True
        else:
            return False

#ref: neetcode's solution https://www.youtube.com/watch?v=QfJsau0ItOY    
class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True,0]
            left,right=dfs(root.left),dfs(root.right)
            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]