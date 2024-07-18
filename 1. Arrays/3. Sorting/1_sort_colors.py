#logic
# 1. Iterate and find the count of 0s,1s and 2s in the array.
# 2 Based upon the counts of 0,1 and 2, place 0s,1s and 2s in the array.
class Solution:
    def sortColors(self, nums):
        count0=count1=count2=0
        for num in nums:
            print(num)
            if num==0:
                count0+=1
                print(count0)
            if num==1:
                count1+=1
            if num==2:
                count2+=1
        print(count0,count1,count2)
        i=0        
        while count0>0:
            nums[i]=0
            i=i+1
            count0=count0 - 1
        while count1>0:
            nums[i]=1
            i=i+1
            count1=count1-1
        while count2>0:
            nums[i]=2
            i=i+1
            count2=count2-1
        return nums
# note:we increment i in all the 3 while loops
Solution().sortColors([2,0,2,1,1,0,1,1])

#optimised solution with only 1 single pass
#Ref : https://www.enjoyalgorithms.com/blog/sort-an-array-of-0s-1s-and-2s 
#Ref: https://www.youtube.com/watch?v=4xbWSRZHqac&t=254s
#ref: https://www.youtube.com/watch?v=sEQk8xgjx64
class Solution:
    def sortColors(self, nums):
        left, mid, right=  0, 0, len(nums)-1
        
        # mid pointer is for iterating through the array to find any 0s and 2s.
        # left pointer is for placing any 0s to the left via swapping with mid pointer value.
        # right pointer is for placing any 2s to the right via swapping with mid pointer value.
        # Note: don't increment mid pointer when swapping with the right pointer.
        
        while mid <= right:
            if nums[mid] == 0:
                nums[mid],nums[left] = nums[left], nums[mid]
                left += 1
                mid+=1

            elif nums[mid]==2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right-=1 # note: we don't incemrent the mid pointer becuase if the swapping is between 2 and 0, then that 0 would be at the middle portion, which means that if we increment mid pointer, then the processing of 0 will be skipped by the mid pointer and the 0 will remain in the middle portion of the array. By not incrementing mid pointer, the mid pointer will process the 0 again and bring it to the left portion of the array.
            else:        # ie, when nums[mid]==1
                mid+=1
        return nums

Solution().sortColors([2,0,2,1,1,0,1,1])





















