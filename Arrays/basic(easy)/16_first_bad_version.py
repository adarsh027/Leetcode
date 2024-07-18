# ref: chatgpt, https://www.youtube.com/watch?v=vnfGi-ucwTE (greg hogg)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # The first bad version is at mid or before mid
            else:
                left = mid + 1  # The first bad version is after mid
        return left  # left will be pointing to the first bad version

# Example usage:
# Assuming isBadVersion API is defined and works correctly
# print(Solution().firstBadVersion(n))  # Replace 'n' with the number of versions

# Time: O(log n), Space: O(1)
