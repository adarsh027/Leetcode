#solution using class or object oriented approach as in leetcode site
class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                res.append(nums[:])
                print(nums)
                return
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        res = []
        backtrack(0, len(nums))
        return res
    

    
    
res=Solution().permute([1,2,3,4])
print(res)


#solution using simple funtional approach
res=[]
def backtrack(nums,start, end):
    if start == end:
        res.append(list(nums))
        return
    for i in range(start, end):
        print("swap: ", nums[start], nums[i])
        nums[start], nums[i] = nums[i], nums[start]
        print("nums After above swap", nums)
        
        backtrack(nums,start+1, end)
        print("Returned after recursive call")
        nums[start], nums[i] = nums[i], nums[start]  
        print("num after undoing swap", nums)
    return res

# backtrack([1,2,3], 0,3) nums after swap [1,2,3] 
# backtrack([1,2,3], 1,3) nums= [1,2,3] nums[1], nums[]

# backtrack([1,2,3], 0,3) nums= [1,2,3] return [1,2,3]
# backtrack([1,2,3], 0,3) nums= [1,2,3]
        

res=backtrack([1,2,3],0,len([1,2,3]))
print(res)


