#Ref : https://www.callicoder.com/longest-substring-with-k-distinct-characters/
# Ref: https://interviewnoodle.com/longest-substring-with-k-distinct-characters-in-python-sliding-window-pattern-coding-52e36fd79b96
#ref: https://www.youtube.com/watch?v=FsIyn_oe3eo&t=9s
#ref: https://www.youtube.com/watch?v=Lav6St0W_pQ

# Note: no. of unique characters in current window = length of dictionary "sCount"
class Solution:
    def lengthofLongestSubstring(self,s,k): 
        left = 0
        max_size = 0
        sCount= dict()
        for right in range(len(s)):
           sCount[s[right]]= sCount.get(s[right],0) + 1
           print(sCount)
           while len(sCount)>k:
               sCount[s[left]]-= 1
               if sCount.get(s[left])==0:
                   sCount.pop(s[left])
               left+=1
           if len(sCount)==k:
                 max_size = max(max_size,right-left+1)

        return max_size
                     
Solution().lengthofLongestSubstring("ababcbcca",2)

# brute force way
class Solution:
    def lengthofLongestSubstring(self,s,k): 
        max_size = 0
        res=""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j+1]
                if len(set(substring)) == k:# if the substring is unique
                   if (j-i+1) >  max_size: #using an if statement instead of using the max() function for computing max_size allows us to capture the resultant longest substring
                       max_size =  j-i+1
                       res= s[i : j+1]
        return max_size,res
                     
Solution().lengthofLongestSubstring("ababcbcca",2)