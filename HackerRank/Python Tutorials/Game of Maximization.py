#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    # Write your code here
    
    # odd_index = []
    # even_index= []

    
    odd_index = arr[::2]
    even_index = arr[1::2]
    # print(odd_index)
    # print(even_index)
    if sum(odd_index) == sum(even_index):
        return odd_index
    else:
        0

        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 4

    arr = [5,1,1,4]

    result = maximumStones(arr)

    print (result)