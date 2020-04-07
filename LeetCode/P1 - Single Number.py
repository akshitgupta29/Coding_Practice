'''
Problem 1:
Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/
'''

#using collections
from collections import Counter
from typing import List

def singleNumber(nums: List[int]) -> int:
    for num, count in Counter(nums).items():
        if count == 1:
            return num
    return 0

#without using the extra memory i.e. using the XOR of all the list elements.
def singleNumber(nums: List[int]) -> int:
    result = 0
    for i in nums:
        result ^= i
    return result

if __name__ == "__main__":
    list1 = [2,2,1,1,4]
    c = singleNumber (list1)
    print (c)
