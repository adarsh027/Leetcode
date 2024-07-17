iterable = [1,2,3]

def permutations(iterable):

    
   if len(iterable) == 1:
        return [iterable]
    
   else:
     
       result =[]
       for i in range(0, len(iterable)):
             
            head = iterable[i]
            remlst = iterable[:i] + iterable[i+1:] 
            print("head = {};remlst = {}, currently excecuting permutations({}))".format(head,remlst,iterable))
            
            print("recursive_call = permutations({}))".format(remlst))
             
            recursive_call= permutations(remlst)
            print("recursive call value:",recursive_call)
            print( "continue excecution of permutations({})".format(iterable))
            for p in recursive_call:
                 combo= [head] + p
                 print("combo is:", combo)
                 result.append(combo) # note that in the 1st iteration len([[]]) returns 1
                 
            print("result: {}".format(result))
            
                 
       print("return value(ie, result) after excecution of permutations({})) = {}".format(iterable,result))
       return result

permutations([1,2,3])


# 1st iter  head= 1, remlst_combo =  permutations([2,3], 1) returns    [1,2]
# 2nd iter  head = 2 permutations([3], 0) [1,3]
# 3rd iter  head =3  permutations([3], 0)



    

    



