#Ref: https://www.youtube.com/watch?v=OADYlWbLbfE
#ref: referred and made it like the program anagarams_in_a_string.py
# Logic
# In each window processing, do the following
# Build deq by storing negative numbers enccountered.
# Build result by taking  the leftmost element,ie, deq[0], in the deque.

#Note: here, deq is the intermediate window computation we need to compute repeatedly for every window to generate/build the result(answer).
from collections import deque
class Solution(object):
    def firstNegativeSlidingWindow(self, nums, k):
        left=0
        deq = deque() # for storing negative numbers.
        res = []
     
        for right in range(k): # computing deq(consisting of negative numebrs) for the 1st window
            if nums[right]<0:
                deq.append(nums[right])
                
        if deq:                   # computing result(answer) for the 1st window. The leftmost element will be the 1st negative number in the 1st window. 
            res.append(deq[0])
        else:
            res.append(0)
                
        for right in range(k, len(nums)): # computing deq for the subsequent windows
            
            if nums[right]<0:
                deq.append(nums[right])
                
            if deq and deq[0] == nums[left]:# pop the leftmost element from deq if we have it as the leftmost element
                deq.popleft()
            left+=1
            
            if deq :                    # computing result(answer) for the current window
                res.append(deq[0])
            else:
                res.append(0)
                
            

        return res
    
Solution().firstNegativeSlidingWindow([12, -1, -7, 8, -15, 30, 16, 28],3)

# Using Aditya Verma's template for fixed sized window
# Ref: https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4
def firstNegativeSlidingWindow(arr, k):
    left = 0
    right = 0
    neg_nums = []
    result = []
       
    while right < len(arr):
        if arr[right] < 0: # Compute neg_nums
            neg_nums.append(arr[right])
        
        #increase right pointer till we reach window size    
        if((right - left + 1) < k):
            right += 1
            
        #if we hit the window size
        elif ((right - left + 1) == k):
            
            #compute final result
            if neg_nums:
                result.append(neg_nums[0])
                if arr[left] == neg_nums[0]:#remove element pointed to by the left pointer from the computation
                    neg_nums.pop(0)  
            else:
                result.append(0)     
            left += 1
            right += 1
            
    return result
firstNegativeSlidingWindow([12, -1, -7, 8, -15, 30, 16, 28],3)













