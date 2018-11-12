# -*- coding: utf8 -*-

from time import time

start_time = time()

fib1 = 1
fib2 = 2
result = 2

while True:
	temp = fib1+fib2
	fib1 = temp
	fib2 += fib1

	if fib1 < 4e6:
		if fib1%2 == 0:
			result += fib1
	else:
		break
	
	if fib2 < 4e6:
		if fib2%2 == 0:
			result += fib2
	else:
		break

print(result)
print("İlk Süre %f" % (time() - start_time))

### 2.yol

start_time = time()

fib1 = 1
fib2 = 2
result = 2

while True:
	temp = fib1+fib2
	fib1 = fib2
	fib2 = temp

	if fib2 >= 4e6:
		break
	elif fib2%2 == 0:
		result += fib2

print(result)
print("İkinci Süre %f" % (time() - start_time))