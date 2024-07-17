#hackerank problem: https://www.hackerrank.com/challenges/find-a-string/submissions/code/274333700

#method 1: comparing only with substrings of length upto length of the substring to be found
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count=count + 1
    return count

        
string="ABCDCDC"
sub_string="CDC"
count_substring(string, sub_string)

#note: we can't use count() method here as it will only consider non-overlapping occurences of the substring,


# method 2: inefficient since we are comparing with all substrings(just for demonstration purpose I'm including this here)
def count_substring(string, sub_string): 
   count = 0
   for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i:j+1] ==sub_string:
                 count=count + 1
                 print(string[i:j+1])

   print(count)

           
string="ABCDCDC"
sub_string="CDC"
count_substring(string, sub_string)


