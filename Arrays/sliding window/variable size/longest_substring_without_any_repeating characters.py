#using a dictionary with variable sized sliding window concept

#Ref: https://www.callicoder.com/longest-substring-without-repeating-characters/
# Note: The number of unique characters in a window can never be greater than the length of the window.
# The no. of unique characters can be either less than window size or equal to the window size.

# Note: no. of unique characters in current window = length of dictionary "sCount"
# Note: when the no. unique characters in a window is equal to the window size, it implies that all the characters in the window are unique, without any repeating characters.
class Solution:
    def lengthofLongestSubstring(self,s): 
        left = 0
        max_size = 0
        sCount= dict()
        for right in range(len(s)):
           sCount[s[right]]= sCount.get(s[right],0) + 1
           print(sCount)
           while len(sCount)< (right-left+1):
               sCount[s[left]]-= 1
               if sCount.get(s[left])==0:
                   sCount.pop(s[left])
               left+=1
           if len(sCount)==(right-left+1): # Note: when the no. unique characters in a window is equal to the window size, it implies that all the characters in the window are unique, without any repeating characters.
                 max_size = max(max_size,right-left+1)

        return max_size,s[left:right+1]
                     
Solution().lengthofLongestSubstring("ababcbcca")


# Brute force apprach
#ref:https://codedamn.com/news/python/find-longest-substring-without-repeating-characters-in-python
#time complexity
# The nested loop to collect each substring: O(N*N) = O(N^2).
# Logic to check one substring has all unique characters: O(N).
# Logic to check each substring having non repeating characters: O(N*N^2) = O(N^3).
class Solution:
    def lengthofLongestSubstring(self,s): 
        max_size = 0
        res=""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j+1]
                if len(set(substring)) == len(substring):# if the substring is unique
                    if len(substring) > max_size:
                        res = substring
                        max_size = len(substring)
                
        return res, max_size
                     
Solution().lengthofLongestSubstring("ababcbccabcdefghaauvxyzabcdefmnop")



# using a set
#ref: https://www.youtube.com/watch?v=wiGpQwVHdE0
#ref: https://www.youtube.com/watch?v=RoRRpF3eCH4
class Solution:
    def lengthofLongestSubstring(self,s): 
        left = 0
        max_size = 0
        seen= set()
        for right in range(len(s)):
            newChar = s[right]
            while newChar in seen:
               seen.remove(s[left])
               left+=1
            seen.add(newChar)
            max_size = max(max_size,right-left+1)

        return max_size,s[left:right+1]
                     
Solution().lengthofLongestSubstring("ababcbccabcdefghaauvxyzabcdefmnop")


#using a dictionary
#ref: https://www.youtube.com/watch?v=UGDXH9dJosg
#ref: https://www.youtube.com/watch?v=qtVh-XEpsJo
#ref: https://www.youtube.com/watch?v=AoWiiN_bwv4
#ref: https://www.youtube.com/watch?v=gHNMSeeu_4Q

class Solution:
    def lengthofLongestSubstring(self,s): 
        left = 0
        max_size = 0
        seen = dict()
        
        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)#left gets updates only if left<=seen[s[right]]
            seen[s[right]] = right
            max_size = max(max_size,right-left+1)
                
        return max_size,s[left:right+1]
                     
Solution().lengthofLongestSubstring("ababcbccabcdefghaauvxyzabcdefmnop")


