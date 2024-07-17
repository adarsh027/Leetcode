# Version 1: O(2N) complexity
def find_second_largest(arr):  
    # find the maximum
    largest = float('-inf') # Alternatively, we can also intiilize this to the 1st element of the array
    for i in range(len(arr)):  
        if arr[i] > largest:  
            largest = arr[i]  
    print(largest) 
    
    # find the second maximum
    second_largest = float('-inf') 
    for i in range(len(arr)):
          if arr[i] > second_largest and arr[i] < largest:
              second_largest=arr[i]

    if second_largest == float('-inf'):
        return "All elements are the same(ie, no second distinct largest element)"
    return second_largest

print(find_second_largest([334,334,334,2,2]))

# Version 2: O(N) complexity
# Note: If we had taken 
# largest = second_largest = arr[0], 
# then the solution won't give accurate result in the case where 1st element in the array is the largest.

def find_second_largest(arr):
    if len(arr) < 2:
        return "Array does not have enough elements to have a second largest"

    # Initialize the largest and second largest to negative infinity
    largest = second_largest = float('-inf')

    # Note: we can also solve the problem by initializing largest to the first element and second largest to negative infinity, as shown below.
    # largest = arr[0]
    # second_largest = float('-inf')

    # Iterate through the array
    for number in arr:
        if number > largest:
            # Update second largest to be the former largest
            second_largest = largest
            # Update largest to the current number
            largest = number
        elif number > second_largest and number < largest:
            # Update second largest to the current number
            second_largest = number

    # Check if a valid second largest was found
    if second_largest == float('-inf'):
        return "All elements are the same(ie, no second distinct largest element)"
    return second_largest

print(find_second_largest([334,334,2,2]))



