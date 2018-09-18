#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3
###
# Name: Gabriella_Nutt
# Student ID: ID_HERE
# Email: nutt@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CLASSWORK_3
###

#n = int(input("hello please type a positive integer!"))

import sys
n = int(sys.argv[1])

def fibonacci(n):

    a, b = 0, 1
    if n < 0:
        print("THIS IS NOT WHAT I ASKED FOR!")

    else:
        #print(a)
        #print(b)
        
        for i in range(n):
            fib= a+b
            a=b
            b=fib
        #print(i)
        return n

def main(argv):
    n = int(argv[1])
    print(fibonacci(n))

if __name__=="__main__":
    import sys
    main(sys.argv)
