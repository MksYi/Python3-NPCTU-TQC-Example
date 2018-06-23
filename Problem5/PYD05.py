#-*- codeing: utf-8 -*-

import sys

"""
input
56
11

output
616
"""

def compute(x, y):
	return x * y

if __name__ == '__main__':
	x = int(input())
	y = int(input())
	print(compute(x, y))