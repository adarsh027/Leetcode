#ref: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/3191901/convert-sorted-array-to-binary-search-tree-with-step-by-step-explanation/?languageTags=python3
#notes:
#build root node using mid value in the given sorted array.
#build left subtree recursively using left portion of mid value
#build right subtree recursively using right portion of mid value
# return the root
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
# Efficient code
#ref: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/1363643/python3-two-solutions-explained-with-diagrams/?languageTags=python3
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(start, end):
            if start > end: 
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = recurse(start, mid-1)
            root.right = recurse(mid+1, end)
            return root

        return build(0, len(nums)-1)