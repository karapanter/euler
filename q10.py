# -*- coding: utf8 -*-

# 2 milyondan küçük asal sayıların toplamını bulma

from time import time 
from math import sqrt

start_time=time()

result=2
i=3 # while counter

# iyileştirmek için asal sayıları ararken sadece ondan önceki asal sayılara bölünüp bölünmediğine bakıldı

primes=[]

while i<2000000:
	check=True
	sqrt_i=sqrt(i)
	for j in primes:
		if j>sqrt_i:	# bir sayının asal olup olmadığına bakarken,
			break       # en çok o sayının köküne kadar olan sayılara bölünüp bölünmediğine bakılır (100 için 10-->3,5,7)
		if i%j==0:
			check=False
			break
	if check:
		result+=i 		# (142913828922, 2000001)
		primes.append(i)	
	i+=2

print(result,i)
print(time() - start_time) # 5 saniye