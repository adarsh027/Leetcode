#ref: https://leetcode.com/problems/search-in-a-binary-search-tree/solutions/688364/python-3-bst-easy-to-read-and-understand/?languageTags=python3
#recursive solution
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val==root.val:
            return root
        elif val<root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
        
   
#ref: https://leetcode.com/problems/search-in-a-binary-search-tree/solutions/3016072/simple-python-iterative-solution-o-h-o-1/?languageTags=python3
#iterative solution
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val==val:
                return root
            if root.val<val:
                root=root.right
            else:
                root=root.left
        return None
