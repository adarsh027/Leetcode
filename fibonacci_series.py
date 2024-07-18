#fibonacci series

#recursive
def fib(n):  
    if(n<=2) : # 1st element(n=1) will be n-1 = 1-1= 0 and second element(n=2) will be  1st element(n=1) will be n-1 = 2-1= 1
        return n-1
    return fib(n-1)+fib(n-2)

fib(8)

for i in range(1,8):
    print(fib(i), end=" ")
    
    
    
#iterative
def fib(n):  
    if(n<=2) :
        return n-1
    n1 = 0
    n2 = 1
    res =[0,1]
    for i in range(2,n):
        n3 = n1 + n2
        res.append(n3)
        n1 = n2
        n2 = n3    
    print(res)

fib(8)

#iterative
def fib(n):  
    if(n<=2) :
        return n-1
    n1 = 0
    n2 = 1
    res =[0,1]
    for i in range(2,n):
        sum = n1 + n2
        res.append(sum)
        n1 = n2
        n2 = sum  
    print(res,sum)

fib(8)