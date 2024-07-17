# approach 1: Using count variable     (source for approach 1 code: chatgpt)
# Invloves comparing cuurent array element with immediate previous element(referred to using the loop iteration variable i as nums[i-1])
class Solution:
    def removeDuplicates(self, nums):
        left = 1  # Start `left` at 1 because the first element is always included.
        count = 1  # Start counting from 1 because the first element is already seen once.
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1  # Increment the count if the current element is the same as the previous.
            else:
                count = 1  # Reset the count if a new element is encountered.

            if count <= 2:
                nums[left] = nums[i]
                left += 1  # Move the left pointer only if the count is less than or equal to 2.
        
        return left



#ref: https://www.youtube.com/watch?v=OZaADxYTfD4
#ref: https://www.youtube.com/watch?v=4IYQYJhi1LA

# approach 2: Without using count variable
# Involves comparing current array element with two places previous elment(referred to using the left pointer 'left' as nums[left=2])

class Solution:
    def removeDuplicates(self, nums):
        left = 2  # Initialize the left pointer. It is used to place any unique element found in the array at the beginning of the array.
         # Note: Taking left=2 since the values at index=0 and index= 1 will always be present regardless of the whatevr value comes at index=2.

        for i in range(2,len(nums)):
            if nums[i]!= nums[left- 2]:
                nums[left] = nums[i]
                left += 1  
        return left
    
Solution().removeDuplicates([0,0,0,1,1,1,1,2,3,3])
Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])

