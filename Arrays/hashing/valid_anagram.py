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
            

Solution().isAnagrams("Listen","Silent")


#alternative way
class Solution:
    def isAnagrams(self, s1, s2):
       if len(s1) != len(s2):
           return False
       s1=s1.lower()
       s2=s2.lower()
     
       return sorted(s1)==sorted(s2)
            

Solution().isAnagrams("Listen","Silent")