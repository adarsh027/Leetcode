# using regex
import re
s = '!hi. wh?at is the weat[h]er lik?e.'
res = re.sub(r'[^\w\s]', '', s)
print(res)



#using for loop with str.replace() method

import string

str1 = '!hi. wh?at is the weat[h]er lik?e.'

for ch in string.punctuation:
    str1 = str1.replace(ch, '')

print(str1)

#using str.translate() method
#this is the most efficient approach

import string

str1 = '!hi. wh?at is the weat[h]er lik?e.'
table = str.maketrans('', '', string.punctuation)
res = str1.translate(table)
print(res)