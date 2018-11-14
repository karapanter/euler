# -*- coding: utf8 -*-

# 6 basamaklı en büyük palindrom sayı
from time import time  

start_time = time()

def ispalindrom(number):
	number = str(number)
	if number[0:3] == number[3:][::-1]:
		return True
	else:
		return False

max_p = [0,0,0]
for i in range(999,99,-1):
	for j in range(i,99,-1):
		number = i*j
		if ispalindrom(number):
			if number > max_p[0]:
				max_p = [number,i,j]


print(max_p)

print(time() - start_time)
