"""
Python Language Overview

All languages have different formats which they expect code to be in. These formats are called 'syntax' and the syntax
for Python is somewhat unique compared to some other languages. Keep this uniqueness in mind when learning python, but
also know that with a solid foundation in how programming languages function, learning the syntax of a new one is easier
than it sounds.

Python is a top-down scripting language, meaning it's simple to start using and easier to understand than some other
languages. This allows us to get to writing the functionality of a script very quickly and without much or any overhead
code to worry about. Each line in python is typically considered it's own 'statement' and unlike most other languages,
the whitespace in python matters. Statements end when the line they're on ends, and don't need to end in semicolons like
 other languages. Some 'control structures' will require a colon to indicate what it should do (we'll discuss this in
detail later). A statement can be things such as creating/modifying a variable or calling a function.
"""

"""
Syntax

Python's syntax uses whitespace (tab or space characters) to divide code into 'blocks'. Other languages typically only
use whitespace for readability, but in python it's part of the code's structure.
"""

# The 'print' statement is within the 'if' statement's block of code, so it should be indented.
# This is usually done using TAB, which either uses tab characters or a set number of space characters.
# The number of space characters is not specified, but standard is 1 tab or a multiple of 4 spaces.
if 1 > 0:
	print('One is greater than zero')
	print('Zero is less than one')

# For example, this print statement isn't indented, so the if statement has no block of code to run, so it causes a
# 'syntax error' meaning the code is formatted incorrectly.
"""
if 1 > 0:
print('One is greater than zero')
"""

# In this example, we aren't using consistent spacing for the block of code, so that also causes a syntax error.
"""
if 1 > 0:
	print('One is greater than zero')
		print('Zero is less than one')
"""

# We can create variables by naming it and assigning a value
# We'll go over variables in more detail later.
some_number = 42
trains = 'I like trains!'

"""
Comments

Comments are used to annotate code, or to prevent it from executing since anything in a comment is ignored by Python.
This is an example of a multi-line comment using triple quotes (can use double or single).

Single line comments start with a '#' character and anything after that character is part of the comment.
"""

# A comment can be on its own line
print('Hello World!')  # Or on the end of a line of code

# They can also be used to 'comment out' a line of code so it doesn't run like the line below.
# print('Hello World')

"""
If we wanted to comment many lines at once
we can use a multi line comment
like this.
"""

"""
Variables

Creating variables in Python is as simple as assigning a value to one. Where most languages require specific commands or
type specifiers to create a variable, python doesn't. A variable just has to start with an alphabetical character,
underscore, or dash, and can be made up of any alphanumeric characters, underscores, and dashes. There are several
naming conventions for variables, and you can use any of them, but consistency is key.

snake_case	-	Typically used for variable and function names
camelCase	-	Rarely used in python, but sometimes used instead of snake case
PascalCase	-	Typically used for class names

Keep in mind that there are many 'reserved' words or 'keywords' in python. These words represent actual functions or
constant values so variable names should never mirror these names. For example, you should never try to make a variable
named 'print' as that would override the 'print' function in python.
"""

age = 25  # The age variable is of type 'int'
name = 'Caleb'  # The name variable is of type 'str' (string)
Name = 'Caleb Marcum'  # Note that variables are case sensitive so Name and name are different variables
print(age)
print(name)
print(Name)

# I can reassign and modify the values of variables as well
age = 30
age = age + 1

# Additional note: Strings can be created using single or double quotes, and it's up to personal preference.
# Sometimes it may be useful to use one over the other such as to include the other type of quotes in the string easier
print('A wise man once said,"I like trains". Truly, he was a wise man.')
# We'll go into more detail on formatting strings for more useful tricks later.

"""
Types

While we don't need to specify the types of variables in Python, all variables still have types. In Python, we can
assign values of one type to a variable which is a different type and there's no problem (just remember what you did to
avoid confusion). However, sometimes we want to convert a value from one type to another, a process called 'casting' or
'type casting'.
"""

age_string = str(25)  # age_string is a string '25'
age_value = int(25)  # age_value is an integer 25
age_in_months = float(25*12)  # age_in_months if a floating point number equal to 25 times 12

# Besides type casting, we can also get the type of a variable in Python
print(type(age_string))
print(type(age_value))
print(type(age_in_months))

"""
Data Types

As we saw above, there are several types of variables in Python, and these are called data types. Most languages have a
lot of the same basic or 'primitive' types, and then there are a few unique ones. Here are some of the commonly used
primitive and a few complex types in Python:

bool	-	Boolean, used to indicate True or False, and is the type required for 'control logic'
str		-	String, this is used for text
int		-	Integer, used for whole numbers
float	-	Floating point number (anything with a decimal)
list	-	List of ordered values (complex type)
dict	-	Dictionary, similar to a list, but instead of ordered values, they are key, value pairs (complex type)
None	-	(NoneType) None, Null, Nill, etc. This is the type of something not yet given a value

There are plenty more types in Python and other languages, both primitive and non-primitive. Something to note though,
is that the non-primitive types are created using combinations of the primitive types of the language. Furthermore,
trying to perform operations such as math on values of differing types can sometimes cause errors or give unexpected
results.
"""

