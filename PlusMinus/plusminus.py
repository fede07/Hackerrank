import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0

    for item in arr:
        if item > 0:
            positives += 1
        elif item < 0:
            negatives += 1
        else:
            zeros += 1

    proportion_positives = positives / len(arr)
    proportion_negatives = negatives / len(arr)
    proportion_zeros = zeros / len(arr)

    print(f"{proportion_positives:.6f}\n{proportion_negatives:.6f}\n{proportion_zeros:.6f6}")



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)