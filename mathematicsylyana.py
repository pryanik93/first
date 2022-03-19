#!/usr/bin/env python3
import random
import os
from num2words import num2words

n = 0

def main():
	global n
	a = random.randint(0,20)
	b = random.randint(0,20)
	plus = a+b
	minus = a-b
	action = [plus, minus]
	if a < b:
		c = plus
	else:
		c = random.choice(action)
	if c == plus:
		print(num2words(a, lang='ru'), "плюс", num2words(b, lang='ru'), "равно")
		#print(num2words(a, lang='pt'), "mais", num2words(b, lang='pt'), "é igual a")
		#print(num2words(a, lang='en'), "plus", num2words(b, lang='en'), "equal")
		print(a, "+", b, "=")
	else:
		print(num2words(a, lang='ru'), "минус", num2words(b, lang='ru'), "равно")
		#print(num2words(a, lang='pt'), "menos", num2words(b, lang='pt'), "é igual a")
		#print(num2words(a, lang='en'), "minus", num2words(b, lang='en'), "equal")
		print(a, "-", b, "=")
	value = int(input())
	if n == 19:
		os.system('cls||clear')
		print("Молодец! Возьми огурец")
		exit(1)
	else:
		if value == c:
		  n += 1
		  os.system('cls||clear')
		  print(num2words(n, lang='en'))
		  print("")
		  return(n)
		else:
		  n -= 2
		  os.system('cls||clear')
		  print(num2words(n, lang='en'))
		  return(n)

os.system('cls||clear')

while n < 20:
	main()
