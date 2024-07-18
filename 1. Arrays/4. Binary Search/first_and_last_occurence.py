#ref: https://www.youtube.com/watch?v=4sQL7R5ySUU
class Solution:
    def searchRange(self, nums, target):
        leftmost=self.binarySearch(nums,target,True)# find the leftmost index of target
        rightmost=self.binarySearch(nums,target,False) # find the rightmost index of target
        return [leftmost,rightmost]
    
        def binarySearch(nums, target,leftbias):
            left, right = 0, len(nums) - 1
            index=-1
            while left <= right:
                mid = (left + right) // 2
                if target==nums[mid]:
                    index = mid
                    if leftbias:        # If we are finding the leftmost index
                       right= mid - 1
                    else:               # If we are finding the rightmost index
                        left=mid+1
                elif  target> nums[mid]:
                    left = mid + 1 
                else:
                    right= mid - 1

            return index


#alternatively, using 2 functions exclusively for finding leftmost and rightmost index of target
class Solution:
    def searchRange(self, nums, target):
        
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            index=-1
            while left <= right:
                mid = (left + right) // 2
                if target==nums[mid]:
                    index = mid
                    right= mid - 1
                elif  target> nums[mid]:
                    left = mid + 1 
                else:
                    right= mid - 1

            return index

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            index=-1
            while left <= right:
                mid = (left+ right) // 2
                if target==nums[mid]:
                    index = mid
                    left= mid + 1
                elif  target> nums[mid]:
                    left = mid + 1 
                else:
                    right= mid - 1

            return index

        start = binarySearchLeft(nums, target)
        end= binarySearchRight(nums, target)
        
        return [start, end]


