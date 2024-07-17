# ref: https://www.youtube.com/watch?v=EMKDoj5Sshk
# ref https://www.youtube.com/watch?v=EvcNmtUbzQQ
class Solution:
    def removeDuplicates(self, s):
        st = []
        for ch in s:
            if st and st[-1]==ch:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)
    
Solution().removeDuplicates("abbaca")


# replace all adjacent duplicates with x
class Solution:
    def removeDuplicates(self, s):
        st = []
        for ch in s:
            if st and st[-1]==ch:
                st.pop()
                st.append('x')
            else:
                st.append(ch)
        return ''.join(st)
    
Solution().removeDuplicates("abbacayyyy")

