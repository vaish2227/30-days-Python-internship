Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Merge(dict1,dict2):
	return(dict2.update(dict1))

>>> dict1={'a':10, 'b':20}
>>> dict2={'x':30, 'y':40}
>>> print(Merge(dict1,dict2))
None
>>> print(dict2)
{'x': 30, 'y': 40, 'a': 10, 'b': 20}
>>> if 'a' in dict2:
	 del dict2['a']

	 
>>> print(dict2)
{'x': 30, 'y': 40, 'b': 20}
>>> dict1=["pooja","Rutuja"]
>>> dict2=[22,45]
>>> result={}
>>> for key in dict1:
	for value in dict2:
		result[key]=value
		dict2.remove(value)
		break

	
>>> print(result)
{'pooja': 22, 'Rutuja': 45}
>>> My_set={"Chennai","Maharashtra","Bihar"}
>>> print(len(My_set))
3
>>> set1={1,2,3,4,5}
>>> set2={4,5,6,7,8}
>>> set1.diffrence_update(set2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set1.diffrence_update(set2)
AttributeError: 'set' object has no attribute 'diffrence_update'
>>> set1.difference_update(set2)
>>> print(set1)
{1, 2, 3}
>>> 
