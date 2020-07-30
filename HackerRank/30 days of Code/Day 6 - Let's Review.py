# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    string = input()
    print(f"{string[::2]} {string [1::2]}")
