# Time and space complexity: O(n) and  O(1)
class Solution:
    def replaceElements(self, arr):
        max_right = -1  # Initialize max_right to -1 because the last element will be -1
        # Iterate from the last element to the first element
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(max_right, arr[i])  # Find the new maximum for the next iteration
            arr[i] = max_right  # Replace the current element with max_right
            max_right = new_max  # Update max_right to new_max for the next iteration
        return arr
    

# Explanation of the Code:
# 1. Initialization: max_right is set to -1 initially because the last element must be replaced with -1.
# 2. Loop: The loop runs from the last element to the first (right to left). For each element:
#     - new_max is calculated as the maximum of max_right and the current element. This prepares the maximum for the next iteration.
#     - The current element arr[i] is replaced with max_right, which contains the maximum value from its right side seen so far.
#     - max_right is then updated to new_max to ensure it carries the correct maximum to the next iteration.
# 3. Return the array