Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Merge(dict1,dict2):
	return(dict2.update(dict1))
dict1={'a':10, 'b':20}
SyntaxError: invalid syntax
>>> def Merge(dict1,dict2):
	return(dict2.update(dict1))

>>> dict1={'a':10, 'b':20}
>>> dict2={'x':30, 'y':40}
>>> print(Merge(dict1,dict2))
None
>>> print(dict2)
{'x': 30, 'y': 40, 'a': 10, 'b': 20}
>>> list1=[2,35,32,12,13,31,77]
>>> list1.sort()
>>> print(list1)
[2, 12, 13, 31, 32, 35, 77]
>>> set1=set(list1)
>>> print(set1)
{32, 2, 35, 12, 13, 77, 31}
>>> #Write a python program to get string from a given string and change the first occurrence
>>> inp=input("Enter string:")
Enter string:Hello
>>> word=",Vaishnavi"
>>> print(inp+word)
Hello,Vaishnavi
>>> #Capitalize the first occurrence
>>> string1=input("Enter string:")
Enter string:doll
>>> string2=string1.capitalize()
>>> print(string2)
Doll
>>> #WAP to find repeated elements in list
>>> def repeat(x):
	length=len(x)
	ele_repeated=[]
	for i in range(length):
		temp=i+1
		for j in range(temp,length):
			if x[i]==x[j] and x[i] not in ele_repeated:
				ele_repeated.append(x[i])
	return ele_repeated

>>> list1=[10,20,20,11,12,3220,23,11,334,32,11]
>>> print(repeat(list1))
[20, 11]
>>> #WAP to check sum of 3 integer and divide by input value given by user
>>> a=int(input("Enter first digit:"))
Enter first digit:4
>>> b=int(input("Enter second digit:"))
Enter second digit:5
>>> c=int(input("Enter third digit:"))
Enter third digit:5
>>> add=a+b+c
>>> add_input=int(input("Enter the number to divide sum value:"))
Enter the number to divide sum value:7
>>> if add%add_input==0:
	print("input divided")

    
input divided
>>> if add%add_input==0:
	print("input divided")

	
input divided
>>> if add%add_input==0:
	
KeyboardInterrupt
>>> if add%add_input==0:
	print("input divided")

input divided
>>> else:
	
SyntaxError: invalid syntax
>>> def mean1():
	mean_list=[2,3,4,5,6]
	length=len(mean_list)
	sum1=sum(mean_list)
	mean=sum1/length
	print(mean)

	
>>> mean1()
4.0
>>> def median():
	med_list=[1,2,3,4,5]
	length=len(med_list)
	if length%2==0:
		med1=med_list[length//2]
		med2=med_list[length//2-1]
		med=(med1+med2)/2
	else:
		med=med_list[length//2]
	print(med)

	
>>> median()
3
>>> w1="Hello"
>>> w2="World"
>>> temp=w1
>>> w1=w2
>>> w2=temp
>>> print(w1,w2)
World Hello
>>> 
