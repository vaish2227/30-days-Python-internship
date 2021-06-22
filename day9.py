Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4,5,6,7]
>>> add_list=[]
>>> for i in list1:
	add_list.append(i+2)

	
>>> print(add_list)
[3, 4, 5, 6, 7, 8, 9]
>>> for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(j,end='')

		
543214321321211
>>> for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(j,end='')
	print()

	
54321
4321
321
21
1
>>> #WAP for Fibonacci series
>>> n=int(input("Enter the number"))
Enter the number 5
>>> count=0
>>> first=1
>>> second=2
>>> temp=0
>>> while count<=n:
	print(first)
	temp = first + second
	first = second
	second = temp
	count = count + 1

	
1
2
3
5
8
13
>>> #WAP for checking armstrong no.
>>> num = int(input("Enter a number: "))
Enter a number: 234
>>> sum = 0
>>> temp = num
>>> while temp > 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

	
>>> if num == sum:
	 print(num,"is an Armstrong number")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> num = int(input("Enter a number: "))
Enter a number: 234
>>> sum = 0
>>> temp = num
>>> while temp > 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10
	if num == sum:
		print(num,"is an Armstrong number")
	else:
		print(num,"is not an Armstrong number")

		
234 is not an Armstrong number
234 is not an Armstrong number
234 is not an Armstrong number
>>> #WAP for table of 9
>>> 
KeyboardInterrupt
>>> for i in range(1,11):
	print("9 X",i,'=',i*9)

	
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90
>>> #WAP for findinf positive and negative
>>> lst=[1,-2,-23,7,-9]
>>> for i in lst:
	if i>0:
		print(i,"is positive")
	else:
		print(i,"is negative")

		
1 is positive
-2 is negative
-23 is negative
7 is positive
-9 is negative
>>> days=int(input())
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    days=int(input())
ValueError: invalid literal for int() with base 10: 'days=int(input())'
>>> days=int(input())

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    days=int(input())
ValueError: invalid literal for int() with base 10: ''
>>> days=int(input())

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    days=int(input())
ValueError: invalid literal for int() with base 10: ''
>>> days=int(input("Enter days:"))
Enter days:1675
>>> year=int(days/365)
>>> print(year,"years ago")
4 years ago
>>> #WAP for trignometry operation
>>> import math
>>> def trignometry(n,m):
	if n=='sin':
		return math.sin(m)
	elif n=='cos':
		return math.cos(m)
	elif n=='cosin':
		return math.cosine(m)
	elif n=='tan':
		return math.tan(m)
	elif n=='sec':
		return math.sec(m)
	elif n=='cosec':
		return math.cosec(m)

	
>>> trignometry('sin',90)
0.8939966636005579
>>> trignometry('cos',90)
-0.4480736161291701
>>> #WAP for Calculator using if-else
>>> def calculate():
	print('+')
	print('-')
	print('*')
	print('/')
	print('%')
	print('**')
	inp_operation=input("Select an operation:")
	print("Enter two numbers:")
	num1=int(input())
	num2=int(input())

	
>>> def calculate():
	print('+')
	print('-')
	print('*')
	print('/')
	print('%')
	print('**')
	inp_operation=input("Select an operation:")
	print("Enter two numbers:")
	num1=int(input())
	num2=int(input())
	if inp_operation=='+':
		print(num1+num2)
	elif inp_operation=='-':
		print(num1-num2)
	elif inp_operation=='*':
		print(num1*num2)
	elif inp_operation=='/':
		print(num1/num2)
	elif inp_operation=='%':
		print(num1%num2)
	elif inp_operation=='**':
		print(num1**num2)
	else:
		print("Invalid Input")

		
>>> calculate()
+
-
*
/
%
**
Select an operation:+
Enter two numbers:
50
56
106
>>> calculate()
+
-
*
/
%
**
Select an operation:-
Enter two numbers:
23
20
3
>>> calculate()
+
-
*
/
%
**
Select an operation:@
Enter two numbers:
22
22
Invalid Input
>>> 
