#ref: https://leetcode.com/problems/rotate-array/solutions/3218810/189-solution-step-by-step-explanation/
# https://www.youtube.com/watch?v=BHr381Guz3Y
class Solution:
    def rotate(self, nums, k):
        # Calculate the number of steps we actually need to take
        k = k % len(nums)
    
        # Reverse the entire array
        nums.reverse()
    
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
    
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
        
        return nums
    
Solution().rotate([1,2,3,4,5,6,7],2) # [6, 7, 1, 2, 3, 4, 5]
        
Solution().rotate([1,2,3,4,5,6,7],3) #  [5, 6, 7, 1, 2, 3, 4]    

Solution().rotate([1,2,3,4,5,6,7],7) #  [1, 2, 3, 4, 5, 6, 7]  

Solution().rotate([1,2,3,4,5,6,7],9) #  [6, 7, 1, 2, 3, 4, 5]