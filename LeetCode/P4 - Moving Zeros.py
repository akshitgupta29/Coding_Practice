'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    arr = nums.copy()
    for i in nums:
        print (i)
    print (nums)


if __name__ == "__main__":
    arr = [0,1,0,3,12]
    moveZeroes(arr)
