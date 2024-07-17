#Ref: https://www.youtube.com/watch?v=s4DPM8ct1pI
#Ref: https://www.youtube.com/watch?v=ApvI7QUqGzI&t=908s

# 1. Define left and right indexes
# 2. find mid index.
# 3. update left or left, depending upon if mid element is less than or greater than the target(value) being searched.
# 4. Repeat 2 and 3 until left<=right   
#Approach1: iterative way 
def search(arr, target): 
    left, right = 0, len(arr) - 1 
    
    while left <= right: 
        mid = (left + right) // 2 
        #mid = left + ((right-left)//2) # use this to avoid integer overflow 
        if target == arr[mid]: 
            return mid            # implies found with index = mid  
        elif target > arr[mid]: 
            left = mid + 1 
        else: 
            right = mid - 1

    return -1 # implies not found 

arr = [2, 3, 4, 10, 40] 

search(arr,10) 
 
#Approach2: recursive way 
def search(arr,left,right,target): 
    if left>right:
        return -1 # implies not found 
    
    mid = (left + right) // 2  
    if target == arr[mid]:  
        return mid
    elif target > arr[mid]:  
        return search(arr,mid+1,right,target)
    else:  
        return search(arr,left,mid-1,target)


arr = [2, 3, 4, 10, 40] 
left, right = 0, len(arr) - 1  
search(arr,left, right, 40)  



#Alternative recursive way(using only 2 arguments to the function)

def search(arr,target): 
    if len(arr)==0:
        return -1
    mid = (len(arr)-1 )// 2  
    print(arr,arr[mid])
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:  #search in right half
        x=search(arr[mid+1:],target)
        print(x,mid+1)
        if x>=0:
            return x + (mid+1)  
        else:
            return -1
    else:                     #search in left half
        return search(arr[:mid],target)

arr = [1,2,6,7,8,9,10,22]
search(arr,22)  




