#ref: https://www.youtube.com/watch?v=fX64q6sYom0 (Simply Coding channel)

# print a row of five stars
'''  
Desired output:
* * * * * 
'''

n = 5
for i in range(n): # print a row of five stars
    print("*", end= ' ')
    

    
    
# print 5 rows of five stars 
'''  
Desired output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

# method 1:
n = 5
for i in range(n): # print a row of five stars
    print("* "*n)
    

# method 2:  
n = 5
for i in range(n): # print 5 rows of five stars
    for j in range(n): # print a row of five stars
        print("*", end= ' ')
    print()# moves the cursor to the next line after printing the stars in a row

# In the above code, we can see:
# (1) No. of times the outer for loop  executes = no. of rows in the desired pattern. In other words, i corresponds to rows.
# (2) No. of times the inner for loop  executes = no. of stars within a row. In other words, j corresponds to columns.
#here, though the problem can be soled s=easily by method 1, method 2, which uses two for loops, is shown to get a better understanding of the concept which will help you in
# solving for complex star patterns.


# print stars in increasing triangle pattern
'''  
Desired output:
* 
* * 
* * * 
* * * * 
* * * * * 
'''
n = 5
for i in range(n): 
    for j in range(i+1):
        print("*", end= ' ')
    print()


# print stars in decreasing triangle pattern
'''  
Desired output:
* * * * * 
* * * * 
* * * 
* * 
* 
'''
n = 5
for i in range(n): 
    for j in range(i,n): 
        print("*", end= ' ')
    print()
    
    
'''  

Desired output:
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
'''
#Here, output= decreasing trangle with space + increasing traingle with *
n = 5
for i in range(n): 
    for j in range(i,n): 
        print(" ", end= ' ')
    for j in range(i+1):
        print("*", end= ' ')
    print()



'''  
Desired output:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''  
#Note: this increasing pattern is different than the above increasing pattern.Here, there is no space at the bottom row. 
#ref: https://www.youtube.com/watch?v=nFEj5mhq6xQ
n = 5
for i in range(n): 
    for j in range(n-i-1): 
        print(" ", end= ' ')
    for j in range(i+1):
        print("*", end= ' ')
    print()



'''  
Desired output:
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
#Here, output= increasing trangle with space + decreasing traingle with *
n = 5
for i in range(n): 
    for j in range(i+1):
        print(" ", end= ' ')
    for j in range(i,n): 
        print("*", end= ' ')
    print()

'''  
Desired output:
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''
#Note: this decreasing pattern is different than the above increasing pattern.Here, there is no space at the bottom row. 
#ref: https://www.youtube.com/watch?v=lM5nyM-V3jg&t=320s
n = 5
for i in range(n): 
    for j in range(i):
        print(" ", end= ' ')
    for j in range(n-i): 
        print("*", end= ' ')
    print()

'''
Desired output:
         * 
       * * * 
     * * * * * 
   * * * * * * * 
 * * * * * * * * * 
'''
#Here, output= decreasing traingle with space + increasing trangle with * + increasing trangle with * 
n = 5
for i in range(n): 
    for j in range(i,n): 
        print(" ", end= ' ')
    for j in range(i):
        print("*", end= ' ')
    for j in range(i+1): 
        print("*", end= ' ')
    print()

'''  
Desired output:
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''
#Here, output= increasing traingle with space + decreasing trangle with * + decreasing trangle with * 
n = 5
for i in range(n): 
    for j in range(i+1): 
        print(" ", end= ' ')
    for j in range(i,n-1):
        print("*", end= ' ')
    for j in range(i,n): 
        print("*", end= ' ')
    print()


'''  
Desired output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
#ref: https://www.youtube.com/watch?v=nFEj5mhq6xQ
n = 5
for i in range(n): 
    for j in range(n-i-1): 
        print(" ", end= '')
    for j in range(i+1): 
        print("*", end= ' ')
    print()


'''  
Desired output:
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
#ref: https://www.youtube.com/watch?v=lM5nyM-V3jg&t=320s
n = 5
for i in range(n): 
    for j in range(i): 
        print(" ", end= '')
    for j in range(n-i): 
        print("*", end= ' ')
    print()
    
