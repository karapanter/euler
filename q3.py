# -*- coding: utf8 -*-

number = input("sayiyi girin =")

number = int(number)

i=2

while i <= number:
	if number % i == 0:
		number /= i
	else:
		i +=1

print(i)