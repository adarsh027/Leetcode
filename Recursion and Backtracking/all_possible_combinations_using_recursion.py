iterable = [1,2,3]

def combinations(iterable,n):

   if n == 0:
        return [[]]
     
   result =[]
   for i in range(0, len(iterable)):
         
        head = iterable[i]
        remlst = iterable[i+1:]
        print("head = {};remlst = {}, currently excecuting combinations({},{}))".format(head,remlst,iterable, n))
        
        print("recursive_call = combinations({},{}))".format(remlst, n-1))
         
        recursive_call= combinations(remlst, n-1)
        print("recursive call value:",recursive_call)
        print( "continue excecution of combinations({},{}))".format(iterable, n))
        for p in recursive_call:
             combo= [head] + p
             print("combo is:", combo)
             result.append(combo) # note that in the 1st iteration len([[]]) returns 1
             
        print("result: {}".format(result))
        
             
   print("return value(ie, result) after excecution of combinations({},{})) = {}".format(iterable, n,result))
   return result

combinations([1,2,3],2)


# 1st iter  head= 1, remlst_combo =  combinations([2,3], 1) returns    [1,2]
# 2nd iter  head = 2 combinations([3], 0) [1,3]
# 3rd iter  head =3  combinations([3], 0)


    

    




