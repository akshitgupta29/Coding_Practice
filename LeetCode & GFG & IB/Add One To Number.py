''' https://www.interviewbit.com/problems/add-one-to-number/ '''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        # listsum = sum(A) + 1
        # return [int(x) for x in str(listsum)]
        # A[-1] = A[-1] + 1
        # for i in range (len(A)-1, 0, -1):
        #     if A[i] == 10:
        #         A[i] = 0
        #         A[i-1] = A[i-1] + 1
        # return [int(x) for x in str(A)]

        t = list(map(str, A))
        p = ''.join(t)
        num = int(p) + 1
        num = str(num)
        temp = []
        for i in range(len(num)):
            temp.append(int(num[i]))

        return temp

ob = Solution()
A =  [9, 9, 9, 9, 9]
print (ob.plusOne(A))