'''https://www.interviewbit.com/problems/pick-from-both-sides

Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2
 '''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum2 = float('-inf')
        for i in range (B):
            # sum1 = max(sum(A[:B]), sum(A[B:]), (sum(A[:i]) + sum(A[len(A)-B+i:]))) 

            # Gives error with this line sum(A[B:]), thugh it should be considered last ke corner bhi to cinsider hne chaiye na
            
            sum1 = max(sum(A[:B]), (sum(A[:i]) + sum(A[len(A)-B+i:]))) 
            #Works with this, but gives time out error.

        
            sum2 = max (sum2, sum1)
        return sum2

ob = Solution()
A = [ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
B = 81

print (ob.solve(A,B))