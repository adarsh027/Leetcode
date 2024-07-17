#ref: https://www.youtube.com/watch?v=2ayws5Y-WM4
#ref: https://leetcode.com/problems/remove-duplicate-letters/solutions/3240694/316-space-98-37-solution-with-step-by-step-explanation/
#note: this problem is same as https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
# Note : Remember the below two points for this problem
# 1 Create a dictionary "last_indx" to store last index of all characters in s
# 2. keep popping the stack as long as:
# 1. stack is non-empty
# 2. current character is less than top(last) element of stack.
# 3. index of current character is less than last index of top(last) element of stack 

class Solution:
    def removeDuplicateLetters(self, s):
        stack = []
        last_indx = {char: i for i, char in enumerate(s)}
        
        for indx, char in enumerate(s):
            if char not in stack:
                while stack and char < stack[-1] and indx < last_indx[stack[-1]]:
                    stack.pop()    
                stack.append(char)
                        
        return ''.join(stack)
Solution().removeDuplicateLetters("cbacdcbc") # prints acdb 
    
# Removing duplicate letters preserving relative order of characters in the original string
# method 1: Using a dictionary 
class Solution:
    def removeDuplicates(self, s):
        seen = {}
        for ch in s:
            seen[ch]= seen.get(ch,0) + 1
        return ''.join(seen)
    
Solution().removeDuplicates("cbacdcbc") # prints cbad

# method 2: using a list( a dictionary is preferred over a list for performance benefits)
# Note: here, we can't use a set don't preserve the order in which elements are inserted. If the question does not specify 
# that the order of elements has to be maintained in the resultant string, then you can use a set.

class Solution:
    def removeDuplicates(self, s):
        seen = []
        for ch in s:
            if ch not in seen:
                seen.append(ch)
        return ''.join(seen)
    
Solution().removeDuplicates("cbacdcbc") # prints cbad









