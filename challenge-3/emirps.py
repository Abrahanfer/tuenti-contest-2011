#! /usr/bin/env python3.4

import fileinput


def is_prime(number):
    if(number <= 3):
        if(number <= 1):
            return False
        return True
    if(not(number % 2) or not(number % 3)):
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):
        if(not number % i or not number % (i + 2)):
            return False
    return True


def count_emirps(number):
    accumulator = 0
    for i in range(2, number):
        if(is_prime(i) and i >= 13):
            reverse_prime = int(str(i)[::-1])
            if(not reverse_prime <= i and is_prime(reverse_prime)):
                if(not (reverse_prime > number)):
                    accumulator = accumulator + i + reverse_prime
                else:
                    accumulator = accumulator + i

    return accumulator


def emirps():
    for line in fileinput.input():
        for number in line.split():
            if((number.isnumeric() and not(number.startswith('-')))):
                print(count_emirps(int(number)))

emirps()
