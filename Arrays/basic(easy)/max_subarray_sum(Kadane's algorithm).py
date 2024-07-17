# brute force or naive appraoch
class Solution:
    def subArraySum(self,arr): 
       max_sum=arr[0] # note: if max_sum is set to 0, then it won't work when all the values in the array are negative.
       #max_sum=float('-inf') # Thus, set max_sum to minus infinity or the 1st element of the array so that it works even when all the array values are negative.
       for i in range(len(arr)):#
               cur_sum=0
               for j in range(i,len(arr)): 
                   cur_sum= cur_sum+ arr[j]
                   max_sum = max(max_sum,cur_sum)
       return max_sum

Solution().subArraySum([-5,-7,-2,-7,-6,-23])


#Kadane's algorithm
# Ref https://www.youtube.com/watch?v=5WZl3MMT0Eg
# ref https://www.youtube.com/watch?v=HCL4_bOd3-4
class Solution:
    def subArraySum(self,arr): 
        cur_sum = 0
        max_sum = arr[0] # note: if max_sum is set to 0, then it won't work when all the values in the array are negative.
        #max_sum=float('-inf') # Thus, set max_sum to minus infinity or the 1st element of the array so that it works even when all the array values are negative.
        for i in range(len(arr)):
            cur_sum= cur_sum+ arr[i]
            max_sum = max(max_sum,cur_sum)
            if cur_sum <0:
                cur_sum = 0
        return max_sum
    
Solution().subArraySum([-2,-7,-3,-7,-23])