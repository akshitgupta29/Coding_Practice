'''https://www.interviewbit.com/problems/find-duplicate-in-array/'''

a = (1,2,3,1)
from collections import Counter
count = Counter(a)
print (count.most_common(1)[0][0])

# print (Counter.most_common))