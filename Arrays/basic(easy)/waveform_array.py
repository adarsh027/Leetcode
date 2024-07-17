#logic: think of them in triplets such that the every even indexed value is greeater
#than adjacent odd indexed values.Thus for every even indexed i, the following 2 conditions
#should be met:
# 1. arr[i-1]<arr[i]
# 2. arr[i]>arr[i+1]
#note: waveform can also be formed by having every odd indexed value greater
# than adjacent even indexed values. In such case, you will use the range function() as
# range(1,len(arr),2) to loop through all odd indexed values

    
#Ref: https://www.enjoyalgorithms.com/blog/sort-an-array-in-a-waveform
# https://www.geeksforgeeks.org/sort-array-wave-form-2/

#using sorting and using even indexing to swap subsequent adjacent pairs(ie, non-overlapping adjacent pairs)
class Solution:
    def convertToWave(self, arr):
        arr.sort()
        for i in range(0,len(arr)-1,2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
    
Solution().convertToWave([ 5, 1, 3, 2, 4 ])

#using even indexing and comparing with its adjacent left and right neighbours
class Solution:
    def convertToWave(self, arr):
        for i in range(0,len(arr)-1,2):
            
            # If current even element is smaller than immediate left/previous
            if i>0 and arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                
            # If current even element is smaller than immediate next/right
            if i< len(arr)-1 and arr[i]<arr[i+1]: # index=0 gets considered here
                 arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
    
Solution().convertToWave([ 5, 1, 3, 2, 4 ])











    
    
