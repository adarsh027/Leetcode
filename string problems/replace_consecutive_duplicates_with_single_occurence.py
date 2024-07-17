#replace consecutive duplicates/occurences with single occurence

# method 1: using a stack
class Solution:
    def remove_duplicates(self, s):
        st = []
        for ch in s:
            if st and st[-1]==ch:
                st.pop()
            st.append(ch)
        return ''.join(st)
    
Solution().remove_duplicates("abbaca") # prints abaca
Solution().remove_duplicates("hooraaaaayaaa") # prints horaya



#method 2 : using string concatenation invloving fwd comparison of elements
class Solution:
    def remove_duplicates(self, s):
        res=""
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                res=res+s[i]  # we keep adding the ith character to the result
            if i== len(s)-2:
                res=res+s[-1] # Including the last character to  the result
            
        return res
Solution().remove_duplicates("abbaca") # prints abaca
Solution().remove_duplicates("hooraaaaayaaa") # prints horaya


#alternatively: Including the last character in the return statement
class Solution:
    def remove_duplicates(self, s):
        res=""
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                res=res+s[i]  # we keep adding the ith character to the result
            
        return res + s[-1]
Solution().remove_duplicates("abbaca") # prints abaca
Solution().remove_duplicates("hooraaaaayaaa") # prints horaya


# method 3 : using string concatenation invloving backward comparison of elements
class Solution:
    def remove_duplicates(self, s):
        res=""
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                res=res+s[i]
            if i== 1:
                res= s[i-1] + res # Including the 1st character is the result
            
        return res
Solution().remove_duplicates("abbaca") # prints abaca
Solution().remove_duplicates("hooraaaaayaaa") # prints horaya

#alternatively, Including the 1st character(0th indexed element) in the return statement
class Solution:
    def remove_duplicates(self, s):
        res=""
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                res=res+s[i]
            
        return s[0] + res
Solution().remove_duplicates("abbaca") # prints abaca
Solution().remove_duplicates("hooraaaaayaaa") # prints horaya