Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def starts_w_p():
	word= input('"Enter a word that starts with P:"')
	if word.upper().startswith("P"):
		print(word, "does start with P.")

		
>>> def starts_w_p():
	word= input('"Enter a word that starts with P:"')
	if word.upper().startswith("P"):
		print(word, "does start with P.")
	else:
		print(word, "does not start with P.")

		
>>> starts_w_p()
"Enter a word that starts with P:"pineapple
pineapple does start with P.
>>> starts_w_p()
"Enter a word that starts with P:"buy
buy does not start with P.
>>> starts_w_p()
"Enter a word that starts with P:"Perfect
Perfect does start with P.
>>> def float_func()
SyntaxError: invalid syntax
>>> def even_or_odd():
	num= input("Enter an integer:")
	num=int(num)
	if int(num)%2 >0:
		print("Your number is even.")

		
>>> def even_or_odd():
	num= input("Enter an integer:")
	num=int(num)
	if int(num)%2 >0:
		print("Your number is even.")
	else:
		print("Your number is odd.")

		
>>> even_or_odd()
Enter an integer:12
Your number is odd.
>>> def even_or_odd():
	num= input("Enter an integer:")
	num=int(num)
	if int(num)%2 = 0:
		print("Your number is even.")
	else:
		print("Your number is odd.")
		
SyntaxError: invalid syntax
>>> def even_or_odd():
	num= input("Enter an integer:")
	num=int(num)
	if int(num)%2 > 0:
		print("Your number is odd.")
	else:
		print("Your number is even.")

		
>>> even_or_odd()
Enter an integer:12
Your number is even.
>>> even_or_odd()
Enter an integer:13
Your number is odd.
>>> def beer_func():
	beer= input("What beer would you like?")
	if beer.lower().startswith("b"):
		print("Your beer will cost $5.00")
	elif beer.lower().startswith("c"):
		print("Your beer will cost $4.25.")
	else:
		print("Your beer will cost $8.00.")

		
>>> beer_func()
What beer would you like?bud light
Your beer will cost $5.00
>>> beer_func()
What beer would you like?corona
Your beer will cost $4.25.
>>> beer_func()
What beer would you like?lagunitas
Your beer will cost $8.00.
>>> def sales_price():
	cost= input("What's the cost of the item you wish to purchase?")
	cost= float(cost)
	if cost > 100:
		print("Your total will be $50 today.")
	elif cost > 50:
		print("Your total will be $25 today.")
	else:
		print("Your total will be $10 today.")

		
>>> sales_price()
What's the cost of the item you wish to purchase?125'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sales_price()
  File "<pyshell#54>", line 3, in sales_price
    cost= float(cost)
ValueError: could not convert string to float: "125'"
>>> sales_price()
What's the cost of the item you wish to purchase?125
Your total will be $50 today.
>>> sales_price()
What's the cost of the item you wish to purchase?60
Your total will be $25 today.
>>> sales_price()
What's the cost of the item you wish to purchase?45
Your total will be $10 today.
>>> def resume_build():
	advice= input("What would you like to work on today with your resume?")
	print(advice, "Yes, we can definitely work on that today!")

	
>>> resume_build()
What would you like to work on today with your resume?highlighting key experiences 
highlighting key experiences  Yes, we can definitely work on that today!
>>> max(1,2,3)
3
>>> max("a","b","c")
'c'
>>> def max_func():
	num1= input("What's your first number?")
	num1= float(num1)
	num2= input("What's your second number?")
	num2= float(num2)
	num3= input("What's your third number?")
	num3= float(num3)
	maxnum= max(num1, num2, num3)
	print(str(maxnum), "is the maximum value.")

	
>>> max_func()
What's your first number?3
What's your second number?10
What's your third number?4
10.0 is the maximum value.
>>> d
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d
NameError: name 'd' is not defined
e
>>> def maximum_letter():
	word1= input("What's your first word?")
	word2= input("What's your second word?")
	word3= input("What's your third word?")
	maxword= max(word1, word2, word3)
	print(maxword, "is the last of the words alphabetically.")

	
>>> maximum_letter()
What's your first word?tiger
What's your second word?apple
What's your third word?heart
tiger is the last of the words alphabetically.
>>> def min_func():
	num1= input("What's your first number?")
	num1= float(num1)
	num2= input("What's your second number?")
	num2= float(num2)
	num3= input("What's your third number?")
	num3= float(num3)
	minnum= min(num1, num2, num3)
	print(str(minnum), "is the minimum value.")

	
