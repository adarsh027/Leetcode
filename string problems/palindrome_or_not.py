# palindrome or not
s="malayalam"
i=0
j=len(s)-1
isPal=True
while i<j:
    print(s[i],s[j])
    if s[i]!=s[j]:
        isPal=False
    j=j-1
    i+=1
        
print(isPal)


#alternatively
def isPalindrome(str):
  
    # Run loop from 0 to len/2
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True
  
s = "malayalam"
isPalindrome(s)