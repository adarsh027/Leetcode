#Given   1<= nums[i] <= n, where n = length
# Ref: https://www.youtube.com/watch?v=kRrSeAZRD6E
# ref : https://www.youtube.com/watch?v=aMsSF1Il3IY&t=3s

# Note: suppose you have an array of lenght, n =5, then the values in the array can be from 1,2,...5. This means that if you subtract 1 from any value in nums, it is a valid index.
# 1. Compute index using each number in the arrays as index = abs(num) - 1
# 2. If the number corresponding to the index is greater than 0, then it will be their 1st appearance(Thus, can be used to build list of unique values). The number will be made as negative in the array.
# 3. Otherwise, the current number is a duplicate value and is hence added to the result.

class Solution:
    def find_duplicates(self, nums):
        res=[]
        for num in nums:
            index= abs(num) - 1 # Note: If you subtract 1 from any value in nums, it is valid index.
            if nums[index]>0:
                nums[index]= -nums[index]
            else:
                res.append(abs(num))
        return res
    
Solution().find_duplicates([4,3,2,7,8,2,3,1])

    

        







