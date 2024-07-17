#ref/inspiration for below notes: hackerrank problem https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true)

# Processing consecutive non-overlapping substrings of given maximum length/width
string =  "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4 # maximum length of each consecutive non-overlapping substring

res=[]
    
for i in range(0,len(string),max_width): 
    res.append(string[i:i+max_width]) 
print('\n'.join(res))

#sample input:   
# string =  "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# max_width = 4
  
# output:  
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# Processing only the consecutive non-overlapping substrings of length = max_width, 
for i in range(0,len(string)-max_width,max_width): # subtract max_width from len(string) in the range() function 
    res.append(string[i:i+max_width]) 
print('\n'.join(res))  

# output:  
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


# Processing consecutive overlapping substrings of given maximum length/width
string =  "ABCDEF"
max_width = 4 # maximum length of each consecutive overlapping substring

res=[]
for i in range(0,len(string)): # observe that there is no 3rd paramter(i.e,steps parameter) like in the case of consecutive non-overlapping substrings
    res.append(string[i:i+max_width]) 
print('\n'.join(res))


#sample input:   
# string =  "ABCDE"
# max_width = 4
  
# output:  
# ABCD
# BCDE
# CDEF
# DEF
# EF
# F

# Processing only the consecutive overlapping substrings of length = max_width, 
# this is like sliding windows of size = max_width
res=[]
for i in range(0,len(string)-max_width+1): # subtract max_width from len(string) and add 1 in the range() function 
    res.append(string[i:i+max_width]) 
print('\n'.join(res))
  
# output:  
# ABCD
# BCDE
# CDEF

