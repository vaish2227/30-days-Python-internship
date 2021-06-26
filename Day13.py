Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> def isallow(string):
	charRe=re.compile(r'[^a-zA-Z0-9.]')
	string=charRe.search(string)
	return not bool(string)

>>> print(isallow("ABCDEFabcdef123450"))
True
>>> print(isallow("1233@@#$$%$"))
False
>>> #WAP that matches a word having ab

>>> def text_match(text):
	patterns='\w*ab.\w*'
	if re.search(patterns,text):
		return 'match found'
	else:
		return 'match not found'

	
>>> print(text_match("Python program"))
match not found
>>> print(text_match("ababbbabbab"))
match found
>>> #WAP to check for a number at the end of word
>>> def end(string):
	text=re.compile(r".*[0-9]$")
	if text.match(string):
		return True
	else:
		return False

	
>>> print(end("dfgh9"))
True
>>> print(end("asdfghjk5678"))
True
>>> print(end("67hohh70hh"))
False
>>> print(end("avd"))
False
>>> #WAP to search the numbers(0-9)of length between 1 to 3 in a string
>>> results=re.finditer(r"([0-9]{1,3})","Exercises number 1,9,11 and 222 are imp")
>>> print("Numbers of length 1 to 3")
Numbers of length 1 to 3
>>> for n in results:
	print(n.group(0))

	
1
9
11
222
>>> #WAP to match string that contains only uppercase letter
>>> def text_check(text):
	patterns='^[a-zA-Z0-9_]*$'
	if re.search(patterns,text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> print(text_check("hlw all"))
Match not found
>>> print(text_check("Hlw World"))
Match not found
>>> print(text_check("Hlw_World"))
Match found
>>> 
