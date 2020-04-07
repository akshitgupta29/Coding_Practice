'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
'''

def isHappy(n: int) -> bool:
    visited = set([n])
    while n!=1:
        num = n
        n = 0
        while num:
            num, rem = num//10, num %10
            n += rem ** 2
            break
        visited.add(n)
    return n == 1 

    

if __name__ == "__main__":
    print (isHappy(19))