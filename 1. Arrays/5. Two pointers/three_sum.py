# Ref: https://www.youtube.com/watch?v=8uWRUyWpy8M(Timothy H Chang)
# Ref: https://www.youtube.com/watch?v=n2_HLNY8e_Q(Sai Anish Malla)
# Ref: https://www.youtube.com/watch?v=6qgC-dqKElA(thecodingworld)
# Ref: https://www.youtube.com/watch?v=qJSPYnS35SE (Nick White)
# Ref: https://www.youtube.com/watch?v=jzZsG8n2R9A(NeetCode)
# Ref:https://www.youtube.com/watch?v=hNRS81I1OZ8&t=1298s(DataDaft)
# ref: https://www.youtube.com/watch?v=DhFh8Kw7ymk&t=2046s (striver)

#Brute force solution
class Solution:
    def three_sum(self, nums, target):
        res=[]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    cur_sum = nums[i] + nums[j] + nums[k] 
                    if (cur_sum== target):
                        triplets=tuple(sorted([nums[i],nums[j],nums[k]]))# sorting so that duplicate triplets can be identified and removed.
                        res.append(triplets)

        return list(set((res)))
             
                       
Solution().three_sum([15,15,0,10,2,4,-10,8,9,5,5,5,0,-10,0],0)

# output:
# [(0, 0, 0), (-10, 0, 10), (-10, 5, 5), (-10, 2, 8)]


# two-pointer stime and space complexity:
# Time O(N^2) | Space O(1)
# Time is O(N^2), basically called n squared or N * N, because our for loop will loop through almost the entire array so we round it to O(N) and Two Pointer algorithm is O(N), hence why the full answer is O(N^2) because for every iteration in the for loop O(N) we do a Two Pointer search O(N).
# Space is O(1) because we don't count the .sort space complexity for Python, you can verify this with the interviewer, tell them Python uses timsort and you're aware it uses O(N) space and ask if they want to count this or not.
# ref: https://leetcode.com/problems/3sum/solutions/2234102/python-two-pointers-time-o-n-2-space-o-1-explained/

# two-pointer solution
class Solution:
    def three_sum(self, nums, target):
        res= []
        nums.sort()
        for i in range(len(nums)-2): # this loop will help to fix the pointer for one number i.e, i
            if i>0 and nums[i]==nums[i-1]: #skipping if we found the duplicate of i.(Note: you can also use i!=0 here instead of using i>0)
                continue
            # Once you got the i, following two pointer approach to get the other no.s
            left, right = i+1, len(nums)-1
            while left<right:
                cur_sum= nums[i] + nums[left]+nums[right]
                if cur_sum==target:
                    res.append([nums[i],nums[left], nums[right]])
                    while left< right and nums[left]==nums[left+1] :   # skip duplicates for the left pointer  
                        left+=1
                    while left< right and nums[right]==nums[right-1]:  # skip duplicates for the right pointer
                        right-=1
                    left+=1
                    right-=1
                    
                elif cur_sum>target:
                    right-=1
                else:
                    left+=1
        return res
            
                       
Solution().three_sum([15,15,0,10,2,4,-10,8,9,5,5,5,0,-10,0],0)

Solution().three_sum([0,0,0,0],0)

# output:
# [[-10, 0, 10], [-10, 2, 8], [-10, 5, 5], [0, 0, 0]]




