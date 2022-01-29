# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:43:39 2022

@author: Gururaja Hegde V'
"""

def rev1(s):
	str=""
	for i in s:
		str=i+str
	return(str)
s=input("Enter the string to be reversed:")
print(" The reversed string using the for loop is:",rev1(s))


def rev2(s):
	print("The string to be reversed(Type 2) is:",s)
	return(s[::-1])
print("The string to be reversed using extended slicing:",rev2(s))

def rev3(s):
	print(" The string to be reversed(Type 3) is:",s)
	return ''.join(reversed(s))
print("The string to be reversed using built in function reversed is:",rev3(s))





