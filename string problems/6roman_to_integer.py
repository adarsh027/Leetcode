#Ref:  https://www.youtube.com/watch?v=3jdxYj3DD98 (neetcode)
# If current element is less than the next element in the array/string as per their integer value, then
# that current element's integer value is taken as negative when computing the result
# otherwise(ie, current element is not less than the next element as per their integer value), then
# that current element's integer value is taken as positive when computing the result

# Examples: Current element is less than the next element as per their integer value
# s = 'IX'
# result = -(integer value of I) + (intger value of X) = -1 + 10 = 9

# Examples : Current element is not less than the next element as per their integer value
# s = 'XI'
# result = (integer value of X) + (intger value of I) = 10 + 1 = 11

# s = 'XX'
# result = (integer value of X) + (intger value of X) = 10 + 10 = 20

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                result -= roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]
        return result
    
# Note: Using the condition i + 1 < len(s) , we avoid index out of bounds error.


# Do not consider the below solution; I have just inlcuded it just like that.. I just happen to solve it after few hours of grinding.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        result = 0
        i = 0

        while i < len(s):
            print(f"iteration {i}")
            if (i+1) < len(s) and  s[i]=='I' and s[i+1]== 'V':
                result = result + 4
                i += 2
            elif (i+1) < len(s) and  s[i]=='I' and s[i+1]=='X':
                result = result + 9
                i += 2
            elif (i+1) < len(s) and  s[i]=='X' and s[i+1]=='L':
                result = result + 40
                i += 2
            elif (i+1) < len(s) and  s[i]=='X' and s[i+1]=='C':
                result = result + 90
                i += 2
            elif (i+1) < len(s) and  s[i]=='C' and s[i+1]=='D':
                result = result + 400
                i += 2
            elif (i+1) < len(s) and  s[i]=='C' and s[i+1]=='M':
                result = result + 900
                i += 2
            else:
                result += roman_numerals[s[i]]
                i += 1
            print(f"result in iteration {i}: {result}")
        return result