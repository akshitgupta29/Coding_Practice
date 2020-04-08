'''
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
'''

from typing import List
def countElements(arr: List[int]) -> int:
    count = 0
    set1 = set(arr)
    for item in arr:
        if (item + 1) in set1:
            count +=1
    return count

if __name__ == "__main__":
    arr = [1,1,2,2]
    print (countElements(arr))

