#using split() from regex module "re" to preserve whitespace characters appearing in the string
import re

s = "hello       world  lol"
str_list = re.split(r'(\s+)', s)

print(str_list)      # prints ['hello', '       ', 'world', '  ', 'lol']
print(list(s))      # returns a list consisting of all individual characters appearing in s


#Note: split on single space v/s default split
#split on single space
x = s.split(' ')
print(x) #This will split on each occurence of a single space and thus prints ['hello', '', '', '', '', '', '', 'world', '', 'lol']
print(' '.join(x)) # to obtain the original string using join() on a single space
print(s)


#default split
x = s.split()
print(x) #This will split on any no. of whitespace characters and thus prints ['hello', 'world', 'lol']
print(' '.join(x)) # Here, we can't obtain the original string using join() on a single space