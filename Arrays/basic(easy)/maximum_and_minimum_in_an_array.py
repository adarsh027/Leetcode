def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    for i in range(1,len(arr)): 
        minimum=min(minimum,arr[i])
        maximum=max(maximum,arr[i])
    return minimum, maximum

find_min_max([2,45,3,34,3])

