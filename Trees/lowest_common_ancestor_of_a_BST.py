#iterative solution
# Neetcode's video https://www.youtube.com/watch?v=gs2LMfuOR9k&t=78s
#note: it is given in the question that p and q will always be present in the BST.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val: # if p and q values are both less than curent node's value, traverse in left subtree
                node = node.left
            elif p.val > node.val and q.val > node.val: # if p and q values are both greater than curent node's value, traverse in right subtree
                node = node.right
            else:
                return node


#recursive solution
# Nick white's video https://www.youtube.com/watch?v=6POfA8fruxI
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)




        return root