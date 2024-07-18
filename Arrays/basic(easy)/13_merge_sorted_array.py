#source : chatgpt
# ref : https://www.youtube.com/watch?v=P1Ic85RarKY&t=180s (neetcode)
class Solution:
    def merge(self, nums1, m, nums2, n) :
        # Pointers for nums1, nums2, and the end of nums1
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge nums2 into nums1 starting from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Handle any remaining elements in nums2 (Here, you fill nums1 with leftover elements in nums2)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]



### Explanation


### Explanation

# 1. **Initialization**:
#    - `p1` starts at `m - 1`, pointing to the last valid element in `nums1`.
#    - `p2` starts at `n - 1`, pointing to the last element in `nums2`.
#    - `p` starts at `m + n - 1`, pointing to the last position in `nums1`.

# 2. **Main Merge Loop**:
#    - The main while loop runs as long as both `p1` and `p2` are non-negative.
#    - If `nums1[p1]` is greater than `nums2[p2]`, copy `nums1[p1]` to `nums1[p]` and decrement `p1`.
#    - Otherwise, copy `nums2[p2]` to `nums1[p]` and decrement `p2`.
#    - Decrement `p` in each iteration.

# 3. **Handling Remaining Elements in `nums2`**:
#    - After the main loop, if `p2` is still non-negative, copy the remaining elements from `nums2` to `nums1` using another while loop.


# alternative approach (extra memory space complexity of O(m+n) due to the use of the temporary array, and thus not recommended)

class Solution:
    def merge(self, nums1, m, nums2, n) :
        # Temporary array to store the merged result
        temp = []
        i, j = 0, 0

        # Merge the two arrays
        while i <= m-1 and j <= n-1:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        # If there are remaining elements in nums1
        while i <= m-1:
            temp.append(nums1[i])
            i += 1

        # If there are remaining elements in nums2
        while j <= n-1:
            temp.append(nums2[j])
            j += 1

        # Copy the merged result back into nums1
        # Note: To ensure that the changes are made to the original list(nums1) passed to the function, we need to copy the elements from temp 
        # into nums1 element by element.
        for k in range(m + n):
            nums1[k] = temp[k]

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


