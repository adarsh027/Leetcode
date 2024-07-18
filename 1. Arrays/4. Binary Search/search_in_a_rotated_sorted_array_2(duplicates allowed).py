#ref: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/28195/python-easy-to-understand-solution-with-comments/?page=2
class Solution:
    def search(self,nums,target): 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print("middle element is: ",nums[mid])
            if nums[mid]==target:
                return True
            while left < mid and nums[left] == nums[mid]: # discarding duplicates
                left += 1
            
            # If the middle number lies in  left sorted portion
            # check if target lies between left element and middle element
            # and update right or left accordingly
            if nums[left] <= nums[mid]:
                print("middle number lies in  left sorted portion")
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            # If the middle number lies in right sorted portion
            # check if target lies between middle element and right element
            # and update left or right accordingly
            else:
                print("middle number lies in right sorted portion")
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False


Solution().search([6,7,0,1,2,3],7)  
