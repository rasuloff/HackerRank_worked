'''
Task

Given an integer, n, print its first 10 multiples. Each multiple n * i (where 1<= i <= 10)
should be printed on a new line in the form: n * i = result.

Input format: A single integer n.

Constraints:
2 <= n <= 20

Output format:
Print 10 lines of output; each line i (where 1 <= i <+ 10) contains the result of n * i in the form:
n * i = result.

'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    result = n * i
    if n < 2:
        print('Number is out of range')
        break
    elif n > 20:
        print('Number is out of range')
        break
    print(f'{n} x {i} = {result}')
