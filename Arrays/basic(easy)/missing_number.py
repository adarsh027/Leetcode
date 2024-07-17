# problem: https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
class Solution:
    def missingNumber(self,array,n):
        sum=n*(n+1)//2
        cur_sum=0
        for x in array:
            cur_sum+=x
        return sum-cur_sum


Solution().missingNumber([6,1,2,8,3,4,7,10,5],10)