#two-pointer approach
def reverseArray(arr):
    i=0
    j= len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

reverseArray([1,2,3,4])


# The loop iterates for n/2 times and in each iteration, we swap two elements. Thus,
# time-complexity is O(n).The space complexity is O(1).