>>> min_func()
What's your first number?4
What's your second number?8
What's your third number?6
4.0 is the minimum value.
>>> def min_word():
	word1= input("What's your first word?")
	word2= input("What's your second word?")
	word3= input("What's your third word?")
	minword= min(word1, word2, word3)
	print(minword, "is the first word in alphabetical order.")

	
>>> min_word()
What's your first word?banana
What's your second word?painting
What's your third word?moose
banana is the first word in alphabetical order.
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(abs(num))
	else:
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value
		      
SyntaxError: EOL while scanning string literal
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(abs(num)))
	else:
		print("your number was negative and the absolute value is," str(abs(num)))
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(abs(num)))
	else:
		print("your number was negative and the absolute value is," str(abs(num)))
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", abs(num))
	else:
		print("your number was negative and the absolute value is," abs(num))
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", abs(num))
	else:
		print("your number was negative and the absolute value is," abs(num))
		      
SyntaxError: invalid syntax
>>> abs(12)
		      
12
>>> abs(-12)
		      
12
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", absnum)
	else:
		print("your number was negative and the absolute value is," absnum)
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(absnum))
	else:
		print("your number was negative and the absolute value is," (absnum))

		      
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(absnum))
	else:
		print("your number was negative and the absolute value is," str(absnum))
		      
SyntaxError: invalid syntax
>>> 
		      
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(absnum))
	else:
		print("your number was negative and the absolute value is," (absnum))

		      
>>> abs_func(_)
		      
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    abs_func(_)
TypeError: abs_func() takes 0 positional arguments but 1 was given
>>> abs_func()
		      
What's the number you'd like to test?12
your number was already positive and the absolute value is 12.0
>>> abs_func()
		      
What's the number you'd like to test?-12
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    abs_func()
  File "<pyshell#127>", line 8, in abs_func
    print("your number was negative and the absolute value is," (absnum))
TypeError: 'str' object is not callable
>>> float(12)
		      
12.0
>>> abs(float(-12))
		      
12.0
>>> float(-12)
		      
-12.0
>>> abs(-12.0)
		      
12.0
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(absnum))
	else:
		print("your number was negative and the absolute value is," absnum)
		      
SyntaxError: invalid syntax
>>> def abs_func():
	num= input("What's the number you'd like to test?")
	num= float(num)
	absnum= abs(num)
	if num > 0:
		print("your number was already positive and the absolute value is", str(absnum))
	else:
		print("your number was negative and the absolute value is," str(absnum))
		      
SyntaxError: invalid syntax
>>> def abs_func(num1):
	absnum1= abs(num1)
	print("The absolute value of your number is", absnum1)

	
>>> abs_func(1)
		      
The absolute value of your number is 1
>>> abs_func(-1000)
		      
The absolute value of your number is 1000
>>> def accepted():
	decision= input("Should we accept this applicant?")
	if decision.lower().startswith("y"):
		print("Congratulations! You have been accepted!")
	else:
		print("I regret to inform you that we could not accept you.")

		      
>>> accepted()
		      
Should we accept this applicant?Yes
Congratulations! You have been accepted!
>>> accepted()
		      
Should we accept this applicant?NO
I regret to inform you that we could not accept you.
>>> def accepted():
	decision= input("Should we accept this applicant?")
	if decision.lower().startswith("y"):
		print("Congratulations! You have been accepted!")
	elif decision.lower().startswith("n"):
		print("I regret to inform you that we could not accept you.")
	else:
		print("You have been waitlisted.")

		      
>>> accepted()
		      
Should we accept this applicant?YES
Congratulations! You have been accepted!
>>> accepted()
		      
Should we accept this applicant?No
I regret to inform you that we could not accept you.
>>> accepted()
		      
