
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'smallestNegativeBalance' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY debts as parameter.
#

def smallestNegativeBalance(debts):
    # Write your code here
    deb = {}
    lend = {}
    for row in debts:
        deb[row[0]] = deb.get(row[0], 0) + int(row[2])
        lend[row[1]] = lend.get(row[1], 0) + int(row[2])

    mindeb = {}
    keys = deb.keys()
    for k in keys:
        d = deb.get(k, 0)
        l = lend.get(k, 0)
        bal = int(l) - int(d)
        mindeb[k] = bal

    name = min(mindeb.items(), key=lambda x: x[1])

    return list(name)[0]

    # print(row)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    debts_rows = int(input().strip())
    debts_columns = int(input().strip())

    debts = []

    for _ in range(debts_rows):
        debts.append(input().rstrip().split())

    result = smallestNegativeBalance(debts)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()



