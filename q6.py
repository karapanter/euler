# -*- coding: utf8 -*-

# 100 e kadar olan sayıların toplamlarının karesinden (squareOfSum)
# 100 e kadar olan sayıların karelerinin toplamının çıkarılması (sumOfSquare)

from time import time 
from math import pow 

start_time = time()

def sumOfSquare(n):
	return ( n*(n+1)*(2*n+1) )/6

def squareOfSum(n):
	return pow(( n*(n+1)/2 ),2)	
	
number = input("sayiyi girin =")
number = int(number)

print(squareOfSum(number)-sumOfSquare(number))

print(time() - start_time)