#-*- codeing: utf-8 -*-

import sys

"""
tip
type
min()

input
29
100
948
377
-24
0
-388
9999

output
-388
"""
data = []
for x in sys.stdin:
	x = int(x)
	data.append(x)
	if x >= 9999:
		print(min(data))
		break;