# This example would cause an error, as we're trying to add an int and a string which is not defined functionality
x = 10
y = '10'
"""
print(x + y)
"""

# This example will convert the integer 10 into a string, and then combine the strings
x = 10
y = '10'
print(str(x) + y)

# This example will convert the string '10' into an integer and add the two together
x = 10
y = '10'
print(x + int(y))

# Note that if we try type casting a value from one type to another, it may cause an error if the types can't convert
# of if the format is incorrect to convert.
# This example would cause an error because we're trying to convert a string representation of a float to an int
"""
print(int('10.6'))
"""

# But if we converted an actual float to an int, Python handles this by rounding the float down
print(int(10.6))


"""
Operators

There are several operators in Python, and some of them have multiple functions depending on what the operands are. For
example, adding strings will add the right string to the end of the left string, and adding lists will add the right
list's items to the end of the left list. There can be a lot of data type specific functionality, for more details on
these, you should refer to Python's online documentation.

	a + b	:	Add a and b
	a - b	:	Subtract b from a
	a * b	:	Multiply a and b
	a / b	:	Divide a by b
	a % b	:	Get the remainder of dividing a by b (called 'Modulo' or 'Mod')
	a ** b	:	Raise a to the power of b
	a // b	:	Divide a by b and round the result down
	
The following only applies to older versions of Python, such as 2.X! In Python 3.X, the highest precision is always
used, meaning that an int divided by an int could still result in a float.

	Note that when we use different numeric data types as the operands, we get different results. In the case of division
	(for example), if one of the operands is a float, the result will also be a float. But if both operands were ints, then
	the result would be an int as well. This could result in the following scenario:
		
		5 / 6		= 0
		5 / 6.0		= 0.833333[...]
		10 / 3		= 3
		10 / 3.0	= 3.333333[...]

There are also several assignment operators which perform some operation with the arguments and saves the result to one.
These are just shorthand for saying 'a = a <operand> b'.

	In all these examples, the resulting value is stored into a
	a = b	:	Assign the value of b to a
	a += b	:	Add a and b
	a -= b	:	Subtract b from a
	a *= b	:	Multiply a and b
	a /= b	:	Divide a by b
	a %= b	:	Get the remainder of dividing a by b (modulo)
	a //= b	:	Divide a by b and round the result down
	a **= b	:	Raise a to the power of b
	
	Bitwise operators (we may discuss this later)
	a |= b	:	Logically OR the bits of a and b
	a &= b	:	Logically AND the bits of a and b
	a ^= b	:	Logically XOR the bits of a and b
	a >>= b	:	Right shift the bits of a by b bits (copy the left-most bit to fill the space, rightmost bits fall off)
	a <<= b	:	Left shift the bits of a by b bits (fill in the space with 0s)
	
"""


"""
Lists

Lists in python are like ArrayLists in other languages. It's an ordered list of values which are stored in one variable.
We can access the different values in a list using their 'index', which is the location they are in the ordered list.
The first item in a list is actually at index 0, not 1. This is a confusing principle to most at first, and can often
lead to errors when trying to get items from a list such as trying to get the last item in the list but accidentally
requesting an item outside the list.

Lists, like variables, can hold values of all different types, and one list can even hold multiple different types at
once. Additionally, the size of a list (how many values are in it) can be increased or decreased using functions.

We can create a list using square brackets. We can also give it initial values in the list and separate the values with
commas, or leave it empty. In addition, we can get individual values from the list, modify them, add more values, or
remove values. There are different ways of doing each of these, and we may cover more complicated methods of interacting
with lists in the future.
"""

# Create a list of grocery items
groc_list = ['Waffles', 'Bananas', 'Milk', 'Cereal', 'Juice']
print(groc_list)

# Get a specific item from the list (remember, the first item is at index 0)
print(groc_list[2])

# We can also get items in the list from the end of the list instead of the beginning
# Note that, when accessing from the end of a list, the last item is actually at -1 not -0
print(groc_list[-2])

# Modify a specific item from the list
groc_list[2] = 'Cottage Cheese'
print(groc_list)

# Add an item to the end of the list
groc_list.append('Milk')
print(groc_list)

# Get the number of items (length) of the list
groc_size = len(groc_list)
print('The list has ' + str(groc_size) + ' items')

# Get and remove a specific item from the list using the index
got_item = groc_list.pop(3)
print('We removed ' + got_item + ' from the list ' + str(groc_list))

# We can also just remove an item from the list using the 'del' (delete) keyword without getting it as well
print(groc_list)
del groc_list[1]
print(groc_list)

# Check if a value is in the list
has_milk = 'Milk' in groc_list  # This expression evaluates to a bool type, and is often used in 'control logic'
print('Is Milk in the list? ' + str(has_milk))

