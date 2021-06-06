'''https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3767/'''

#Solution is implemented using BFS. Mostly with the help of internet.
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        queue = deque([('0000',0)])
        visited = set('0000')
        # print (queue)
        # return 1

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            
            elif string in dead_set:
                continue

            for i in range (4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[i:] + str(new_digit) + string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))

        
        return -1




#Driver Funcion
ob = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print (ob.openLock(deadends, target))