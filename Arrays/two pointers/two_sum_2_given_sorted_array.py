# two pointer approach
#Two pointer approach is handy in problems where a sorted array needs to fulfill certain constraints
# w.r.t a specific array element(as in the case of binary search) or a set of array elements(such as a pair, a triplet, or even a subarray)
# Reference for the above lines about two pointers:https://www.educative.io/blog/coding-interview-leetcode-patterns

#ref: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/3208849/167-solution-with-step-by-step-explanation/
# ref : https://www.youtube.com/watch?v=cQ1Oz4ckceM
# ref: https://www.youtube.com/watch?v=UXDSeD9mN-k

class Solution:
  def twoSum(self, numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


Solution().twoSum([2,7,11,15,20,31], 17)
#Note: The leetcode problem states that "The tests are generated such that there is exactly one solution."


# Brute force approach
class Solution(object):
    def twoSum(self, nums, target):        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                if (nums[i]+nums[j]) == target: 
                    return[i+1,j+1] # Adding 1 to each variable since the return type is 1 indexed instead of 0 indexed. 
                
        return [-1,-1]
    
Solution().twoSum([2,7,11,15,20,31], 17)