# Check if a value is in the list, and if so, find the fist index it can be found at (because lists can have the same
# multiple times, this only gets the first instance found)
if has_milk:
	milk_index = groc_list.index('Milk')
	print('Milk is in the list at index ' + str(milk_index))
else:
	print('Milk is not in the list')

# Similar to finding the first instance of a value in a list, we can also remove the first instance of a value in a list
# Note that this doesn't return the value, unlike .pop
groc_list.remove('Milk')
print(groc_list)

# Insert a value into the list at the specified index.
# This shifts the value at that index and after to the right to make room for the new value
groc_list.insert(1, 'New Milk')
print(groc_list)

# Remove all items from the list
groc_list.clear()
print(groc_list)


"""
Tuples

A Tuple is very much like a list, with the exception that it can't be modified once created. A tuple in Python is
created using parenthesis instead of square brackets, and uses commas to separate values. Additionally, to create a
tuple with only 1 item, we need to include a comma after that item to tell python it should be a tuple instead of just
evaluating what's in the parenthesis as an expression.
"""

# Create a tuple
sample_tup = ('First item at index 0', 'Second item at index 1', 2, 3, 'Last item')
# Notice that it can also hold varying data types in it just like all other collections (lists and dicts) in Python

# If we tried to change the tuple or modify a value in it, we would get an error
"""
del sample_tup[0]  # Tries to remove an item, but we can't remove or add items to a tuple
sample_tup[0] = 0  # Tries to change the value of an item in a tuple, but we can't modify items in a tuple
"""


"""
Dictionaries

Dictionaries are similar to lists in that they hold multiple values within one variable and the values are comma
separated. However, there are several important differences. A dictionary stores its entries in key:value pairs, where
the key and value can be any datatype, though the keys are commonly strings. In Python 3.7+, dictionaries are ordered
but in versions before this they aren't (this is important when going through the keys or values in a for loop).

We can create a dictionary similarly to a list, either creating an empty one or giving it initial values. We use
curly brackets to do this, and if we want to give it initial values, each value needs a key with a colon separating the
key and value (commas separate entries). Getting the values of a dictionary is similar to getting the values of a list,
though the methods for modifying the dictionary are somewhat different.

A big part of dictionaries to keep in mind is that while they can have the same value in them as often as you like, they
can only have one instance of any given key in them. Since the primary way we get values from dictionaries is using
their keys, if we had the same key in a dictionary more than once, there would be no way to say which value we were
actually trying to get.
"""

# Create a dictionary containing a grocery list items as keys, and their prices as the associated values
groc_dict = {'Eggs': 5.50, 'Cereal': 4.75, 'Bacon': 7.00, 'Cheese': 3.80, 'Cleaning Spray': 6.30, 'Toilet Paper': 4.60}
print(groc_dict)

# Get an item from the dictionary
print('Cereal = ' + str(groc_dict['Cereal']))  # Notice how it only prints 5.5 instead of 5.50.
# We will discuss how to format values in a string later

# Modify an item in the dictionary
groc_dict['Cereal'] = 5.95
print('Cereal = ' + str(groc_dict['Cereal']))

# Adding an item is the exact same as modifying an item!
print(groc_dict)
groc_dict['Milk'] = 5.75
print(groc_dict)

# Get the length of the dictionary, this will get the number of items (key:value pairs)
print(len(groc_dict))

# Get and remove an item from the dictionary, very similar to a list, but we use the key instead of the index
got_item = groc_dict.pop('Bacon')
print('Bacon = ' + str(got_item))
print('We removed Bacon from the dictionary ' + str(groc_dict))

# Again, we can remove items without getting them using the 'del' keyword
print(groc_dict)
del groc_dict['Cleaning Spray']
print(groc_dict)

# Check if a key is in the dictionary
has_milk = 'Milk' in groc_dict
print('Does the dictionary have the key "Milk"? ' + str(has_milk))

# We can also check if a value is in the dictionary
has_cost = 4.60 in groc_dict.values()
print('Is the value 4.60 in the dictionary? ' + str(has_cost))
# We can go into the more practical use of this later...

# And also like lists, we can use .clear to remove all items from the dictionary
groc_dict.clear()
print(groc_dict)

"""
None

I want to briefly go over the 'None' type before moving on. None is the Python equivalent to saying 'Nothing',
'Unknown', or 'Not Set'. Other languages have their own versions of this, and it's typically used as a default value for
some variable that will be set later, and shouldn't have an initial value.

Keep in mind that None isn't used to check if we have created a variable or not yet. If we tried to check if a variable
we haven't created is equal to None, we would get an error that the variable hasn't been created yet instead.
"""

# Check if a value is equal to None
my_null_val = None
my_val = 42
print(my_null_val is None)
print(my_val is None)
# Note that we use the keyword 'is' here. We'll discuss it in detail later...
