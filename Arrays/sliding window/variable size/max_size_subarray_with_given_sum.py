# ref : https://www.youtube.com/watch?v=TfQPoaRDeMQ

# Variable sized window differs from fixed sized window in the following ways:
# 1. Window size is not given. Instead, we are given some given condition(for example the window sum(ie, the subarray sum) should be equal to target sum) which needs to be met.
# 2. Process all windows using only 1 for loop and it involves the below steps:
# 2. Shrinking the window when the given condition is violated: We consider the scenario of where the given condition gets violated(for example the currrent window sum becomes greater than the target sum). 
# Then, we keep shrinking the window by removing left pointer computations and increasing the left pointer by 1 until the given condition is not violated. Thus, we 
# can't maintain a constant window size here as the given condition is dependent on the values in the array.


# Variable sized sliding window working:
# 1. We process each window using a single for loop and it invloves the following steps:
# a. Using the current element represented by right pointer, do some intermediate computation/computations.
# b. Check whether the given condition gets violated(for example the currrent window sum becomes greater than the target sum). 
#    Then, we keep shrinking the window by removing left pointer computation from the intermediate computation/computations and 
#    increasing the left pointer by 1 until the given condition is not violated. 
# c. Check if the given condition is met and compute the result(say maximum size) for the current window.

# 2. Once all the windows are processed(ie, when the for loop exits), we return the result.


# Ref: using neetcode's solution for minimum size subarray with given sum
class Solution:
    def maxSubArraySize(self,arr, target): 
        left,cur_sum= 0,0
        max_size = float('-inf')
        for right in range(len(arr)):
           cur_sum += arr[right]
           while cur_sum>target:
               cur_sum -= arr[left]
               left+=1
           if cur_sum==target:
                 max_size = max(max_size, (right-left+1))
               
        if max_size== float('-inf'):
            return 0
        else:
            return max_size
                     
Solution().maxSubArraySize([15,2,4,9,3,5,6,23],17)

#brute force approach
class Solution:
    def maxSubArraySize(self,arr, target): 
        max_size = float('-inf')
        for i in range(len(arr)):
            cur_sum=0
            for j in range(i,len(arr)):
               cur_sum += arr[j]
               if cur_sum==target:
                    max_size = max(max_size, (j-i+1))
        if max_size== float('-inf'):
            return 0
        else:
            return max_size
                     
Solution().maxSubArraySize([15,2,4,9,3,5,6,23],17)










