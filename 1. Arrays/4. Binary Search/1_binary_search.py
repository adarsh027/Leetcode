list1 = [2, 3, 4, 10, 40] 

#Approach1: iterative way 
def find_element(list1, value): 
    left, right = 0, len(list1) - 1 

    while left <= right: 

        middle = (left + right) // 2 
        #middle = left + ((right-left)//2) # use this to avoid integer overflow 
        if list1[middle] == value: 
            return True             # implies found the element
        elif list1[middle] < value: 
            left = middle + 1     # consider right portion of middle
        else: 
            right = middle - 1    # consider left portion of middle

    return False # implies not found 


find_element(list1,10) 

 
#Approach2: recursive way 

def find_element(list1,value): 
    left, right = 0, len(list1) - 1  

    while left <= right:  
        middle = (left + right) // 2  

        if list1[middle] == value:  
            return True                                 # implies found the element
        elif list1[middle] < value:  
            return find_element(list1[middle+1:],value) # consider right portion of middle
        else:  
            return find_element(list1[:middle],value)   # consider left portion of middle

    return False # implies not found  

find_element(list1,10)  

