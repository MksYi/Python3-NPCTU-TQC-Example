#-*- codeing: utf-8 -*-

import sys

"""
tip
ord()
chr()

input
Kingdom

output
ASCII code for 'K' is 75
ASCII code for 'i' is 105
ASCII code for 'n' is 110
ASCII code for 'g' is 103
ASCII code for 'd' is 100
ASCII code for 'o' is 111
ASCII code for 'm' is 109
713
"""

if __name__ == '__main__':
	_str = input()
	_sum = 0
	for x in _str:
		print('ASCII code for \'%s\' is %d' %(x, ord(x)))
		_sum += ord(x)
	print(_sum)



