from typing import List, Sized

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print (nums1)
        # if n != 0:
        #     del nums1[n:]
        # print (nums1)
        # # nums1 = nums1 + nums2
        # nums1.extend(nums2)
        # # print (nums1)
        # nums1.sort()
        # print (nums1)
        '''One approach'''
        # N = len(nums1)
        # for i in range(N-1, N-n-1, -1):
        #     if nums1[i] == 0:
        #         del nums1[i]
        #     print (nums1)
        # nums1.extend(nums2)
        # nums1.sort()

        '''Another Approach'''

        for i in range (m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

        
ob = Solution()
# nums1 = [1,2,3,0,0,0]
nums1 = []

m = 0
nums2 = [1]
n = 1
ob.merge(nums1,m,nums2,n)
print (nums1)