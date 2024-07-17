# One-Sided Two-Pointer Technique Explained:
# Time and space complexity: O(n) and  O(1)
class Solution:
    def removeElement(self, nums, val):
        left = 0  # Initialize the left pointer. It is used to place any non-val element found in the array at the beginning of the array.
        for i in range(len(nums)):
            if nums[i] != val:# if a non-val element is found in the array, place it at the left index and increment left.
                nums[left] = nums[i]
                left += 1
        return left  # The left pointer indicates the count of non-val elements
    

# Slightly optimized version
def removeElement(self, nums, val):
    left = 0
    for i in range(len(nums)):
        if nums[i] != val:
            if i > left:  # Check to avoid unnecessary self-assignment
                nums[left] = nums[i]
            left += 1
    return left

# Condition i > left: The check ensures that we only perform the assignment when i is actually ahead of left, meaning that i has 
# encountered a non-val element somewhere after left has started accumulating valid elements. This skips the self-assignment when
# i and left are the same, which occurs when all elements from the start up to i are non-val.

# Why use i> left condition instead of i!= left condition:
# Precision: i > left is more precise in the context of this problem. It directly addresses the scenario we care about: avoiding 
# operations when they are not needed. i != left could theoretically also check for i < left, which isn't a possibility in this structured loop, making i > left a more accurate reflection of the intended logic.

# One-Sided Two-Pointer Technique Explained:
# Slow Pointer (left): This pointer represents the position where the next element not equal to val should be placed. It only moves when a non-val element is found.
# Fast Pointer (i): This pointer is used to examine each element of the array. If an element does not match val, it is copied to the index pointed by left.
# This technique ensures that "non-val" elements are moved to the beginning of the array, and the final value of left will be the count of these "non-val" elements.

# How It Works:
# 1. Initialize left at 0: This points to the index where the next valid element (not equal to val) will be placed.
# 2. Iterate with i: Loop through the array with the i pointer.
# 3. Check if nums[i] != val:
#     - If true, copy nums[i] to nums[left] and increment left.
#     - If false, simply move to the next element.
# 4. Return left: After the loop, left will have the count of elements that are not val, and the elements from nums[0] to nums[left-1] will be the required elements.


# Converging Two-Pointer Technique Explained:
# Time and space complexity: O(n) and  O(1)
class Solution:
    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Move the left pointer until it finds an element equal to val
            while left <= right and nums[left] != val:
                left += 1
            
            # Move the right pointer until it finds an element not equal to val
            while left <= right and nums[right] == val:
                right -= 1
            
            # Swap if the left is less than right
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left  # Left points to the number of elements not equal to val

# Converging Two-Pointer Technique Explained:
# Left Pointer (left): This pointer starts at the beginning of the array and moves rightward, but only moves when placing elements that are not equal to val.
# Right Pointer (right): This pointer starts at the end of the array and moves leftward, acting as a check to see if an element is equal to val and can be ignored (or eventually overwritten).
# This approach aims to use the right pointer to find elements that are not equal to val and swap or replace them into the place of elements that are equal to val found by the left pointer. 
# How It Works:
# 1. Initialize Pointers:
#     left starts at the beginning of the array.
#     right starts at the end of the array.
# 2. Find Target Element with Left Pointer:
#     Move left until you find an element that is equal to val.
# 3. Find Non-Target Element with Right Pointer:
#     Move right until you find an element that is not equal to val.
# 4. Swap Elements:
#     If left is still less than right, swap the elements at left and right. After swapping, move left forward and right backward to continue the process.
# 5. Finish when Left meets or crosses Right:
#     When left crosses right, all the elements to the left of left are guaranteed to not be equal to val.
# 6. Return left:
#     This gives the count of elements not equal to val since all such elements are now at the start of the array.
#     This two-pointer approach allows you to minimize the number of unnecessary operations by directly handling and bypassing the elements equal to val more efficiently. It's particularly useful when val elements are frequent or clustered, as it quickly segregates them to the end of the array.


# Key Differences:
# 1.Pointer Movement:
#     Converging Two-Pointer: Uses both left and right pointers moving toward each other. This approach actively uses both pointers to shrink the problem space from both ends, making it efficient when there are large blocks of val at both ends of the array.
#     One-Sided Two-Pointer: The left pointer marks the position for the next non-val element, while i iterates through the array. This method is straightforward and very intuitive, especially for those less familiar with two-pointer techniques.
# 2. Efficiency in Swapping:
#     Converging Two-Pointer: Minimizes the number of writes by only swapping when absolutely necessary, which could be more efficient in cases where val elements are frequent and spread throughout the array.
#     One-Sided Two-Pointer: Although efficient in linearity, this method may involve more operations because it rewrites every non-val element to its correct position, even if it's already in the right place.
# 3. Complexity and Intuitiveness:
#     Converging Two-Pointer: While slightly more complex due to the management of two moving indices, it offers a more balanced and possibly more efficient handling in varied scenarios, particularly where the array ends have a high concentration of val.
#     One-Sided Two-Pointer: Offers utmost simplicity and is highly intuitive. It's easy to understand and implement, making it ideal for beginners or in scenarios where code readability and maintainability are priorities.

# When to Use Each:
# Converging Two-Pointer: Best when you anticipate that the array might have multiple contiguous val elements, especially towards the ends. It's also preferable when minimizing the number of element swaps or moves is crucial.
# One-Sided Two-Pointer: Ideal for scenarios where simplicity and clarity are more valuable than optimizing a few operations. It's particularly effective when the array is either mostly non-val elements or when the performance difference is negligible.