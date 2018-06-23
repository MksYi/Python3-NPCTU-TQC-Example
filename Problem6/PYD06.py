#-*- codeing: utf-8 -*-

import sys

"""
tip
list.index()

input
5
10
K
3
A

output
32
"""

if __name__ == '__main__':
	key = ['0','A','2','3','4','5','6','7','8','9','10','J','Q','K']
	_in = []
	_sum = 0
	for x in range(5):
		_sum += key.index(input())
	print(_sum)

