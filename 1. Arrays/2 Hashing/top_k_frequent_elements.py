# ref:
# chatgpt
# https://www.youtube.com/watch?v=YPTqKIgVk-k (neetcode)
# https://www.youtube.com/watch?v=phNDYf1xzco (greg hogg)

# naive approach using hashmap and sorting
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies using Counter
        count = Counter(nums)
        
        # Step 2: Convert the hashmap to a list of tuples (element, frequency)
        freq_list = list(count.items())
        
        # Step 3: Sort the list by frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        # Step 4: Extract the top k elements
        return [item[0] for item in freq_list[:k]]

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))  # Output: [1, 2]

Time complexity: O(nlogn)
Space commplexity: O(n)



# Bucket sort approach
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies using Counter
        count = Counter(nums)
        
        # Step 2: Create a list of empty lists (buckets) of size len(nums) + 1
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        
        # Step 3: Fill the buckets
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Step 4: Collect the top k elements
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))  # Output: [1, 2]
 
### Explanation
# 1. **Count Frequencies**:
#    - Use `Counter` from the `collections` module to count the frequency of each element in `nums`.
#    - `count = Counter(nums)` gives us a dictionary where keys are elements and values are their frequencies.

# 2. **Create Buckets**:
#    - Create a list of empty lists (buckets) of size `len(nums) + 1` to store elements by their frequency.
#    - `buckets = [[] for _ in range(len(nums) + 1)]` creates the bucket list.

# 3. **Fill Buckets**:
#    - Iterate through the frequency dictionary and append each element to the bucket corresponding to its frequency.
#    - `buckets[freq].append(num)` fills the buckets with elements based on their frequency.

# 4. **Collect Top K Elements**:
#    - Iterate through the buckets from the end (highest frequency) to the beginning.
#    - Collect elements into the result list until `k` elements are collected.
#    - `for i in range(len(nums), 0, -1):` iterates from the highest frequency to the lowest.
#    - `result.append(num)` collects the top `k` elements.

### Overall Time Complexity : O(n)
# 1. **Counting Frequencies**:
#    - **Operation**: Count the frequency of each element.
#    - **Time Complexity**: O(n)

# 2. **Creating Buckets**:
#    - **Operation**: Create empty buckets.
#    - **Time Complexity**: O(n)

# 3. **Filling Buckets**:
#    - **Operation**: Place elements into corresponding buckets.
#    - **Time Complexity**: O(n)

# 4. **Collecting Top `k` Elements**:
#    - **Operation**: Collect the top `k` elements from the buckets.
#    - **Worst-Case Time Complexity**: O(n)
#    - **Average-Case Time Complexity**: O(k)

# *Overall Time Complexity**: O(n) + O(n) + O(n) + O(n) = O(n)  

### Overall Space Complexity : O(n)
# - **Frequency Dictionary**: O(n)
#   - Stores each unique element and its frequency.
# - **Buckets**: O(n)
#   - `n + 1` buckets, each potentially holding multiple elements, but the total number of elements is `n`.
# - **Result List**: O(k)
#   - Stores the top `k` frequent elements.

# **Overall Space Complexity**: O(n) + O(n) + O(k) = O(n)   (since k<=n , the dominant term is O(n))

# Heap (min heap) approach
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies using Counter
        count = Counter(nums)
        
        # Step 2: Use a heap to keep the top k elements
        heap = []
        for num, freq in count.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        
        # Step 3: Extract the elements from the heap
        return [num for freq,num in heap]

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))  # Output: [1, 2]

### Overall Time Complexity : O(nlog k)

# 1. **Counting Frequencies**: O(n)
# 2. **Building the Heap**: O(nlog k)
# 3. **Extracting Top k Elements**: O(klog k)

# Thus, the overall time complexity is:

#  O(n) + O(nlog k) + O(klog k) = O(nlog k) (Since the dominant term here is O(nlog k), especially when n is significantly larger than n)

### Overall Space Complexity**: O(n + k)

# 1. **Frequency Dictionary**:
#    - **Space Complexity**: O(n)
#    - The dictionary stores up to n unique elements with their frequencies.

# 2. **Heap**:
#    - **Space Complexity**: O(k)
#    - The heap stores the top k frequent elements.

# Even though k is typically much smaller than n, we still account for it separately to provide a complete analysis. Thus, the overall space complexity is:
# O(n) + O(k) = O(n + k)
# Note: We can choose to neglect O(k) in the above equation as k is typically much smaller than n. In so that case th overall space compllexity will just be O(n).


# The bucket sort approach is more efficient than the heap-based approach. 
# This approach leverages the properties of bucket sort to efficiently find the top `k` frequent elements.
