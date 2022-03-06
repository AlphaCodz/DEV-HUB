"""
Hisses

Developed in 1990, Python is one of the most popular general-purpose programming languages in modern times.


The term “general-purpose” simply means that Python can be used for a variety of applications and does not focus on any one aspect of programming. 
"""

	To display Strings (group of characters enclosed in single or double quotes) 
print('Hello World') // Hello World
print("Hello World") // Hello World

	To display Numbers
print(50) // 50
print(1000) // 1000
print(3.142) // 3.142

	To display multiple data
print(50, 1000, 3.142, "Hello World", 'hello') # 50, 1000, 3.142, Hello World, hello 

By default Python prints 'print'  statements on new lines hence to join these 'print'  statements use the 'end'  attribute with whatever value you wish.
Use case:
print("Hello, come",  end=" ")
print("World") // Hello, come World

print("Hello", end=" ")
print("World") // Hello World

print("Hello", end="") 
print("World") // HelloWorld

	To Comment using the  hash (#)  for single-line and triple quotations """ """ for multi-line
Use case:
print(50)  # This line prints 50
print("Hello World")  # This line prints Hello World

# This is just a comment hanging out on its own!

# For multi-line comments, we must
# add the hashtag symbol
# each time or 
"""
Use triple quotes

"""

	Python has three main data types:
	
Numbers (2, 3.142, 1000)

Strings ("Hello", 'Dev hub', "Dev hub") 

Booleans (true, false) 

	<h4>	Variables  </h4>
	Variables are mutable. Hence, the value of a variable can always be updated or replaced.
	
Naming convention:

Numbers must not begin a variable name but can appear anywhere else: For example, 12income✖️ is not a valid name but income12✔️ or in12come✔️ are valid.

Case sensitivity: For example, Income and income are two different variables and not one.
You can define your income variable as Income or income, both are valid.

Underscores can appear anywhere: For example, _income or income_ are valid name, monthly_income is a valid name.

Variables must give meaningful information: For example, inc or even income would not give any useful information but names like weekly_income, monthly_income, or annual_income explain the purpose of our defined variable. 