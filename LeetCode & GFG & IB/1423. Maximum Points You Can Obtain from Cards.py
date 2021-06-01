''' https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3739/'''
'''https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/'''

from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum (cardPoints)
        else:
            # # print (cardPoints[-k:])
            # sum = 0
            # left = 0
            # right = -1
            # max_num = cardPoints[left]
            # sum = max(max_num, cardPoints[right])
            # if max(max_num, cardPoints[right]) == max_num:
            #     left += 1
            # else:
            #     right -= 1 

            # print (sum)

            # return max(sum(cardPoints[:k]), sum(cardPoints[-k:]))
            left_sum = [0] *(k+1)
            right_sum = [0]* (k+1)



            for i in range (1,k+1):
                left_sum[i] = left_sum[i-1] + cardPoints[i-1]
            
            for i in range (1,k+1):
                right_sum[i] = right_sum[i-1] + cardPoints[len(cardPoints) - i]
            
            sum = 0
            for i in range (k+1):
                sum = max(sum, left_sum[i]+right_sum[k-i])
            return sum



            

ob = Solution()
cardPoints = [100,40,17,9,73,75]
k =3
print (ob.maxScore(cardPoints, k))