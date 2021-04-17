'''https://leetcode.com/problems/maximum-product-of-three-numbers/'''
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 3:
            return nums[-1]*nums[-2]*nums[-3]
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

obj = Solution()
nums = [-100,-98,-1,2,3,4]
# [1,2,3,4]
# [-1,-2,-3]

print (obj.maximumProduct(nums=nums))