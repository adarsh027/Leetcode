#method 1: sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_index = len(nums) - k
        nums.sort()
        return nums[kth_index]


# method 2: quickselect logic(based upon quicksort)
#ref: https://www.youtube.com/watch?v=XEmy13g1Qxc
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_index = len(nums) - k
        def partition(start, end):
            pivot = nums[end]
            l, r = start, end-1
            
            while True:
                while l <= r and nums[l] <= pivot:
                    l += 1
                while l <= r and nums[r] >= pivot:
                    r -= 1

                if l<=r:
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    break
            nums[l], nums[end] = nums[end], nums[l]
            return l
        def quick_select(start,end,kth_index):
                    if start==end:
                        return nums[start]
                    
                    pi = partition(start,end)
                    
                    if pi == kth_index:
                        return nums[pi]
                    elif kth_index<pi:
                        return quick_select(start,pi-1, kth_index)
                    else:
                        return quick_select(pi+1, end, kth_index)
                        
                
        return quick_select(0, len(nums) - 1, kth_index)

