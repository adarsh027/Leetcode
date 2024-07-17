# naive approach :checking sum for every pair of elements in the given array
class Solution:
    def two_sum(self,nums, target): 
       for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]== target:
                    return [i,j]

           
Solution().two_sum([15,2,4,8,9,5,10,23],11)


# using dictionary
# ref: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=326s
class Solution:
    def two_sum(self,nums, target): 
       nums_map = {} # dictionary to store already visited numbers with its index
       for indx,num in enumerate(nums):
           complement = target - num
           print(nums_map, complement)
           if complement in nums_map:
               return [nums_map[complement], indx]    
           else:
               nums_map[num] = indx
       
                       
Solution().two_sum([15,2,4,8,9,5,10,23],11)