Should we accept this applicant?Maybe
You have been waitlisted.
>>> def max_sum():
	num1= input("What's your first number?")
	num2= input("What's your second number?")
	num3= input("What
		    
SyntaxError: EOL while scanning string literal
>>> sdef max_sum():
	num1= input("What's your first number?")
	num2= input("What's your second number?")
	num3= input("What's your third number?")
		    
SyntaxError: invalid syntax
>>> def max_sum():
	num1= input("What's your first number?")
	num2= input("What's your second number?")
	num3= input("What's your third number?")
	sum1= float(num1)+float(num2)
	sum2= float(num1)+float(num3)
	sum3= float(num2)+float(num3)
	maxsum= max(sum1, sum2, sum3)
	print("Thhe max sum is", maxsum)

		    
>>> max_sum
		    
<function max_sum at 0x00F5C1E0>
>>> max_sum()
		    
What's your first number?10
What's your second number?20
What's your third number?29
Thhe max sum is 49.0
>>> def min_sum()
		    
SyntaxError: invalid syntax
>>> def minsum():
	num1= input("What's your first number?")
	num2= input("What's your second number?")
	num3= input("What's your third number?")
	sum1= float(num1)+float(num2)
	sum2= float(num1)+float(num3)
	sum3= float(num2)+float(num3)
	minsum= min(sum1, sum2, sum3)
	print("The minimum sum is", minsum)

		    
>>> minsum()
		    
What's your first number?18
What's your second number?29
What's your third number?57
The minimum sum is 47.0
>>> 
		    
>>> def minword():
	word1= input("What's the first word?")
	word2= input("What's the second word?")
	word3= input("What's the third word?")
	minword= min(word1, word2, word3)
	print(minword, "is the first word alpabetically.")

		    
>>> minword()
		    
What's the first word?banana
What's the second word?shirt
What's the third word?apple
apple is the first word alpabetically.
>>> def nameageschool():
	name= input("What's your name?")
	age= input("What's your age?")
	school1= input("What's your first school?")
	school2= input("What's your second school?")
	school3= input("What's your third school?")
	minschool= min(school1, school2, school3)
	print("Name:", name, "\nAge:", str(age), "\nFirst Choice School:", minschool)

		    
>>> nameageschool()
		    
What's your name?AJ
What's your age?24
What's your first school?University of Arizona
What's your second school?Berkeley
What's your third school?Yale
Name: AJ 
Age: 24 
First Choice School: Berkeley
>>> def housechoice():
	name= input("What's your name?")
	place= input("What location are you looking into?")
	price= input("What's your budget?")
	price= float(price)
	if price > 500000:
		print(name, "I'm sure we can find a house at", str(price), "in", place)
	elif price < 500000 and price > 200000:
		print(name, "I'm sure we can find a house at", str(price), "in", place)
	else:
		print(name, "I'm sure we can find a rental at your budget of", str(price), place)

		    
>>> housechoice()
		    
What's your name?AJ
What location are you looking into?750000
What's your budget?
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    housechoice()
  File "<pyshell#217>", line 5, in housechoice
    price= float(price)
ValueError: could not convert string to float: 
>>> housechoice()
		    
What's your name?AJ
What location are you looking into?Bay Area
What's your budget?750000
AJ I'm sure we can find a house at 750000.0 in Bay Area
>>> housechhoice()
		    
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    housechhoice()
NameError: name 'housechhoice' is not defined
>>> housechoice()
		    
What's your name?AJ
What location are you looking into?Tucson
What's your budget?300000
AJ I'm sure we can find a house at 300000.0 in Tucson
>>> housechoice()
		    
What's your name?AJ
What location are you looking into?Bay Area
What's your budget?190000
AJ I'm sure we can find a rental at your budget of 190000.0 Bay Area
>>> def count():
	count= 0
	while (count<9):
		print ("The count is", count)
		count= count +1

		    
>>> count()
		    
The count is 0
The count is 1
The count is 2
The count is 3
The count is 4
The count is 5
The count is 6
The count is 7
The count is 8
>>> def count_less():
	count = 0
	while (count <5):
		print("The count is less than 5.")
		count = count + 1
	else:
		print("The count is not less than 1.")

		    
>>> count_less()
		    
The count is less than 5.
The count is less than 5.
The count is less than 5.
The count is less than 5.
The count is less than 5.
The count is not less than 1.
>>> def countdown():
	count= 31
	while (count > 14):
		print("You have", count, "days til school starts.")
		count = count -1
	else:
		print("You have less than 2 weeks til school starts.")

		    
>>> countdown()
		    
You have 31 days til school starts.
You have 30 days til school starts.
You have 29 days til school starts.
You have 28 days til school starts.
You have 27 days til school starts.
You have 26 days til school starts.
You have 25 days til school starts.
You have 24 days til school starts.
You have 23 days til school starts.
You have 22 days til school starts.
You have 21 days til school starts.
You have 20 days til school starts.
You have 19 days til school starts.
You have 18 days til school starts.
You have 17 days til school starts.
You have 16 days til school starts.
You have 15 days til school starts.
You have less than 2 weeks til school starts.
>>> 44610+5000+600+3000+2500
		    
55710
>>> def count():
	count = 0
	while (count < 6):
		print("The count is", count)
		count = count +0.5
	else:
		print("The count is more than 6.")

		    
>>> count()
		    
The count is 0
The count is 0.5
The count is 1.0
The count is 1.5
The count is 2.0
The count is 2.5
The count is 3.0
The count is 3.5
The count is 4.0
The count is 4.5
The count is 5.0
The count is 5.5
The count is more than 6.
>>> 
