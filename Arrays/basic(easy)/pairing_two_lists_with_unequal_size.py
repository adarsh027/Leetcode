shorter_list= ['Mon','WED','FRI']
longer_list= [1,2,3,4,5,6,7,8,9,10]

# Method 1 :Using indexing for the shorter list so that we can cycle through it upto the length of longer list.
# Note: i%len(shorter_list) < len(shorter_list) as remainder is always less than the divisor. This way, we can cycle through the smaller list when processing a larger list parallely.
for i in range(len(longer_list)):
    print(i%len(shorter_list))
    print(shorter_list[i%len(shorter_list)],longer_list[i])


print(shorter_list*len(longer_list))

# Method2 : Making length of shorter_list equal to or greater than longer_list
for i,j in zip(shorter_list*len(longer_list),longer_list):# we need not multiply shorter_list with length of longer_list; we can use any multiplier value provided it makes the shorter_list equal to or greater than the longer_list
    print((i,j),end=' ')


# Method 3: Using itertools
from itertools import cycle

# zipping in cyclic fashion if any of the list is of shorter length
for x,y in zip(cycle(shorter_list),longer_list):
    print(x,y)
    
