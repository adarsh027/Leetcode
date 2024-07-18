#ref: https://leetcode.com/problems/find-peak-element/solutions/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search/
# Case 1 : mid lies on the right of our result peak ( Observation : Our peak element search space is leftside )
# Case 2 : mid is equal to the peak element ( Observation : mid element is greater than its neighbors )
# Case 3 : mid lies on the left. ( Observation : Our peak element search space is rightside )

# equivalent python code for the java code given on the above leetcode link

def findPeakElement(nums):
    
    n=len(nums)
    if n == 1 :
        return 0
    
    # check if 0th/n-1th index is the peak element
    if nums[0]>nums[1]:
            return 0
    if(nums[n-1] > nums[n-2]) :
        return n-1
    
    # search in the remaining array
    left = 1
    right = len(nums) - 2
    while left <= right:
        mid = (left + right) // 2
        if(nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]): # if mid == peak ( case 2 )
            return mid
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:  # upward slope and search space right side ( case 3)
            left= mid + 1
        elif mid < len(nums) - 1 and nums[mid] < nums[mid - 1]:  # downward slope and search space left side ( case 1)
            right= mid - 1


findPeakElement([1,2,1,3,5,6,4])