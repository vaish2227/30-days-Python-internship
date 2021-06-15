Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hrs challenge")
30 days 30 hrs challenge
>>> 
>>> #Assuming string
>>> hrs=thirty
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hrs=thirty
NameError: name 'thirty' is not defined
>>> hrs="thirty"
>>> print(hrs)
thirty
>>> hrs="thirty"
>>> print(hrs[0])
t
>>> rock="indestrutible"
>>> print(rock[-1])
e
>>> print(rock[3:6])
est
>>> print(rock[-2-5])
r
>>> print(rock[::-1])
elbiturtsedni
>>> print(len(rock))
13
>>> newstr="fgthFjakaA"
>>> print(newstr.lower())
fgthfjakaa
>>> print(newstr.upper())
FGTHFJAKAA
>>> #concatenating str
>>> a="30 days"
>>> b="30 hrs"
>>> print(a+b)
30 days30 hrs
>>> c=a+" " +b
>>> print(c)
30 days 30 hrs
>>> #caseFold
>>> text=""
>>> 
>>> text="Thirty days and Thirty hrs"
>>> print(text.casefold())
thirty days and thirty hrs
>>> text="thirty days and hirty hrs"
>>> print(text.casefold())
SyntaxError: multiple statements found while compiling a single statement
>>> text1="thirty days and hirty hrs"
>>> print(text1.casefold())
SyntaxError: multiple statements found while compiling a single statement
>>> capital="DON'T TROUBLE UNTIL TROUBLE TROUBLES YOU."
>>> y=capital.capatalize()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    y=capital.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'
>>> y=capital.capitalize()
>>> print(y)
Don't trouble until trouble troubles you.
>>> y=capital.find('Y')
>>> print(y)
37
>>> y=capital.isalpha()
>>> print(y)
False
>>> digi=445689
>>> x=digi.isalnum()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x=digi.isalnum()
AttributeError: 'int' object has no attribute 'isalnum'
>>> x=digi.isalpha()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x=digi.isalpha()
AttributeError: 'int' object has no attribute 'isalpha'
>>> digi="34567"
>>> x=digi.isdigit()
>>> print(x)
True
>>> sample="Hello123"
>>> z=sample.isalnum()
>>> print(z)
True
>>> 
