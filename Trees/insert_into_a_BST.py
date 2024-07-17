#ref: https://leetcode.com/problems/insert-into-a-binary-search-tree/solutions/3328536/701-solution-with-step-by-step-explanation/?languageTags=python3
#recursive solution
class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    # if the root is null, create a new node with the given val and return it as the new root of the BST
    if not root: # this is same as--> "if root is None:"
        return TreeNode(val)
    
    
    if  val < root.val:
        root.left = self.insertIntoBST(root.left, val)
        
    else:
        root.right = self.insertIntoBST(root.right, val)
    
    # return the root of the BST after the insertion
    return root

#ref: https://leetcode.com/problems/insert-into-a-binary-search-tree/solutions/3031013/python3-iterative/?page=4&languageTags=python3
#iterative solution
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node=root
        while True:
            if val<node.val and node.left is None:
                node.left=TreeNode(val)
                return root
            elif val>node.val and node.right is None:
                node.right=TreeNode(val)
                return root

            if val<node.val:
                node=node.left
            elif val>node.val:
                node=node.right