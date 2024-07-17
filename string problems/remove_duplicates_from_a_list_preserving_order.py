# Removing duplicates using a set does not preseve order

lst = [42, 42, 'Alice', 'Alice', 1]
seen = set()
for ele in lst :
    if ele not in seen:
        seen.add(ele)
print(list(seen))                  # prints ['Alice', 1, 42]


# Removing duplicates using a dictionary preserves order
seen = {}
for ele in lst :
    seen[ele]= seen.get(ele,0)+1
print(list(seen.keys()))            #prints [42, 'Alice', 1]
    



# Using set() method to remove duplicates does not preserve order
lst = [42, 42, 'Alice', 'Alice', 1]
res = list(set(lst))
print(res)                      # ['Alice', 1, 42]



# Using dict.fromkeys() method to remove duplicates does preserve order
lst = [42, 42, 'Alice', 'Alice', 1]
res = list(dict.fromkeys(lst))
print(res)                        #prints [42, 'Alice', 1]

#Note: The dict.fromkeys() method of dictionary returns dictionary as seen below
print(type(dict.fromkeys(lst))) #   prints <class 'dict'>
# print(dict.fromkeys(lst))     prints {42: None, 'Alice': None, 1: None}


# Preserving the order by sorting using key parameter of methods sort() and sorted()

# using sort() with key parameter
list1 = ['b','c','d','b','c','a','a']    
list2 = list(set(list1))    
list2.sort(key=list1.index)    
print(list2)                               #prints [42, 'Alice', 1]  

# using sorted() with key parameter
list1 = ['b','c','d','b','c','a','a']  
list2 = sorted(set(list1),key=list1.index)  
print(list2)                                #prints [42, 'Alice', 1]



