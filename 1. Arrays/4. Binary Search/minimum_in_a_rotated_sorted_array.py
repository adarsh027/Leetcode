
#ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/
#Note: no. of times the array was rotated = index of the minum element in the rotated array

class Solution:
    def search(self,nums): 
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)// 2
            if nums[mid] > nums[right]:  # search on the right side,
                left = mid + 1
            elif nums[mid] <= nums[right]: 
                right = mid # search the minimum in the left side
        return nums[left]
    

Solution().search([6,7,0,1,2,3])  


#Alternative solution
#ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/1436502/python-binary-search-with-picture-clean-concise/?page=2
class Solution:
    def search(self, nums):
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:  # The nums[mid] is the minimum number
                return nums[mid]
            if nums[mid] > nums[right]:  # search on the right side, because smaller elements are in the right side
                left = mid + 1
            else:
                right = mid - 1  # search the minimum in the left side
                
Solution().search([6,7,0,1,2,3])  