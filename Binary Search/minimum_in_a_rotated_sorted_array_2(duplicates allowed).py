#ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solutions/48908/clean-python-solution/?page=3
#ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solutions/373747/python-binary-search-compare-to-153/?page=5
class Solution:
    def search(self,nums): 
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)// 2
            if nums[mid] > nums[right]:  # search on the right side,
                left = mid + 1
            elif nums[mid] < nums[right]: 
                right = mid # search the minimum in the left side
            elif nums[mid]==nums[right]:
                right-=1
        return nums[left]


Solution().search([6,7,0,0,1,1,1,2,3])  