#version 1: Taking the 1st element of the array as largest

# Advantage: There is one less comparison involved, which is a slight optimization.
def find_largest(arr):
    # Handle the case when the array is empty
    if not arr:
        return "Array is empty"
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

print(find_largest([3,3,3,3,334,25,23,25,56,67,70]))

#version 2: Assuming a very small number as the largest.(Note: Taking negative inifnity as the initial value 
# for the largest number ensures that any number in the array will be larger than the initial value.)

# Advantage: No need to handle empty array. If the array is empty, negative infinity, ie, float('-inf'), is returned.
def find_largest(arr): 
    largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest