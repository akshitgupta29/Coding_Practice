# Problem link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


directory = {}
n = int(input())
for _ in range(n):
    data = input()
    data_split = data.split(" ")
    directory[data_split[0]] = data_split[1]
    # for key, value in directory.items():
    #     print(key)
    #     print(value)
while True:
    try:
        to_check = input()
        if to_check in directory:
            print(f"{to_check}={directory[to_check]}")
        else:
            print("Not found")
    except:
        break
