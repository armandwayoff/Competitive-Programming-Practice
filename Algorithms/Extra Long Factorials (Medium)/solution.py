#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = n
    for i in range(1, n):
        factorial *= n - i
    print(factorial)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
