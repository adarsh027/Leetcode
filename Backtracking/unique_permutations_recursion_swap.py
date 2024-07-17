#solution using class or object oriented approach as in leetcode site
class Solution:
    def permuteUnique(self, nums):
        def backtrack(start, end):
            seen= set()
            if start == end:
                res.append(nums[:])
                print(nums)
            for i in range(start, end):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start+1, end)
                    nums[start], nums[i] = nums[i], nums[start]
                
        res = []
        backtrack(0, len(nums))
        return res

res=Solution().permuteUnique([1,2,3,3])
print(res)


#solution using simple funtional approach
res=[]
def permuteUnique(nums,start, end):
    seen=set()
    if start == end:
        res.append(list(nums))
        return
    for i in range(start, end):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            permuteUnique(nums,start+1, end)
            nums[start], nums[i] = nums[i], nums[start]  
    return res
        

res=permuteUnique([1,2,3,3],0,len([1,2,3,3]))
print(res)
