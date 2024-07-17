# ref: https://leetcode.com/problems/sqrtx/solutions/3180948/69-sqrt-x-with-step-by-step-explanation/?page=7
#ref: https://www.youtube.com/watch?v=HCCj-g0Tt6Q
#ref: https://www.youtube.com/watch?v=xiqmzdPKNOw
#ref: https://www.youtube.com/watch?v=Cg_wWPHJ2Sk&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=3
class Solution:
    def mySqrt(self, x: int) -> int:
        # using binary search method to find the square root
        left, right = 0, x
        while left <= right:
            # find the middle value of the current search range
            mid = (left + right) // 2
            mid_sqr= mid*mid
            # if the square of the middle value is greater than x, move the right boundary to the left 
            if mid_sqr > x:
                right = mid - 1
            # if the square of the middle value is smaller than x, move the left boundary to the right
            elif mid_sqr < x:
                left= mid + 1
            # if the square of the middle value is equal to x, return the middle value
            else:
                return mid
        # return the right boundary as the answer, because the left boundary is the largest integer that is smaller than the square root of x
        return right


# ref: https://leetcode.com/problems/sqrtx/solutions/25061/python-binary-search-solution-o-lgn/?page=8
# class Solution(object):
#     def mySqrt(self, x):
#         left, right = 0, x
#         while left <= right:
#             mid = (left + right)//2
#             mid_sqr= mid*mid
#             if mid_sqr <= x < (mid+1)*(mid+1):
#                 return mid
#             elif mid_sqr > x:
#                 right = mid - 1
#             else:
#                 left = mid + 1
                