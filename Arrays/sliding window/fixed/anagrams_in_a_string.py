# ref: https://www.youtube.com/watch?v=G8xtZy0fDKg&t=612s

# Logic(in short) w.r.t to the current problem:
# 1. Compute sCount and result for the 1st window. While computing sCount also compute pCount.(Note: pCount is computed only once )
# 2. Process subsequent windows in s. In each subsequent window processing, we do the following
# 1.Build sCount by visiting every element in s.
# 2.Build result by including the starting index of the window, provided the corresponding substring in s, 
# (ie, s[left:right+1]),is an anagram of p. This is achieved by comparing sCount and pCount for equality.
# Note : starting index of the 1st window is 0 and for subsequent windows will be the left pointer.
# Note: here, sCount is the intermediate window computation we need to compute repeatedly for every window to generate/build the result(answer).



# Sliding window fixed size working:
# 1. The 1st for loop: We process the 1st window,compute intermediate computation and result for the 1st window. No sliding happens happens in this case.
# 2. The 2nd for loop: We process subsequent windows, sliding happens and it invloves the below steps:
# a. Using the current element represented by right pointer, do some intermediate computation/computations.
# (Using the element represented by the right pointer is same as processing a window. In sliding window, each window processing invloves processing a single element represented by the right pointer.)
# b. From intermediate computation, remove computation related to the preceding windows leftmost element, which is represented by the left pointer.
# c. Increment left by 1 so that it points to the leftmost element of the current window.
#    (Sliding has finished; the left and right are at the boundaries of the current window.)
# d. Finally, depending upon the problem, you might have to satisfy a given condition that involves your intermediate computation/computations done for the current window. 
#    Check if the given condition is satisfied and compute the answer/result for the current window.
  
# 3. Once all the windows are processed(ie, when the 2nd for loop exits), we return the result.

class Solution:
    def findAnagrams(self, s, p):
       if len(p) >len(s):
           return []
       sCount, pCount= {},{}
       for i in range(len(p)): # computing pCount and sCount for the 1st window, which is the size of p.
           pCount[p[i]] = 1 + pCount.get(p[i],0)
           sCount[s[i]] = 1 + sCount.get(s[i],0)
           
       print(sCount,pCount)
      
       if sCount==pCount: # computing result(answer) for the 1st window
            res=[0]
       else:
            res=[]
            
       left = 0
       for right in range(len(p),len(s)): # computing sCount for the subsequent windows
           # Computing sCount for the current window
            sCount[s[right]]= 1 + sCount.get(s[right],0) 
            sCount[s[left]]-=1 
            if sCount[s[left]]==0:
                sCount.pop(s[left])
            left+=1 # Incrementing the left pointer
            
            if sCount==pCount: # computing result(answer) for the current window
                print(sCount,pCount)
                res.append(left)      
       return res
       

Solution().findAnagrams("cbaebabacd","abc")


#Note:
s = "xyz"
print(s[ord('a')-ord('a')])# prints x, ie, the value at index 0.
print(s[ord('b')-ord('a')])# prints y, ie, the value at index 1.
print(s[ord('c')-ord('a')])# prints z, ie, the value at index 2.


# alternative approach(not efficient)
class Solution:
    def isAnagrams(self, s1, s2):
       if len(s1) != len(s2):
           return False
       s1Count, s2Count= {},{}
       s1=s1.lower()
       s2=s2.lower()
       for i in range(len(s1)):
           s1Count[s1[i]] = 1 + s1Count.get(s1[i],0)
           s2Count[s2[i]] = 1 + s2Count.get(s2[i],0)
           
       if s1Count==s2Count: 
            return True
       else:
            return False
    def findAnagrams(self, s, p):
        res=[]
        for i in range(len(s)):
            x=self.isAnagrams(s[i:i+len(p)],p)
            if x:
                res.append(i)
            
        return res

Solution().findAnagrams("cbaebabacd","abc")

# alternative approach(not efficient)
class Solution:
    def findAnagrams(self, s, p):
        res=[]
        for i in range(len(s)):
            print(s[i:i+len(p)])
            if sorted(s[i:i+len(p)])==sorted(p):
                res.append(i)    
        return res

Solution().findAnagrams("cbaebabacd","abc")



