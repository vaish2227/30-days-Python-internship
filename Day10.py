Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Bank_Account:
	def __init__(self):
		self.balance=20000
		print("Hello!!!")
	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)
	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance  ")
	def display(self):
		print("\n Net Available Balance=",self.balance)

		
>>> class Info(Bank_Account):
	name=input("Enter name:")
	acc=int(input("Enter Account no.:"))
	print("Acccount Holder is:",name)
	print("Acc no.:",acc)

	
Enter name:Vaishnavi
Enter Account no.:5649909018820
Acccount Holder is: Vaishnavi
Acc no.: 5649909018820
>>> s = Info()
Hello!!!
>>> s.deposit()
Enter amount to be Deposited: 20000

 Amount Deposited: 20000.0
>>> s.withdraw()
Enter amount to be Withdrawn: 5000

 You Withdrew: 5000.0
>>> s.display()

 Net Available Balance= 35000.0
>>> 
