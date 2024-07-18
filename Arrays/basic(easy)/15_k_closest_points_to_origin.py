# ref:
# chatgpt
# https://www.youtube.com/watch?v=rI2EBUEMfTk (neetcode)
# https://www.youtube.com/watch?v=IGRUukbD6p8 (greg hogg)

# min heap approach
import heapq

class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            # Calculate the Euclidean distance (squared) and store it with the point
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))  # Append distance and point to the heap list
        
        # Transform the list into a heap in-place
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            # Pop the smallest distance from the heap and get the point
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))  # Add the point to the result list
        return res

# Example usage:
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
solution = Solution()
print(solution.kClosest(points, k))  # Output: [[0, 1], [-2, 2]]

# max heap approach
import heapq

class Solution:
    def kClosest(self, points, k):
        maxHeap = []
        for x, y in points:
            # Calculate the Euclidean distance (squared) and negate it
            d = (x ** 2) + (y ** 2)
            if len(maxHeap) < k:
                # Push the negated distance and point to the heap
                heapq.heappush(maxHeap, (-d, x, y))
            else:
                # Push the new point and pop the largest distance
                heapq.heappushpop(maxHeap, (-d, x, y))

        # Extract the points from the heap and return them
        return [(x, y) for d, x, y in maxHeap]
    
# Example usage:
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
solution = Solution()
print(solution.kClosest(points, k))  # Output: [(-2, 2), (0, 1)]
# Note: Yes, it is alright for the two approaches to return the results in different orders. The problem of finding the k closest points to the origin does not specify the order in which the closest points should be returned, only 
# that the k closest points should be included in the result.


### Explanation

#### Min Heap Approach

# 1. **Calculating Distances and Building the Heap**:
#     - For each point `(x, y)`, calculate the squared distance from the origin: `(x ** 2) + (y ** 2)`.
#     - Append a tuple `(dist, x, y)` to the `minHeap` list.
#     - Use `heapq.heapify(minHeap)` to transform the list into a heap in-place.

# 2. **Extracting the k Closest Points**:
#     - Initialize an empty list `res` to store the result.
#     - Use a loop to pop the smallest element from the heap `k` times.
#     - For each pop, append the point `(x, y)` to `res`.
#     - Return `res`.

# #### Max Heap Approach

# 1. **Calculating Distances and Building the Heap**:
#     - For each point `(x, y)`, calculate the squared distance from the origin: `(x ** 2) + (y ** 2)`.
#     - Negate the distance to simulate a max heap using Python's min heap.
#     - If the heap size is less than `k`, push the tuple `(-d, x, y)` to `maxHeap`.
#     - If the heap size is equal to `k`, use `heapq.heappushpop(maxHeap, (-d, x, y))` to push the new point and pop the largest distance from the heap.

# 2. **Extracting the k Closest Points**:
#     - Use a list comprehension to extract the points from `maxHeap`.
#     - Return the list of points.

# ### Functions Explained

# 1. **`heapify`**:
#     - `heapq.heapify(minHeap)`: Transforms a list into a heap in-place. This operation rearranges the elements of the list to satisfy the heap property, where the smallest element is at the root. The time complexity is \(O(n)\).

# 2. **`heappush`**:
#     - `heapq.heappush(maxHeap, (-d, x, y))`: Adds an element to the heap while maintaining the heap property. The time complexity is O(log n).

# 3. **`heappop`**:
#     - `heapq.heappop(minHeap)`: Removes and returns the smallest element from the heap. The heap property is maintained after the pop operation. The time complexity is O(log n).

# 4. **`heappushpop`**:
#     - `heapq.heappushpop(maxHeap, (-d, x, y))`: Pushes a new element onto the heap and pops the smallest element in a single atomic operation. This is more efficient than pushing and then popping separately if both operations are needed. The time complexity is O(log n).

# ### Comparison of Approaches

# - **Min Heap Approach**:
#   - More intuitive as it directly uses the min heap properties to extract the k smallest distances.
#   - Simpler and easier to understand.
#   - Time complexity: (O(n + k log n)), where n is the number of points and  k is the number of closest points to extract.
#     Explantion for time complexity: heapify is O(n) and extracting k elements is O(k log n)
#   - Space Complexity:
    # (i) Heap Storage: We store all n points in the heap.
    # (ii)Result Storage: We store k points in the result list.
    # (iii)Therefore, the total space used is O(n) + O(k) ≈ O(n) because n is typically much larger than k.

# - **Max Heap Approach**:
#   - Efficient when `k` is much smaller than `n`.
#   - Maintains a heap of size `k`, making the push-pop operation O(log k).
#   - Time complexity: O(n log k), where n is the number of points and  k is the number of closest points to extract.
#     Explantion for time complexity: each insertion and removal of points on the heap of size k is O(log k) and there are total n points.
#   -Space Complexity:
    #  (i) Heap Storage: We maintain a max-heap of size k to store the closest points.
    # (ii) Result Storage: We store k points in the result list.
    # (iii) Therefore, the total space used is O(k) + O(k) = O(2k) = O(k).

# Both approaches are efficient, and the choice depends on the context and specific requirements. For small values of `k`, the max heap approach may be more efficient. For a straightforward solution, the min heap approach is easier to implement and understand.