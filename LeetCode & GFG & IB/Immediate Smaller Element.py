'''https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1'''


#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
	    temp = []
        for i in range(0, n):
            if arr[i+1] > arr[i]:
                temp.append(-1)
            else:
                temp.append(arr[i+1])
        
        temp.append (-1)
        return temp



		# code here

#{ 
#  Driver Code Starts


# if __name__ == '__main__':
#     tcs=int(input())

#     for _ in range(tcs):
#         n=int(input())
#         arr=[int(x) for x in input().split()]
#         ob = Solution()
#         ob.immediateSmaller(arr,n)
#         for x in arr:
#             print(x, end=" ")
#         print()
# # } Driver Code Ends