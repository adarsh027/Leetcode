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

        return list(set(res))
Solution().three_sum([15,15,0,10,2,4,-10,8,9,5,5,5,0,-10,0],0)

# using dictionary
class Solution:
    def threeSum(self, nums, target):
        res=[]
        for i in range(len(nums)-2):
            nums_map = {}
            for j in range(i + 1, len(nums)):
                complement = target - (nums[i] + nums[j])
                if complement in nums_map:
                    print(nums[i], nums[j], complement)
                    triplets= tuple(sorted([nums[i], nums[j], complement])) # sorting so that duplicate triplets can be identified and removed.
                    res.append(triplets)
                else:
                    nums_map[nums[j]]=1
                
        return list(set(res))

Solution().threeSum([15,15,0,10,2,4,-10,8,9,5,5,5,0,-10,0],0)

# using set

class Solution:
    def threeSum(self, nums, target):
        res=[]
        for i in range(len(nums)-2):
            nums_map = set()
            for j in range(i + 1, len(nums)):
                complement = target - (nums[i] + nums[j])
                if complement in nums_map:
                    print(nums[i], nums[j], complement)
                    triplets= tuple(sorted([nums[i], nums[j], complement])) # sorting so that duplicate triplets can be identified and removed.
                    res.append(triplets)
                else:
                    nums_map.add(nums[j])
                
        return list(set(res))

Solution().threeSum([15,15,0,10,2,4,-10,8,9,5,5,5],0)