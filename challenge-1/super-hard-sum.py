#! /usr/bin/env python3.4

import fileinput


def super_hard_sum():
    """Sum lines from standard input

    Get line by line and return the sum of all numbers.
    """
    for line in fileinput.input():
        sum = 0
        for num in line.split():
            if(num.isnumeric() or (num.startswith('-') and num[1:].isdigit())):
                sum += int(num)
        print(sum)

super_hard_sum()
