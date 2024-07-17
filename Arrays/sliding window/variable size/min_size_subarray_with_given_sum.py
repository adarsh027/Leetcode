#Ref: https://www.callicoder.com/minimum-size-subarray-sum-smallest-subarray-with-given-sum/
class Solution:
    def minSubArraySize(self,arr, target): 
        left,cur_sum= 0,0
        min_size = float('inf')
        for right in range(len(arr)):
           cur_sum += arr[right]
           while cur_sum>target:
               cur_sum -= arr[left]
               left+=1
           if cur_sum==target:
                 min_size = min(min_size, (right-left+1))
               
        if min_size== float('inf'):
            return 0
        else:
            return min_size
                     
Solution().minSubArraySize([15,2,4,9,3,5,7,23],13)

# Using Aditya Verma template for variable size window
# ref : https://www.youtube.com/watch?v=TfQPoaRDeMQ
# ref: https://www.youtube.com/watch?v=LV-BgyeH8yo&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=9
class Solution:
    def minSubArraySize(self,arr, target): 
        left,right = 0,0
        cur_sum = 0
        min_size = float('inf')
        while right<len(arr):
           cur_sum += arr[right]
           if cur_sum < target:
               right+=1
           elif cur_sum==target: 
               min_size = min(min_size, right-left+1) 
               right+=1
           else:
               while cur_sum>target:
                   cur_sum -= arr[left]
                   left+=1
               if cur_sum==target: 
                   min_size = min(min_size, right-left+1)
               right+=1
               
        return min_size
                     
Solution().minSubArraySize([15,2,4,9,3,5,7,23],13)



#brute force approach
class Solution:
    def minSubArraySize(self,arr, target): 
        min_size = float('inf')
        for i in range(len(arr)):
            cur_sum=0
            for j in range(i,len(arr)):
               cur_sum += arr[j]
               if cur_sum==target:
                    min_size = min(min_size, (j-i+1))
        if min_size== float('inf'):
            return 0
        else:
            return min_size
                     
Solution().minSubArraySize([15,2,4,9,3,5,7,23],13)