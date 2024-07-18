# This problem is similar to remove elemnts from array
# method 1 : without swapping
class Solution:
    def moveZeroes(self, nums):
        left = 0   # Initialize the left pointer. It is used to place any non-zero element found in the array at the beginning of the array.
        # First pass: move all non-zero elements to the front of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        
        # Second pass with a while loop: Fill remaining array space with zeros
        while left < len(nums):
            nums[left] = 0
            left += 1


# method 2 : with swapping
class Solution:
    def moveZeroes(self, nums):
        left = 0  # Pointer for placing the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1  # Move left pointer to the next position for a non-zero element

#note: For both the methods can further optimize by introducing the condition i > left, like we did for remove elements from array problem.





