"""
Calculating n digits of Pi using Chudnovsky's algorithm
https://en.wikipedia.org/wiki/Chudnovsky_algorithm
http://www.craig-wood.com/nick/articles/pi-chudnovsky/
"""

from decimal import *
import math, sys
from math import factorial


def calculatePi(k):
    sum = 0
    getcontext().prec = k
    getcontext().rounding = ROUND_FLOOR
    for i in range(k + 1):
        up = factorial(6 * i) * (13591409 + 545140134 * i)
        down = factorial(3 * i) * (factorial(i)) ** 3 * (640320 ** (3 * i))
        sum += up / down
    sum = Decimal(sum)

    pi = Decimal(426880 * math.sqrt(10005))/sum

    return pi


def main():
    sys.setrecursionlimit(100)
    print "PI Calculator \n"
    print "This program can be used to calculate digits of PI upto kth place(max 100)\n"
    while True:
        k = raw_input("How many digits to calculate or quit to exit? ")
        if k.lower() == "quit":
            break
        elif not k.isdigit():
            print "Please enter a number. Try again"
        elif int(k) > 100:
            print "Please enter a number below 100"
        else:
            print calculatePi(int(k))


if __name__ == '__main__':
    main()
