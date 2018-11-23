# -*- coding: utf8 -*-

from time import time
from math import pow 

check=False

# 1000*c + a*b = 500000'den 

for c in range(500,333,-1):
	for b in range(c-1,0,-1):
		a=1000-c-b
		if a>=b:
			break
		if pow(a,2)+pow(b,2)==pow(c,2):
			print(a,b,c,a*b*c)
			check=True
			break
	if check:
		break