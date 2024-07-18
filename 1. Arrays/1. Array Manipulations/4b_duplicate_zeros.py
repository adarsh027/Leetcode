# Brute force approach
# 1. Iterate through the array: The loop runs until the end of the array is reached.
# 2. Check for zero: If a zero is found, all elements after this zero are shifted one position to the right. This makes space to duplicate the zero.
# 3. Boundary Check: Before duplicating the zero, ensure the duplicate does not go out of bounds.
# 4. Skip the duplicated zero: Increase the index by an additional one to avoid duplicating the newly added zero.

class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                # Move all elements one step to the right to make space for the duplicate zero
                j = n - 1
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                # We need to check if i+1 is within the array bounds before duplicating zero
                if i + 1 < n:
                    arr[i + 1] = 0
                # Skip the next zero to avoid duplicating it again
                i += 1
            i += 1

# Example Usage
arr = [1, 0, 2, 3, 0, 4, 5]
sol = Solution()
sol.duplicateZeros(arr)
print(arr)  # Output: [1, 0, 0, 2, 3, 0, 0]


# Using Python built-in methods approach
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i < len(arr)-1:
            if arr[i]==0:
                arr.insert(i+1, 0)
                del arr[-1]  # alternatively, you can use arr.pop()
                i+=2
            else:
                i+=1

# Most Optimum approach : O(n) time comlpexity and O(1) space complexity

# Note: 
# Shifting from left to right: When duplicating a zero in an array, all the elements to the right of that zero needs to moved /shifted to the right to make space for that new duplicated zero.
# Note: Why reverse traversing is preferrred over foward traversing when duplicating zeros in an array?
# Reverse traversal ensures that you don't overwrite any elements that have not yet been processed. By moving from the end to the beginningie(ie, from right to left), each element is moved or duplicated only once, directly into its final position once, without disturbing the unprocessed parts of the array.

class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        total_zeros = arr.count(0)  # Count total zeros in the array

        # Reverse traversal considering duplications
        for i in range(n - 1, -1, -1):
            # (i + total_zeros): new postion where we can potentially place an element(when shifting) or potentailly place a zero(when duplicating).
            # Calculate new position where the current element could be potentially placed(shifted) based upon the total zeros count,
            # and if wihtin bounds, place the curent element in the new position.
            if i + total_zeros < n:
                arr[i + total_zeros] = arr[i]
            
            # If current element is a zero, it could potentially be duplicated
            if arr[i] == 0:
                total_zeros -= 1  # Decrease zero count as the current zero is already considered
                # Calculate new position where zero could be potentially placed(duplicated) based upon the updated total zeros count,
                #  and if within bounds, place zero in this position
                if i + total_zeros  < n:
                    arr[i + total_zeros ] = 0  # Duplicate zero if within bounds

# Example usage
arr = [8, 4, 5, 0, 0, 0, 0, 7]
sol = Solution()
sol.duplicateZeros(arr)
print(arr)  # Expected output: [8, 4, 5, 0, 0, 0, 0, 0]



        