# Return left and right index of subarray of given sum
# sliding window approach : applicable to  array containing postive integers only
# use prefix sum apprach as it is more versatile approach.
# references:
#1. submission by user SagarMc for  https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
#2. https://www.youtube.com/watch?v=Ofl4KgFhLsM
class Solution:
    def subArraySum(self,arr, n, target): 
        left, cur_sum = 0, 0
        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target and left < right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                return [left+1, right+1] # adding 1 to left and right since the problem specifies 1-based indexing; if it was 0 based indexing, then there is no need for addding 1 to left and right
        return [-1] # implies not found
           
Solution().subArraySum([15,3,4,8,9,7,14,23],8,24)

# altrnatively using while loop
class Solution:
    def subArraySum(self,arr, n, target): 
        left,right, cur_sum = 0, 0,0
        while right<n:
            cur_sum += arr[right]
            while cur_sum > target and left < right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                return [left+1, right+1] # adding 1 to left and right since the problem specifies 1-based indexing; if it was 0-based indexing, then there is no need for addding 1 to left and right
            
            right += 1
        return [-1]
    
Solution().subArraySum([15,3,4,8,9,7,14,23],8,24)