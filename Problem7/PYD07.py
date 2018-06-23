#-*- codeing: utf-8 -*-

import sys

"""
tip
type
strip()
sort()
str.join()
str.format()

input
9
0
-1
3
8
-9999
28
16
39
56
78
88
-9999

output
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
"""

if __name__ == '__main__':
	data = []
	for x in range(2):
		for n in sys.stdin:
			if int(n) == -9999:
				break
			n = n.strip('\n')
			data.append(n)

	before = ', '.join(data)
	data = [int(x) for x in data]
	data.sort()
	print("Combined tuple before sorting: ({})".format(before))
	print('Combined list after sorting: {}'.format(data))



