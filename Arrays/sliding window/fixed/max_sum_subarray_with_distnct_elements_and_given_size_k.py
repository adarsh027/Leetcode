#refer max_sum_subarray_with_given_size_k.py and anagrams_in_a_string.py

# Note: no. of unique elements in current window = length of dictionary "numCount"
# Note: when the no. unique elements in a window is equal to the window size, it implies that all the elements in the window are unique, without any repeating elements.
class Solution:
    def maxsubArraySum(self,nums, k): 
        numCount = dict()
        cur_sum=0
        max_sum = 0
        left= 0
        for right in range(k):
            cur_sum += nums[right]
            numCount[nums[right]] = 1 + numCount.get(nums[right],0)
        if len(numCount) == k:# compute result for 1st window
            max_sum = cur_sum
        for right in range(k, len(nums)):
            cur_sum = cur_sum + nums[right] - nums[left]
            numCount[nums[right]] = 1 + numCount.get(nums[right],0)
            numCount[nums[left]] -= 1
            if numCount[nums[left]] == 0:
               numCount.pop(nums[left])
            left+=1
            if len(numCount) == k: # Note: length of numCount gives the count of distinct elements in the current window
                max_sum = max(max_sum, cur_sum)
        return max_sum



Solution().maxsubArraySum([1,5,4,2,9,9,9],3) # 15