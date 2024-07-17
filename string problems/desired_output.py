#input: n=4
#desired output:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

n=4

x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x, end =' ') 
        x+=1
    print()
