#!/bin/python3

import math
import os
import random
import re
import sys


def check_number(n):
    if n % 2 != 0:
        return "Weird"
    elif n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 21):
        return "Weird"
    else:
        return "Not Weird"


if __name__ == '__main__':
    n = int(input())
    print(check_number(n))
