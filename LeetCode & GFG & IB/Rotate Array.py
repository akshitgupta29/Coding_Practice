''' https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/'''

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if k > n:
            i = k%n
            nums[:] =nums[n-i:]+ nums[0:n-i]
        else:
            nums[:] =nums[n-k:]+ nums[0:n-k]
        
ob = Solution()
# nums = [int (x) for x in input().strip().split()]
nums = [1,2,3]
# k = int(input())
k=4
ob.rotate(nums, k)
print (nums)