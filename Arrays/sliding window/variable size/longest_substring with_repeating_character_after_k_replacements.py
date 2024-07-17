# Ref: https://www.youtube.com/watch?v=gqXU1UyA8pk&t=39s
# https://www.callicoder.com/longest-substring-with-same-letters-after-replacement/

# note : 
#  Given condition: The number of replacements in current window to obtain a substring with same letters should be less than or equal to k.
#  The number of replacements in current window can be computed as:
#  number of replacements in current window = length of current window - Maximum frequency of a character within the current window 
     
#  Violating condition for current window will be:
#  length of current window - Maximum frequency of a character within the current window  <= k

class Solution:
    def lengthofLongestSubstring(self,s, k): 
        sCount = {}
        maxFreq = 0  # max. repeating character in the current window
        max_size = 0
        left = 0
        for right in range(len(s)):
           sCount[s[right]]= sCount.get(s[right],0) + 1
           # maxRepeatCharCount = max(count.values())
           maxFreq = max(maxFreq ,sCount[s[right]])
           
           while (right-left+1)-maxFreq> k:
               sCount[s[left]]-= 1
               left+=1
               
           max_size = max(max_size,right-left+1)
        return max_size
                     
Solution().lengthofLongestSubstring("ababcbcca", 2)
