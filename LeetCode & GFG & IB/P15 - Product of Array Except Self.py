from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        current = i
        product = 0
        result = [1]
        for j in range(len(nums)):
            if j == current:
                continue
            else:
                result[j] = result[j] * nums[j]
    return result
if __name__ == "__main__":
    result = productExceptSelf([1,2,3,4])
    print (result)