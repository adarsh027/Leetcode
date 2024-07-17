#ref: https://www.youtube.com/watch?v=w6LcypDgC4w&t=2s
# ref: https://www.youtube.com/watch?v=HGMGudSfpRk

#Logic
# 1. If stack is non-empty and current element matches with last lement of stack--> increase the count
# else----> add the character to the stack with count as 1.
# 2. If count of last element of stack equals k, then pop the stack.
# 3 Consruct the string using join()

class Solution:
    def removeDuplicates(self, s, k):
        st = [] # to store [ch, count]
        for ch in s:
            if st and st[-1][0]==ch:
                    st[-1][1]+=1
            else:
                st.append([ch,1]) # make sure you use a list here and not a tuple as a tuple can't be modified.
                
            if st[-1][1]==k:
                st.pop()
        
        # print(type(ch*cnt for ch,cnt in st))  
        return ''.join(ch*cnt for ch,cnt in st)
    
Solution().removeDuplicates("abbbaacccacabbbx",3) # prints acax

# Note:
# When you get IndexError, your mind should think of putting the
# condition to check if the iterable is not empty before the 
# operation that caused the IndexError
