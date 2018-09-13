#!/usr/bin/env python3
#-*- coding: utf-8 -*-

###
# Name: Alley Busick
# Student ID: 2293544
# Email: busick@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW 3.3
###

import sys

n = int(sys.argv[1])

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(n))