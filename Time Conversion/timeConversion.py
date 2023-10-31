#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # 07:05:45PM
    time = s.split(":")
    hours = int(time[0])
    minutes = time[1]
    seconds = time[2][:2]
    meridiem = time[2][2:] 

    if meridiem == "AM" and hours == 12:
        hours = hours - 12
    elif meridiem == "PM" and (hours >= 1 and hours <= 11):
        hours = hours + 12

    if hours < 10:
        hours = f"0{hours}"


    return f"{hours}:{minutes}:{seconds}"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()