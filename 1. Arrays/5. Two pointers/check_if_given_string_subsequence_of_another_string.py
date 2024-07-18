# ref: https://www.youtube.com/watch?v=99RVfqklbCE
class Solution:
    def isSubsequence(self, s, t):
        i,j = 0,0
        while i < len(s) and j<len(t):
                if s[i]==t[j]:
                    i+=1
                j+=1
  
        if i==len(s): # When all the characters of s are present in t, i will become equal to len(s)
            return True
        else:
            return False
        
Solution().isSubsequence("abc","ahbgdc")
