'''
https://www.geeksforgeeks.org/run-length-encoding/ '''

from collections import Counter
def countingChar(string):
    return Counter(string)

string = 'wwwwaaadexxxxxx'
print (countingChar(string))