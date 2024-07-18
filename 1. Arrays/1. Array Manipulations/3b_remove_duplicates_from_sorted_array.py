# approach 1: Here, the immediate previous element(used for comparing with curent array element) is referred using the loop iteration variable 'i' as nums[left-1]
class Solution:
    def removeDuplicates(self, nums):
        left = 1 # Initialize the left pointer. It is used to place any unique element found in the array at the beginning of the array.
        # Note: As the array is sorted, left pointer is initilized to 1 as the 1st array element(at index 0) is considered as unique element. So we need to place the next unique element at index 1 and so on.
        # Note: As the array is sorted, the next unique element can be found by comparing the current element to the immediate previous elemnt while iterating through the array.
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # if a unique element is found in the array, place it at the left index and increment left.
                nums[left] = nums[i]
                left += 1
        
        return left

Solution().removeDuplicates([0,0,0])
Solution().removeDuplicates([0,0,0,1,1,1,2,2,3,3,4])


# approach 2: Here, the immediate previous element(used for comparing with current element) is referred using the left pointer 'left' as nums[left-1]
class Solution:
    def removeDuplicates(self, nums):
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[left-1]:
                nums[left] = nums[i]
                left+=1
        return left
        