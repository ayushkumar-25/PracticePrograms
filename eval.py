#!/bin/python3

import math
import os
import random
import re
import sys
import functools as f

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    x = arr[0:4]
    y = f.reduce(lambda a,b:a+b,x)
    z = arr[1:5]
    a = f.reduce(lambda a,b:a+b,z)
    print(y,a)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
