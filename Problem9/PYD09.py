#-*- codeing: utf-8 -*-

import sys

"""
input
None

output
660
"""

if __name__ == '__main__':
	_sum = 0
	with open('./read.txt') as f:
		for line in f:
			data = line.split(' ')
			data = [int(x) for x in data]
			_sum = sum(data)

	print(_sum)



