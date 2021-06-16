Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[2,3,4,5]
>>> def add(l1):
	l1.append(6)
	print(l1)

	
>>> add(l1)
[2, 3, 4, 5, 6]
>>> l2=[2,3,4,5]
>>> def dele(l2):
	l2.pop(2)
	print(l2)

	
>>> dele(l2)
[2, 3, 5]
>>> l3=[2,3,4,5,6]
>>> a=max(l3)
>>> print(a)
6
>>> l4=[2,3,4,5,6]
>>> b=min(l4)
>>> print(b)
2




