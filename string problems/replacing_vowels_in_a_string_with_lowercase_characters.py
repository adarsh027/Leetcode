st = "ADARSH"

for ch in st:
    if ch in ['A','I','E','O','U']:
        st= st.replace(ch, ch.lower())

print(st)



# st = "ADARSH"
# new_st=""
# count=0
# for ch in st:
#     if ch in ['A','I','E','O','U']:
#         count+=1
#         ch = ch.lower()
#     new_st = new_st + ch

# print(new_st, count)