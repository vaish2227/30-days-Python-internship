Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #create fumction getting two integers from user and print addition,subtraction,multiplication,division.
>>> def inp():
	a=int(input("Enter Fisrt no."))
	b=int(input("Enter second no."))
	print("Addition of",a,"and",b,"is",a+b)
	print("Subtraction of",a,"and",b,"is",a-b)
	print("Division of",a,"and",b,"is",a/b)
	print("Multiplication of",a,"and",b,"is",a*b)

	
>>> inp()
Enter Fisrt no.40
Enter second no.50
Addition of 40 and 50 is 90
Subtraction of 40 and 50 is -10
Division of 40 and 50 is 0.8
Multiplication of 40 and 50 is 2000
>>> def covid():
	p_name=input("Enter Patient Name:")
	body_temp=input("Body Temprature:")
	default=98
	if not body_temp:
		body_temp=default
	print("Patient name is:",p_name)
	print("Body Temprature is:",body_temp)

	
>>> covid()
Enter Patient Name:vaishnavi
Body Temprature:88
Patient name is: vaishnavi
Body Temprature is: 88
>>> covid()
Enter Patient Name:pooja
Body Temprature:
Patient name is: pooja
Body Temprature is: 98
>>> 
