#-*- codeing: utf-8 -*-

import sys

"""
tip
data format
%7.2f  = 7 Numbers(Incude Second decimal place) Align Text to the Right.
%-7.2f = 7 Numbers(Incude Second decimal place) Align Text to the Left.

input:
23.12
395.3
100.4617
564.329

output
|  23.12   395.30|
| 100.46   564.33|
|23.12    395.30 |
|100.46   564.33 |
"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
print('|%7.2f  %7.2f|' % (a, b))
print('|%7.2f  %7.2f|' % (c, d))
print('|%-7.2f  %-7.2f|' % (a, b))
print('|%-7.2f  %-7.2f|' % (c, d))