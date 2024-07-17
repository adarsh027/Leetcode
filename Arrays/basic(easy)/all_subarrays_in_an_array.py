# print all non-empty sub arrays and its count
# Note: no of non-empty subarrays in an array of length n = n*(n+1)/2
# note: no. of subsets in an array is diferent than no. of subarrays in an array.
# note: no. of subsets in an array of length n = 2^n (ie, 2 to the power of n)
class Solution:
    def sub_arrays(self,arr): 
       lst= []
       for i in range(len(arr)):# i represents start index of each subarray
            for j in range(i,len(arr)):# j represents end index of each subarray
                lst.append(arr[i:j+1])
                print(arr[i:j+1])# Here, j+1 means that jth index element is considered for each subarray
       print(len(lst),lst)

Solution().sub_arrays([15,2,4])         

# Equivalent code using only while loops
class Solution:
    def sub_arrays(self,arr): 
       i=0
       while i<len(arr):
           j=i
           while j<len(arr):
               print(arr[i:j+1])
               j+=1
           i+=1
        
Solution().sub_arrays([15,2,4,8,9,5,10,23])

# Obtain list of all subarrays, including the empty array[]
class Solution:
    def sub_arrays(self,arr): 
       lst= [[]]     # using a list initialized with an empty list in order to include an empty list in the output(ie, list of subarrays)
       for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                lst.append(arr[i:j+1])
       return lst

           
Solution().sub_arrays([15,2,4])

# To display each subarray element individually, use an additional loop 
class Solution:
    def sub_arrays(self,arr): 
       for i in range(len(arr)):
            for j in range(i,len(arr)):
                for k in range(i,j+1):
                    print(arr[k])
                print()
           
Solution().sub_arrays([15,2,4])




