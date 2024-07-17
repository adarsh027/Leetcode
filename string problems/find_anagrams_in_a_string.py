# To solve this, refer the problem of processing consecutive overlapping substring of fixed lengths
class Solution:
    def findAnagrams(self, s, p):
        res=[]
        for i in range(len(s)):
            print(s[i:i+len(p)])
            if sorted(s[i:i+len(p)])==sorted(p):
                res.append(i)    
        return res
Solution().findAnagrams("abcdefcdebcdg","bcd")
Solution().findAnagrams("cbaebabacd","abc")