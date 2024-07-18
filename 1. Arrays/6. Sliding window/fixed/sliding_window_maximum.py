#ref: Using for loop (modified neetcode's solution using while loop)
#ref: https://www.youtube.com/watch?v=DfljaUwZsOk&t=180s
# ref: https://www.youtube.com/watch?v=MCvGwtkqJS0&t=313s
#ref: https://www.youtube.com/watch?v=Bx0Z3GaNJJM
#ref: https://www.youtube.com/watch?v=MCvGwtkqJS0
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deq = deque()
        result = []
        left=0
        for right in range(k):
            while deq and nums[deq[-1]] <= nums[right]: # pop all elements starting from end/right of the queue that are smaller or equal to the current element.
                deq.pop()
            deq.append(right)
        result.append(nums[deq[0]])
        
        for right in range(k, len(nums)):
            while deq and nums[deq[-1]]<= nums[right]:# pop all elements starting from end/right of the queue that are smaller or equal to the current element.
                deq.pop()
            deq.append(right) # add current window index to deq
            
            if deq[0]== left:# After sliding, remove the left index from deq
                deq.popleft()
                
            if (left+right)>=k:
                result.append(nums[deq[0]])
                left+=1

        return result
    
Solution().maxSlidingWindow([15,43,4,8,9,7,14,23],3)

