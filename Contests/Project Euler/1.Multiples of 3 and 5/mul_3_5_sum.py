'''
Aurthor: Prathmesh Agrawal
Problem:If we list all the natural numbers 
below 10 that are multiples of 3 or 5 , we get 3,5,6 and 9 . 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N . 
'''
#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
	
	# "//" for integer division
    fact3 = ( n - 1 ) // 3;	#number of factors of 3
    fact5 = ( n - 1 ) // 5;	#number of factors of 5
    #since the LCM of 3 and 5 is 15
	#we take consideration LCM because the LCM would be common in both 5 and 3
	factHCF = ( n - 1 ) // 15;
	
    #taking general formula of sum of n number
	sum3 =  ((fact3) * (2*3 + ((fact3 - 1) * 3))) // 2
    sum5 =  ((fact5) * (2*5 + ((fact5 - 1) * 5 ))) // 2
    sumHCF =  ((factHCF) * (2*15 + ((factHCF - 1) * 15))) // 2
    
	count = sum3 + sum5 - sumHCF
    
	print( int( count ))