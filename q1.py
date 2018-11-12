# -*- coding: utf8 -*-

from time import time

start_time = time()

result = 0	# brute force 

for i in range(3,1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i

print(result)
print(time() - start_time)


start_time = time()
r3 = 0	# 3 + 5 - 15 
r5 = 0
r15 = 0

for i in range(1,334):
	r3 += i*3 

for i in range(1,200):
	r5 += i*5 

for i in range(1,67):
	r15 += i*15 

print(r3+r5-r15)
print(time() - start_time)


start_time = time()	# terim toplamı 


def sumof(fterm,lterm,accrual):
	return ((lterm-fterm)/accrual +1) * ((lterm+fterm)/2)

result = sumof(3,999,3) + sumof(5,995.,5) - sumof(15,990.,15)

print(result)
print(time() - start_time)