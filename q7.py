# -*- coding: utf8 -*-

# 10.001 inci asal sayı

from time import time 

start_time=time()

count=1
i=3 # while counter

# iyileştirmek için asal sayıları ararken sadece ondan önceki asal sayılara bölünüp bölünmediğine bakıldı
# iyileştirmeden önceki süre: 36 saniye, iyileştikten sonra:5 saniye

primes=[]

while True:
	check=True
	for j in primes:
		if i%j==0:
			check=False
			break
	if check:
		count+=1
		primes.append(i)
		if count == 10001:
			break
	i+=2

print(i)
print(time() - start_time)
