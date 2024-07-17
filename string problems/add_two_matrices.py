#input
X= [[1,2,3],
       [4 ,5,6],
       [7 ,8,9]]

Y = [[9,8,7],
       [6,5,4],
       [3,2,1]]

#output:
[[10, 10, 10], [10, 10, 10], [10, 10, 10]]


# using two for loops to build the result(output)
def add(x,y):
    res= [[0]*3,[0]*3,[0]*3] # ie, res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
           res[i][j]= x[i][j]+ y[i][j]
    return res

add(X,Y)

# list comprehension to build the result(output)
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]

# using zip()
  
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [map(sum, zip(*t)) for t in zip(X, Y)]
  
print(result)



# using numpy
import numpy as np
  
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = np.array(X) + np.array(Y)
 
print(result)



