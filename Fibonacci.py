# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:27:50 2022
@author: Gururaja Hegde V'
"""

"""Write a program to generate Fibonnaci numbers. 
The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

def gen_fib1():
	count=int(input("Gen_fib_1- How many fibonacci numbers would you like to generate?:"))
	i=1
	if count==0:
		fib=[]
	elif count==1:
		fib=[1]
	elif count==2:
		fib=[1,1]
	elif count>2:
		fib=[1,1]
		while i<(count-1):
			fib.append(fib[i]+fib[i-1])
			i+=1
	return fib



def gen_fib2():
	num=int(input("Gen_fib_2- How many fibonacci numbers would you like to generate:"))
	i=1
	if num==0:
		fib=[]
	elif num==1:
		fib=[1]
	elif num==2:
		fib=[1,1]
	elif num>2:
		fib=[1,1]
		while i<(num-1):
			fib.append(fib[i]+fib[i-1])
			i+=1
	return fib



def gen_fib3():
    n =int(input("Gen_fib_3- How many fibonacci numbers would you like to generate:"))
    f=[]
    f.append(1)
    f.append(1)
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    print(f)



""" Type 4 """
# 1. Take the number of terms from the user and store it in a variable.
# 2. Pass the number as an argument to a recursive function named fibonacci.
# 3. Define the base condition as the number to be lesser than or equal to 1.
# 4. Otherwise call the function recursively with the argument as the number minus
# 1 added to the function called recursively with the argument as the number minus 2.
# 5. Use a for loop and print the returned value which is the fibonacci series.
# 6. Exit. 


def gen_fib4(n):
    if(n <= 1):
        return n
    else:
        return(gen_fib4(n-1) + gen_fib4(n-2))
n = int(input("Enter number of terms for fibon:"))
print("Fibonacci sequence:")
for i in range(n):
    print(gen_fib4(i))
    
print(gen_fib1())
print(gen_fib2())
print(gen_fib3())

	