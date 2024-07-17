#Ref: https://leetcode.com/problems/next-greater-element-i/solutions/824654/python-3-94-64-faster-used-stack-and-dictionary-explanation-added/

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        res = []
        mapping = {}
        
        for num in nums2:
            while(stack and num > stack[-1]):
                popped = stack.pop()
                mapping[popped] = num
            stack.append(num)
        
        while stack:
            mapping[stack.pop()] = -1
             
        for n in nums1:
            res.append(mapping[n])
 
        return res

