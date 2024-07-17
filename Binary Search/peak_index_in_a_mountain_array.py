
#ref: https://leetcode.com/problems/peak-index-in-a-mountain-array/solutions/1535878/python-from-o-n-to-o-logn-clean-concise/?page=3
class Solution:
    def peakIndexInMountainnumsay(self,nums):
        n = len(nums)
        left = 1
        right = n - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

