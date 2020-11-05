from itertools import permutations

a,b = input().split()
b = int(b)

new_list = [''.join(x) for x in sorted(list(permutations(a,b)))]
print (new_list) 

