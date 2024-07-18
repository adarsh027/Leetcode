class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # Initialize an empty set to track seen elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        return False  # No duplicates found

# Example usage:
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.containsDuplicate(nums))  # Output: True
