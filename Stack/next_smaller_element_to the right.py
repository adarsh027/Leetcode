#ref: https://leetcode.com/problems/next-greater-element-ii/solutions/145374/python-beats-100/
# circular array solution
class Solution(object):
    def nextSmallerElements(self, nums):
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(2*n - 1, -1, -1):
            while s and s[-1] >= nums[i%n]:#Compare top stack element with current array element and keep removing greater elements from the stack
                s.pop()
            if s:
                res[i%n] = s[-1]
            s.append(nums[i%n])
        return res

# Input: nums = [1,2,7,4,3]
# Output: [-1, 1, 4, 3, 1]
Solution().nextSmallerElements([1,2,7,4,3])

#regular array solution
class Solution(object):
    def nextSmallerElements(self, nums):
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(n - 1, -1, -1):
            while s and s[-1] >= nums[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(nums[i])
        return res

# Input: nums = [1,2,7,4,3]
# Output: [-1, -1, 4, 3, -1]
Solution().nextSmallerElements([1,2,7,4,3])

