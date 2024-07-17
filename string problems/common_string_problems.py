# build a string by taking charaters from two strings alternatively 
#problem ref: https://www.youtube.com/watch?v=92iIL2WY-YQ&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv&index=8    
s1="abcde"
s2="xyz"
res=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        res=res+s1[i]
        i+=1
    if j<len(s2):
        res=res+s2[j]
        j+=1
print(res)

#just another way I solved the above problem(not efficient but it works!)

s1="abcde"
s2="xyz"
res=''
index=0
if len(s1)>len(s2):
    larger=s1
else:
    larger=s2

for i,j in zip(list(s1),list(s2)):
        index=index+1
        res=res+ i
        res=res+ j
print(res+larger[index:])


#ref: https://www.youtube.com/watch?v=r552u44Zklg
s1="abcdefgh"
s2="xyz"
s3= "12345"
# output = ax1 by2 cz3 d4 e5 f g h 

i,j,k = 0,0,0
while i<len(s1) or j<len(s2) or k<len(s3):
    res=''
    if i<len(s1):
        res=res+s1[i]
        i+=1
    if j<len(s2):
        res=res+s2[j]
        j+=1
    if k<len(s3):
        res=res+s3[k]
        k+=1   
    print(res)



#input : B4A1D3
#output: ABD134
#problem ref: https://www.youtube.com/watch?v=VVznkRrzAbI&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv&index=9
s="B4A1D3"
res1,res2='',''
for ch in s:
    if ch.isalpha():
        res1=res1+ ch
    if ch.isdigit():
        res2=res2+ ch
print((''.join(sorted(res1)))+(''.join(sorted(res2))))


#input : a4b3c2
#output: aaaabbbcc
#problem ref: https://www.youtube.com/watch?v=E9xbLEoSE5Y&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv&index=10
res=''
for ch in s:
    if ch.isalpha():
        prev = ch
    else:
        res=res + prev*int(ch)
print(res)
        
#alternatively      
s="a4b3c2"
res=''
for i in range(len(s)):
    if s[i].isalpha():
        res= res + s[i]*int(s[i+1])
print(res)


# Input: aaabbbccaabb
# Output : 3a3b2c2a2b

#method 1: forward comparison
# 1.Initilize count to 1:
# 2.Compute res when a new character is seen and rest count to 1
# 3 Compute res to include the computation for the last character of input string.


s='aaabbbccaabxb'
cnt=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
    else:  
        res=res+ str(cnt) + s[i]
        cnt=1
    if i==len(s)-2:
        res=res+ str(cnt) + s[-1]
print(res)
        

# method 2: backward comparison
# 1.Initilize count to 1:
# 2.Compute res when a new character is seen and rest count to 1
# 3 Compute res to include the computation for the last character of input string.
s='aaabbbccaabb'
cnt=1 
res=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        res = res + str(cnt)+ s[i-1]
        cnt=1
    if i==len(s)-1:
        res = res + str(cnt)+ s[-1]

print(res)



# Input: a4k3b2
# Output : aeknbd

s='a4k3b2'
Output ='aeknbd'

i=0
res=""
for ch in s:
    if ch.isalpha():
        res = res + ch
        prev = ch
    else:
        res= res + chr(ord(prev)+int(ch))
print(res)     




