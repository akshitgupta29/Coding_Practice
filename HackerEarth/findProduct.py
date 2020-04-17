#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

'''
Input: 
5
1 2 3 4 5

Output: 120
'''

num = int(input())
answer = 1

values = [int(value) for value in input().split(' ')]
for j in values:
    answer = (answer * j) % (10**9 + 7)
print (answer)
