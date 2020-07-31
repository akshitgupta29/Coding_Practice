#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
    # print(len(max(bin(int(input().strip()))[2:].split('0'))))
    # print (bin(n))
    result = len(max(bin(n).replace("0b", "").split('0')))
    print (result)
    
