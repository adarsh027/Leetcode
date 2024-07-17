# count no. of subarrays with given sum k
#solution 1: Naive approach
class Solution:
    def subArraySum(self,arr, k): 
       count = 0
       for i in range(len(arr)):# i represents start index of each subarray
               cur_sum=0
               for j in range(i,len(arr)): # j represents end index of each subarray
                   cur_sum= cur_sum+ arr[j]
                   if cur_sum==k:
                       count+= 1
                       print(i,j)
       return count

Solution().subArraySum([15,3,4,8,9,7,14,23],7)

#note:
# subarray_sum(i,j) = subarray_prefix_sum(j) - subarray_prefix_sum(i-1)
#here, i and j are index in the array
#solution 2: prefix sum approach
#note: prefix sum= sum upto the current element starting from index=0.
# refer submitted solution in leetcode
#ref: https://www.youtube.com/watch?v=fFVZt-6sgyo
#ref: https://www.youtube.com/watch?v=bWym1dWZhh0
#ref: https://www.youtube.com/watch?v=YkacnIOt2jM
class Solution:
    def subarraysum(self, arr,k):
        count=0 # count of subarrays having given sum
        cur_sum = 0
        prefix_sums={} #stores prefix sum and its corresponding count

        for i in range(len(arr)):
            cur_sum = cur_sum + arr[i]
            if cur_sum == k:
                count+=1
            if (cur_sum-k) in prefix_sums: # this means the we have found a subarray whose sum is k. The  start index of the subarray found will be the next index of the prefix sum found in the prefix_sums dictionary and the end index will be the current index of the iteration.
                count = count + prefix_sums[cur_sum-k]
                
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum,0)#building the prefix_sums dictionary using cur_sum

        return count

Solution().subarraysum([1,3,3,4,8,9,6,23,15],24)


# slight variation of the above
#Find start and end index of the subarray that sums to k
class Solution:
    def subarraysum(self, arr,k):
        cur_sum = 0
        prefix_sums={} #stores cur_sum and its corresponding index
        start=0
        end = -1

        for i in range(len(arr)):
            cur_sum = cur_sum + arr[i]      
            if cur_sum == k:
                start=0
                end = i
                break
            if cur_sum-k in prefix_sums: # this means the we have found a subarray whose sum is k. The  start index of the subarray found will be the next index of the prefix sum found in the prefix_sums dictionary and the end index will be the current index of the iteration.
               start= prefix_sums[cur_sum-k]+1
               end = i
               break
            prefix_sums[cur_sum] = i


        if end ==-1:
            print("not found")
        else:
            print(start,end)

Solution().subarraysum([1,3,3,4,8,9,6,23,15],24)         
            


