#-*- codeing: utf-8 -*-

import sys

"""
input
14
1144

output
327714
"""

a = int(input())
b = int(input())

_sum = 0
for x in range(a, b+1):
	if not x % 2:
		_sum += x

print(_sum)