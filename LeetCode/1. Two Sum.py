'''
https://leetcode.com/problems/two-sum/
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dicts.keys():
                return [dicts.get(target-nums[i]), i]
            else:
                dicts[nums[i]] = i
        return (None)
            
obj = Solution()
nums = [2,7,11,15]
target = 18
print (obj.twoSum(nums, target))