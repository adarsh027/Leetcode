# ref:https://www.youtube.com/watch?v=U8XENwh8Oy8
#ref: https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/894031/python-o-logn-detailed-explanation/?page=5
class Solution:
    def search(self,nums,target): 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print("middle element is: ",nums[mid])
            if target == nums[mid]:
                return mid
            
            # If the middle number lies in  left sorted portion
            # check if target lies between left element and middle element
            # and update right or left accordingly
            elif nums[left] <= nums[mid]:
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
                    
        return -1


Solution().search([6,7,0,1,2,3],7)  
# Solution().search([4,5,6,7,0,1,2],0) # here, middle element 7 is  in left sorted array
# Solution().search([6,7,0,1,2,3,4],6) # here, middle element 1 is  in right sorted array


