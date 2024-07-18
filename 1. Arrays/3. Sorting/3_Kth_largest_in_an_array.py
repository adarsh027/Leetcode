#method 1: sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_index = len(nums) - k
        nums.sort()
        return nums[kth_index]
# Time Complexity: O(nlogn)
# Space Complexity: O(n), due to the due to the auxiliary arrays used during the merging phase of Timsort algorithm.

### What is Timsort?
# Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data. Timsort is the default sorting algorithm used in 
# Python's built-in `sort()` method and `sorted()` function.

### How Timsort Works
# 1. **Divide the Array into Runs**:
#    - Timsort splits the array into small segments called runs. Each run is sorted individually using insertion sort, which is efficient for small segments.

# 2. **Merge Runs Using Merge Sort**:
#    - The sorted runs are then merged using a process similar to merge sort. This is done iteratively until the entire array is merged into a single sorted array.
#    - Timsort maintains two auxiliary arrays for merging runs. 


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


# Time Complexity: On average O(n), but in the worst case O(n ^2). However, the average case is more typical due to the random pivot selection.
# Space Complexity: O(1)    

# using min-heap
import heapq

class Solution:
    def findKthLargest(self, nums) :
        # Create a min-heap with the first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Iterate through the remaining elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        
        # The root of the heap is the Kth largest element
        return heap[0]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))  # Output: 5

# Time Complexity: O(nlogk)
# Space Complexity: O(k) for storing the heap.
    
# Time complexity explanation:
# 1. Initial Heap Construction: Building a heap with the first k elements takes O(k) time.
# 2. Heap Operations for Remaining Elements:
# Each of the remaining n - k elements might require an insertion and removal operation on the heap, each of which takes O(logk) time.
# Total time for heap operations: 
# (n−k) × O(logk).
# 3. Therefore, the total time complexity is:
# O(k) + (n−k) × O(logk)
# Since O(k) is dominated by (n−k) × O(logk) for large n, the overall time complexity simplifies to: O(nlogk)

# Quickselect vs heap approach

# Conclusion
# Both approaches are efficient and useful. The Quickselect algorithm is usually faster and uses less additional memory, 
# making it an excellent choice for finding the k-th largest element. However, the heap approach is simpler to implement and 
# understand, and it provides more predictable performance across different scenarios.




