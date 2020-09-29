# Enter your code here. Read input from STDIN. Print output to STDOUT

rangea = int(input())
a = list(map(int, input().split()))

rangeb = int (input())
b = list(map(int, input().split()))

seta = set(a)
setb = set(b)

setc = seta.union(setb)

print (len(setc))
