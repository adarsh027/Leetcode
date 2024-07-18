#ref: https://www.youtube.com/watch?v=cOjLyASDJcc
#ref: https://www.youtube.com/watch?v=_-QHfMDde90
#ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/875568/python-commented-and-explained/?languageTags=python3
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


       # I have reached a dead end, I didn't find anything here
        if not root:
            return None
        
        # I see one of the targets! I will inform my caller!
        if root == p or root == q: 
            return root
        
        # Recursively look for p or q in left subtree, if found, return the found target.
        foundInLeft = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively look for p or q in right subtree, if found, return the found target.
        foundInRight = self.lowestCommonAncestor(root.right, p, q)
        
        # Didnt find anything in the left, must be in right
        if not foundInLeft: 
            return foundInRight
        
        # Didnt find anything in the right, must be in the left
        elif not foundInRight: 
            return foundInLeft
        
        # Found something in both left and right subtree of some node. Such a node is is the required LCA  and we return it.
        else:
            return root