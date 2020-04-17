# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

''' word is similar if 2x = y '''

from collections import Counter

word = input()
count = Counter(word)
if (2 * count['z']) == count['o']:
    print ('Yes')
else:
    print ('No')



