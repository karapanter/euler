# -*- coding: utf8 -*-

from time import time
from math import sqrt

start_time=time() 

i=1
triangular=0


while True:
	triangular+=i
	count=0
	sqrt_tri=sqrt(triangular)
	for j in range(1,int(sqrt_tri)+1):
		if triangular % j==0:
			count+=1

	if sqrt_tri==int(sqrt_tri):
		count=count*2-1
	else:
		count*=2

	if count>500:
		break
	i+=1

print(triangular,count)

print(time() - start_time)