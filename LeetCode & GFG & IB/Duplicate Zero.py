'''https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/'''

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        N = len (arr)
        while i < N:
            if arr[i] == 0:
                print (i)
                arr.insert(i+1, 0)
                i +=2
            else:
                i+=1
        del arr[N:]

ob = Solution()
x= [1,0,2,3,0,4,5,0]
ob.duplicateZeros(x)
print (x)