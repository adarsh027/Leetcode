class Solution(object):
    def prevSmallerElements(self, nums):
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(n):
            while s and s[-1] >= nums[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(nums[i])
        return res


Solution().prevSmallerElements([1,2,7,4,3])
