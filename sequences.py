#!/usr/bin/env python3
#-*- coding: utf-8 -*-

###
# Name: Alley Busick
# Student ID: 2293544
# Email: busick@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW 3.3
###

#definition
def fibonacci(n):
    lst = [1,1]
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    for i in range(2,n):
        lst.append(lst[i - 1]+lst[i - 2])
    return lst

#program
def main(argv):
    n = int(argv[1])
    print(fibonacci(n))

#protects code
if __name__ == "__main__":
    import sys
    main(sys.argv)