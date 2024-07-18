class Solution:
    def findDisappearedNumbers(self, nums):
        # Step 1: Mark the presence of each number by negating the value at the corresponding index
        for num in nums:
            index = abs(num) - 1  # Convert the number to an index
            nums[index] = -abs(nums[index])  # Mark the presence by setting the value to negative
        
        # Step 2: Collect all indices that have positive values, which indicates the missing numbers
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)  # Convert the index back to the number
        
        return missing_numbers

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDisappearedNumbers(nums))  # Output: [5, 6]

nums = [1, 1]
print(solution.findDisappearedNumbers(nums))  # Output: [2]
