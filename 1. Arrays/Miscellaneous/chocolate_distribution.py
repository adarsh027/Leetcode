def minDiff(arr, n, k):
    arr.sort()
    min_diff = float('+inf')
    print(arr)
    for i in range(n - (k - 1)):
        print(arr[i:i+k],i,i+k)
        print(arr[i], arr[i + k - 1])
        diff= arr[i + k - 1] - arr[i]
        min_diff = min(min_diff,diff)
    return min_diff
        
        
minDiff([12, 4, 7, 9, 2, 23, 25, 41,],8, 3)

