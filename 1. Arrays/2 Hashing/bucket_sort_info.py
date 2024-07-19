'''
### Bucket Sort Algorithm (sourcce : chatgpt)

Bucket sort is a sorting algorithm that distributes elements into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort. Finally, the sorted buckets are concatenated to produce the final sorted array.

### Steps Involved

1. **Create Buckets**: Divide the range of the data into a number of buckets.
2. **Distribute Elements**: Distribute the elements into the appropriate buckets based on their values.
3. **Sort Buckets**: Sort each bucket individually.
4. **Concatenate Buckets**: Concatenate the sorted buckets to get the final sorted array.

### Example

Let's use the following array as an example:

- **Input**: `[0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]`

### Steps

1. **Create Buckets**:
   - Determine the number of buckets. For simplicity, we can use 10 buckets for values in the range [0, 1).
   - Initial buckets: `[[], [], [], [], [], [], [], [], [], []]`

2. **Distribute Elements**:
   - Distribute the elements into the appropriate buckets based on their values.
   - For example, the element 0.42 goes into the bucket 4:
     bucket[int(0.42 * 10)] = bucket[4]
     Similarly, the element 0.47 also goes into the bucket 4.
   - Updated buckets after distributing elements:
     - Bucket 2: `[0.23, 0.25]`
     - Bucket 3: `[0.32]`
     - Bucket 4: `[0.42, 0.47]`
     - Bucket 5: `[0.52, 0.51]`

3. **Sort Buckets**:
   - Sort each bucket individually. We can use any sorting algorithm for this step. For simplicity, we'll use Python's built-in `sorted()` function.
   - Sorted buckets:
     - Bucket 2: `[0.23, 0.25]`
     - Bucket 3: `[0.32]`
     - Bucket 4: `[0.42, 0.47]`
     - Bucket 5: `[0.51, 0.52]`

4. **Concatenate Buckets**:
   - Concatenate the sorted buckets to get the final sorted array.
   - Final sorted array: `[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]`

### Python Code

Here's the Python code implementing the general bucket sort algorithm:

def bucket_sort(arr):
    # Step 1: Create buckets
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]
    
    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)
    
    # Step 3: Sort each bucket
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])
    
    # Step 4: Concatenate buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

# Example usage:
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)  # Output: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]


### Explanation

1. **Create Buckets**:
   - We create a list of empty buckets. Here we use 10 buckets for simplicity.

2. **Distribute Elements**:
   - Each element in the input array is placed into a bucket based on its value. The index of the bucket is determined by multiplying the element by the number of buckets and converting it to an integer.

3. **Sort Buckets**:
   - Each bucket is sorted individually. We can use any sorting algorithm for this step. In the code, we use Python's built-in `sorted()` function.

4. **Concatenate Buckets**:
   - The sorted buckets are concatenated to form the final sorted array.

### Time Complexity

- **Best Case**: \(O(n + k)\)
- **Average Case**: \(O(n + k)\)
- **Worst Case**: \(O(n^2)\)

Here, \(n\) is the number of elements in the array, and \(k\) is the number of buckets. The worst-case complexity occurs when all elements are placed into a single bucket.

### Space Complexity

- **Space Complexity**: \(O(n + k)\)
  - \(O(n)\) for the input array and temporary storage.
  - \(O(k)\) for the buckets.

### Use Cases

Bucket sort is useful when:
- The input is uniformly distributed over a range.
- We need a stable sorting algorithm.

### Conclusion
Bucket sort is an efficient sorting algorithm for specific scenarios where the input data is uniformly distributed. It works by dividing the data into buckets, sorting each bucket individually, and then concatenating the sorted buckets to produce the final sorted array.

# Note:
# While traditional/general bucket sort algorithm can have a worst-case complexity of O(n^2), the specific bucket-like approach for solving the 
# "Top K Frequent Elements" problem leverages frequency counting and efficient bucket distribution, leading to an overall time 
# complexity of O(n). This is due to the linear nature of the counting and bucket creation steps, as well as the practical O(k))
# extraction step for collecting the top k elements.











'''