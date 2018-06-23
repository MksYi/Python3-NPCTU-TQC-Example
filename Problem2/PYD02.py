#-*- codeing: utf-8 -*-

import sys

"""
input
55
36
92
15

output
55 is a multiple of 5.
36 is a multiple of 3.
92 is not a multiple of 3 or 5.
15 is a multiple of 3 and 5.

"""

number = int(input())

anwser = 0

if not number % 3:
	anwser += 3
if not number % 5:
	anwser += 5

if anwser == 3:
	print('%d is a multiple of 3.' %(number))
elif anwser == 5:
	print('%d is a multiple of 5.' %(number))
elif anwser == 8:
	print('%d is a multiple of 3 and 5.' %(number))
else:
	print('%d is not a multiple of 3 or 5.' %(number))
