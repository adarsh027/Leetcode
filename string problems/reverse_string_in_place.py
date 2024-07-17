#leetcode problem https://leetcode.com/problems/reverse-string/submissions/
#two-pointer approach
#In this problem, we are actually reversing a list of strings since we can't modify a string in place.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j= len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1

# Two ways you can modify a string:
# 1. Convert it into a list using list(), do the modification and join it back using join().

# Ex: replacing a character in the string
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print(string)          # prints abrackdabra


# 2. Concatenate strings( string slices or empty string) using '+' operator. 

# Ex 1:replacing a character in the string
string = "abracadabra"
string = string[:5] + "k" + string[6:]
print(string)    # prints abrackdabra

# Ex 2: reverse a string
str1 = "python" 
str2 = "" 
for ch in str1: 
    str2 = ch + str2
    print(str2)
print(str1) # prints the original string: python
print(str2) # prints the reversed string : nohtyp
