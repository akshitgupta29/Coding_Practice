'''https://leetcode.com/problems/maximum-product-of-three-numbers/'''
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if n == 3:
            return nums[n-1]*nums[n-2]*nums[n-3]
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[2])

obj = Solution()
nums = [1,2,3]
# [1,2,3,4]
# [-1,-2,-3]

print (obj.maximumProduct(nums=nums))