# Given   1<= nums[i] <= n, where n = length
# This means that subtracting 1 from any value in the array will be a valid index.
# Note: suppose you have an array of lenght, n =5, then the values in the array can be from 1,2,...5. If you subtract 1 from any value in nums, it is a valid index in the array.

#ref: 
# https://www.youtube.com/watch?v=Y8x0iAVEITo
# https://www.youtube.com/watch?v=kRrSeAZRD6E
# https://www.youtube.com/watch?v=aMsSF1Il3IY&t=3s

# 1. Iterate though nums and Compute index for each number as: index = abs(num) - 1
# 2. If the array element at this index is less than 0, the current number is a duplicate value and is hence added to the result. 
# 3. Otherwise, it means that the current number is seen/visited for the first time and thus the array element at this index is made negative.

# Key point for solving this problem: Use the array itself to record information about which elements have been seen. The element which is seen is marked 
# as seen/visited by making the array element at the computed index as negative.

class Solution:
    def find_duplicates(self, nums):
        dups = []
        for num in nums:
            index = abs(num) - 1  # Compute index using the current number
            if nums[index] < 0:
                dups.append(abs(num))  # If the element at this index is already negative, it's a duplicate. Add the current number to the result.
            else:
                nums[index] = -nums[index]  # Otherwise, mark the element at this index as negative.This signifies the 1st appearance of the current number.
        
        return dups

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().find_duplicates(nums))  # Output: [2, 3]

    

        







