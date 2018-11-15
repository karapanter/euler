# -*- coding: utf8 -*-

# 20 ye kadar tüm sayılara tam bölünen en küçük sayı
# ekok

from time import time  

start_time = time()

product=1

numbers=range(2,21)
i=2

while True:
	check=False
	for j,item in enumerate(numbers):
		if item %i ==0:
			check=True
			numbers[j]/=i
			if numbers[j]==1:			# sayının böleni kalmadığında diziden silinir
				del numbers[j]

	if not check:
		if i<20:
			i+=1
		else:
			break
	else:
		product*=i

print(product)

print(time() - start_time)
	
