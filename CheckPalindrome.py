# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:24:24 2022

@author: Gururaja Hegde V'
"""

# to check for palindrome
def palindrome(s):
	revS=s[::-1]
	if s==revS:
		print(" The entered string is a palindrome")
	elif s!=revS:
		print(" The entered string is not a palindrome")
	else:
		print("Invalid Input")
	return(s)
if __name__=='__main__':
	usip=input("Enter the string:")
	palindrome(usip)

#redivider, 
#deified
#civic, 
#radar
#level, 
#rotor
#kayak, 
#reviver
#racecar
#madam
#refer