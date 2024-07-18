'''
# the below content explains min-heap and max-heap in detail(source: chatgpt)
### Min-Heap

#### Definition
A min-heap is a complete binary tree where the value at each node is less than or equal to the values of its children. The smallest 
value is at the root of the tree.

#### Properties
- **Complete Binary Tree**: All levels are completely filled except possibly for the last level, which is filled from left to right.
- **Heap Property**: For any given node `i`, the value of `i` is less than or equal to the values of its children.

#### Example

Consider the following array representation of a min-heap:
[1, 3, 6, 5, 9, 8]


The corresponding binary tree is:

      1
     / \
    3   6
   / \ / \
  5  9 8


1. **Root Element**: The root is `1`, which is the smallest element.
2. **Heap Property**: Every parent node is smaller than its children (e.g., `1` is smaller than `3` and `6`, `3` is smaller than `5` and `9`, `6` is smaller than `8`).

#### Operations

1. **Insertion**:
   - Add the new element at the end of the heap.
   - "Bubble up" the new element to restore the heap property.

2. **Deletion (Extract Min)**:
   - Remove the root element.
   - Move the last element to the root.
   - "Bubble down" this element to restore the heap property.

#### Example: Inserting `2` into the Min-Heap `[1, 3, 6, 5, 9, 8]`
1. Add `2` at the end:
   [1, 3, 6, 5, 9, 8, 2]

2. Bubble up `2`:
   - Swap `2` with `6`:
     [1, 3, 2, 5, 9, 8, 6]
  
   - Now, `2` is in the correct position, and the heap property is restored.

### Max-Heap

#### Definition
A max-heap is a complete binary tree where the value at each node is greater than or equal to the values of its children. The largest value is at the root of the tree.

#### Properties
- **Complete Binary Tree**: All levels are completely filled except possibly for the last level, which is filled from left to right.
- **Heap Property**: For any given node `i`, the value of `i` is greater than or equal to the values of its children.

#### Example

Consider the following array representation of a max-heap:

[9, 5, 6, 2, 3]


The corresponding binary tree is:

      9
     / \
    5   6
   / \
  2   3


1. **Root Element**: The root is `9`, which is the largest element.
2. **Heap Property**: Every parent node is larger than its children (e.g., `9` is larger than `5` and `6`, `5` is larger than `2` and `3`).

#### Operations

1. **Insertion**:
   - Add the new element at the end of the heap.
   - "Bubble up" the new element to restore the heap property.

2. **Deletion (Extract Max)**:
   - Remove the root element.
   - Move the last element to the root.
   - "Bubble down" this element to restore the heap property.

#### Example: Inserting `7` into the Max-Heap `[9, 5, 6, 2, 3]`
1. Add `7` at the end:
   [9, 5, 6, 2, 3, 7]

2. Bubble up `7`:
   - Swap `7` with `6`:
     [9, 5, 7, 2, 3, 6]

   - Now, `7` is in the correct position, and the heap property is restored.

### Python `heapq` Module

- The `heapq` module in Python provides an implementation of the min-heap. For max-heap functionality, you can store negative values to simulate a max-heap.

#### Key Functions

1. **`heapify`**: Converts a list into a heap, in-place, in linear time.

    import heapq
    lst = [1, 3, 6, 5, 9, 8]
    heapq.heapify(lst)


2. **`heappush`**:  Adds an element to the heap, maintaining the heap property.
   
    heapq.heappush(lst, 2)


3. **`heappop`**:  Removes and returns the smallest element from the heap.
   
    smallest = heapq.heappop(lst)


4. **`heappushpop`**: Pushes a new item on the heap and then pops and returns the smallest item from the heap.

    smallest = heapq.heappushpop(lst, 4)
 

### Example Usage of Min-Heap and Max-Heap in Python

#### Min-Heap Code
import heapq

# Create a min-heap
min_heap = [1, 3, 6, 5, 9, 8]
heapq.heapify(min_heap)
print("Min-Heap:", min_heap)

# Insert a new element
heapq.heappush(min_heap, 2)
print("After Inserting 2:", min_heap)

# Extract the smallest element
smallest = heapq.heappop(min_heap)
print("Extracted Smallest Element:", smallest)
print("After Extracting:", min_heap)
```

#### Max-Heap Code (Using Negation)
import heapq

# Create a max-heap using negation
max_heap = [-1, -3, -6, -5, -9, -8]
heapq.heapify(max_heap)
print("Max-Heap (Negated):", max_heap)

# Insert a new element
heapq.heappush(max_heap, -2)
print("After Inserting -2:", max_heap)

# Extract the largest element
largest = -heapq.heappop(max_heap)
print("Extracted Largest Element:", largest)
print("After Extracting:", [-x for x in max_heap])
```

### Conclusion

- **Min-Heap**: Root contains the smallest element. Every parent node is smaller than its children.
- **Max-Heap**: Root contains the largest element. Every parent node is larger than its children.
- **`heapq` Module**: Provides min-heap functionality. For max-heap, store negative values.
- **Operations**: `heapify`, `heappush`, `heappop`, and `heappushpop` maintain the heap property during modifications.

'''