#ref: https://www.youtube.com/watch?v=w6LcypDgC4w&t=2s
# ref: https://www.youtube.com/watch?v=HGMGudSfpRk
class Solution:
    def removeDuplicates(self, s, k):
        st = []
        for ch in s:
            if st and st[-1][0]==ch:
                    st[-1][1]+=1
            else:
                st.append([ch,1])
            if st[-1][1]==k:
                st.pop()
        
        # print(type(ch*cnt for ch,cnt in st))  
        return ''.join(ch*cnt for ch,cnt in st)
    
Solution().removeDuplicates("abbbacccacabbbx",4)

# Note:
# When you get IndexError, your mind should think of putting the
# condition to check if the iterable is not empty before the 
# operation that caused the IndexError
