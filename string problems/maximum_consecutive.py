# ref: https://leetcode.com/problems/consecutive-characters/solutions/1626103/c-python-3-simple-solutions-w-explanation-brute-force-sliding-window-single-pass/
# ref: https://www.youtube.com/watch?v=Pt4Z8iLbBZY
# ref: https://www.youtube.com/watch?v=aBT1_0PGEAk
#ref:https://www.youtube.com/watch?v=_e_7hTec-SM

class Solution:
    def maxPower(self, s):
        count=1 # For a non-empty string, the count of consecutive characters is atleast 1 regardless of whether it contains consecutive duplicates or not.
        max_cnt=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
                max_cnt= max(max_cnt,count)
            else:
                count=1 #resetting the countback to 1 when consecutive characters are not found
        return max_cnt
    
Solution().maxPower("abcd") # prints 1
Solution().maxPower("abccaaddd") # prints 8
