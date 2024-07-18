# using 2 pointer variables, left and right.
class Solution:
    def maxsubArraySum(self,arr, k): 
        cur_sum = 0
        max_sum = 0
        left = 0
        #first we can compute the sum of first window and consider it as maximum
        for right in range(k):
            cur_sum = cur_sum + arr[right]
        max_sum = cur_sum
        #Now compute the sum of subsequent windows
        #by sliding. That is, increase one element from end and subtract start element of last processed window.
        # Compare and keep updating max_sum until you reach the end.
        for right in range(k, len(arr)):
            cur_sum = cur_sum + arr[right] - arr[left] # Here, arr[right-k] is equivalent to arr[left if you choose to use an left pointer variable
            left+=1
            max_sum = max(max_sum, cur_sum)
        return max_sum
           
Solution().maxsubArraySum([15,4,4,8,9,7,14,23],3)

#Note1: Indexing relation within the window itself
 #   right(right index of current window) - left(left index of current window) + 1 = k(size of current window)
#note2: Indexing relation between the current window and previous window. This relation you can use iou want to avoid using additonal pointer variable "left".
#    left(starting index of last window) = k(size of current window) - right(right index of current window) 


# using only 1 pointer variable, right.
class Solution:
    def maxsubArraySum(self,arr, k): 
        cur_sum = 0
        max_sum = 0
        #first we can compute the sum of first window and consider it as maximum
        for right in range(k):
            cur_sum = cur_sum + arr[right]
        max_sum = cur_sum
        #Now compute the sum of subsequent windows
        #by sliding. That is, increase one element from end and subtract start element.
        # Compare and keep updating max_sum until you reach the end.
        for right in range(k, len(arr)):
            cur_sum = ((cur_sum + arr[right]) - arr[right-k]) # Here, arr[right-k] is equivalent to arr[left if you choose to use an left pointer variable
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
           
Solution().maxsubArraySum([15,4,4,8,9,7,14,23],3)

# Using Aditya Verma template for fixed size window
# ref : https://www.youtube.com/watch?v=KtpqeN0Goro&t=1093s
# ref: https://www.youtube.com/watch?v=LV-BgyeH8yo&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=
class Solution:
    def maxsubArraySum(self,arr, k): 
        left,right = 0,0
        max_sum = 0
        cur_sum = 0
        while right<len(arr):
           cur_sum = cur_sum + arr[right]
           if (right-left+1)<k:
               right+=1
           elif(right-left+1)==k: # this means we have hit the size k of the window(ie, i and j are at correct positions for the window size k)
               max_sum = max(max_sum, cur_sum) # this statement should come before the sliding window statement since when we 1st hit the size k of the window, the sum of the 1st window should be considered as maximum. Then we do the sliding using the sliding statement.
               cur_sum = cur_sum - arr[left] # sliding window statement
               left+=1
               right+=1
        return max_sum
           
           
Solution().maxsubArraySum([15,4,4,8,9,7,14,23],3)




#brute force approach
class Solution:
    def maxsubArraySum(self,arr, k): 
        max_sum = float('-inf')
        for i in range(len(arr)):
            cur_sum=0
            for j in range(i,len(arr)):
               cur_sum += arr[j]
               if (j-i+1) == k:
                     max_sum = max(max_sum, cur_sum)
        if max_sum== float('-inf'):
            return 0
        else:
            return max_sum
                     
Solution().maxsubArraySum([15,4,4,8,9,7,14,23],3)














