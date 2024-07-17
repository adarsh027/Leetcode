#naive method : comparing every pair of elements in the given array
class Solution(object):
    def findDuplicate(self, nums):
        for i in range(0, len(nums)):    
            for j in range(i+1, len(nums)):    
                if(nums[i] == nums[j]):    
                    print(nums[j]) 
                
Solution().findDuplicate([3,1,3,4,2,4,8,9])


# using set
class Solution(object):
    def findDuplicate(self, nums):
        dups=[]
        seen =set() # seen will contain only unique elements
        for num in nums:
            if num in seen:
                dups.append(num)
            else:
                seen.add(num)
        print(seen, dups)

                
Solution().findDuplicate([3,1,3,4,2,4,8,9])

# using dictionary
class Solution(object):
    def findDuplicate(self, nums):
        dups=[]
        seen ={}    # seen will contain only unique keys
        for num in nums:
            if num in seen: # this is equivalent to:  if num in seen.keys()
                seen[num] = seen[num]+1
                dups.append(num)
            else:
                seen[num] = 1  
        print(seen.keys(),dups)
                

Solution().findDuplicate([3,1,3,4,2,4,8,9,2])






