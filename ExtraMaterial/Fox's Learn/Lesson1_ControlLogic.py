"""
Control Logic

All languages have different syntax for control logic, but most share a few of the same general structures. Some common
control logic structures are 'If - Else', 'For loops', 'While Loops', and 'Try Catch'. This is by no means an exhaustive
list of control structures, but they are common and the main subject of this lesson.

Before we discuss the structures, we need to understand what a 'block' of code is, and what that looks like in python. A
block is a set of instructions (lines of code) that execute one after the other. Whereas most other languages ignore
whitespace; In Python, a block of code requires all instructions to have the same indentation level (IE, the same number
of spaces or tabs) and doesn't use any other characters to indicate separate blocks of code. In Python, the more
indentation the code has, the 'lower' the block is. This means that for a control structure to contain a block of code,
the block of code it contains must be indented more than the control structure is.

	Conditions
		Some of these control structures require a condition. This condition can be any 1 line of code, so long as it
		evaluates, or can be cast, to a boolean. There are lost of 'implicit' type casting that can be done on data
		types to convert them to boolean, so if you're passing a non-boolean type as a condition, it's best to know
		exactly how that cast would function so you don't get unexpected behavior. For example, type casting the string
		"False" to a boolean would actually result in True.

		Conditions are typically created using a comparator of some kind. Python has the following comparators which are
		mathematical, but can also work on non-numeric data types. However, keep in mind that you should compare values
		of the same data type and that you should understand what the comparator is checking when working with
		non-numerical data types.

		a == b	-	True if a is equal to b. Note the use of double equals sign indicating the evaluation of a being
					equal to b instead of the assignment of b's value to a.
		a != b	-	True if a is not equal to b.
		a > b	-	True if a is greater than b.
		a < b	-	True if a is less than b.
		a >= b	-	True if a is greater than OR equal to b.
		a <= b	-	True if a is less than OR equal to b.
		a is b	-	True if a refers to the same object as b. This is a complicated operator, and its use is more
					technical than we'll get into for now.
		a in b	-	True if a is in the collection of b. This is another complicated operator, and also has different
					uses depending on the context. In this context, it's being used to check something, but we'll cover
					its other uses later. For this use, b should be some collection of values such as a list.

		Furthermore, we can combine conditions using logical operators which, unlike other languages, mirror their
		english counterparts to make the condition easier for humans to read.

		a or b	-	True as long as either a or b is True. Is also true if both a and b are true.
		a and b	-	True only if a and b are both True.
		not a	-	True if a is False.

if
An if block will execute the code within its block IF the condition it is given evaluates to the boolean value True. If
it evaluates to False, the code block is skipped.

else
In addition to an if block, there is an else block. The else block only executes if the associated if block above it
hasn't executed. As such, an else block can't exist without an if block directly above it in the same block of code.

elif
There's a unique control structure in Python which combines the else block and if block called an elif. It's short for
else if, and it takes a conditional just like an if block. The difference between elif and if, is that an elif requires
an if block above it just like else, and it will only check its given condition if the if block above it hasn't
executed. The reason for the naming, is to shadow the conventions of most other languages where they need to use else if
as the else will interact with the above if, and then if the above didn't run, then it will allow its own if condition
to check if it should run. Just think of elif as another branch of code to run for different conditions.
"""


# Example a basic if block
grade = 80  # Variable used in the condition
if grade > 49:  # The condition checks if grade is greater than 49
	print('Passing grade')  # This is the block of code it runs if the condition is True

# Example of if-else block
grade = 30
if grade >= 50:  # The condition checks if the grade is greater than or equal to 50
	print('Passing grade')
else:
	print('Failing grade')

# Example of if-elif-else block
grade = 80
if grade >= 90:
	print('A')
elif grade >= 80:
	print('B')
elif grade >= 70:
	print('C')
elif grade >= 60:
	print('D')
else:
	print('F')

# Keep in mind that if an if or elif block above an elif or else runs, it won't run, and any connected elif or else
# blocks below it also won't run. So the above example will skip the first block (80 >= 90 = False), run the second
# block (80 >= 80 = True), and then since it ran, the remaining blocks will be skipped.

# If we instead switched a few of these from elif to if, then we're separating it into multiple if-elif-else groups, and
# each one will evaluate separate from the other.
grade = 80
if grade >= 90:
	print('A')
elif grade >= 80:
	print('B')
if grade >= 70:  # Changed this one from elif to if, creating a new group of if-elif-else.
	print('C')
elif grade >= 60:
	print('D')
else:
	print('F')

# There's no limit to putting control logic on the top level, so we can nest control logic as well like so
grade = 100
if grade >= 90:
	# This is the start of the 'A' code block
	letter_grade = 'A'
	if grade == 100:
		letter_grade += '+'
	elif grade == 90:
		letter_grade += '-'
	# This is the end of the 'A' code block

elif grade >= 80:
	letter_grade = 'B'
	if grade == 89:
		letter_grade += '+'
	elif grade == 80:
		letter_grade += '-'

elif grade >= 70:
	letter_grade = 'C'
	if grade == 79:
		letter_grade += '+'
	elif grade == 70:
		letter_grade += '-'

elif grade >= 60:
	letter_grade = 'D'
	if grade == 69:
		letter_grade += '+'
	elif grade == 60:
		letter_grade += '-'

else:
	letter_grade = 'F'
print(letter_grade)


"""
Loops

It's often necessary for the same code block to run more than once, such as running the code for each item in a list, or
running over and over as long as a certain condition is met. There are two control structures in Python to accomplish
this. They are 'while loops' and 'for loops'. 

while
While loops are fairly simple in design and are structured similarly to the if control structure. They require a
condition and check that it's True before running their code block. The difference is that when the while block's code
ends, it goes back to teh start of the while loop and checks the condition again. If it's still True, the code block
runs again. This can repeat for as long as the condition is True, and if the condition never changed to False, it could
loop forever.

This means that before the loop starts, we need the variables required in the condition to already have values.

for
For loops are a bit more complicated syntax wise, being designed to run a pre-determined number of times. Most other
languages have two types of for loops, a standard for loop that increments a specific variable each time it runs, and a
for-each loop that sets a specific variable to the next item of a collection (like a list) each time it runs. Python
combined the two into a single for loop format, and this syntax is where the keyword 'in' comes back. In Python, to make
a for loop, you specify a variable name for the loop, and then specify the collection that variable will get its values
from. This is essentially just a for-each loop, meaning "for each item in this collection, do this code". 
"""

# While loop example
some_var = 0
while some_var < 10:
	some_var += 1  # You might've noticed this 'a += b' operator earlier as well. It's shorthand for 'a = a + b'
	print(some_var)

# For loop example
for index_var in range(0, 10):
	print(index_var)
# Note that the range function generates something similar to a list for us to iterate over in our for loop since our
# for loop requires some kind of collection to loop over. The range function call here is the same as if we typed in
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# We may discuss the range function in more detail later, but for now all you need to know is it creates something like
# a list from the first value and to (but not including) the second value.

# For loop iterating over the items of a list
groc_list = ['Milk', 'Eggs', 'Cereal', 'An entire cow somehow', '1 unit of fresh air in a can']
for item in groc_list:
	print(item)


"""
Complex For Loops

There are times where we might want to iterate over more than one list at once, and Python's syntax of for loops allows
for us to do just that. We can create multiple variables for our for loops as long as the collection we're iterating
over in the loop has enough values nested in it to do so! This is a complex topic, and it's called multi-dimensional
arrays (or in this case, a multi-dimensional list) meaning the array (list) is more than just 1 dimension of values.

We'll discuss multi-dimensional arrays in more detail later, for our examples, we only need to understand that it's a
list containing lists inside of it.

We have a few tools to make this easier in Python. One function, enumerate, allows us to iterate over the indices of the
given list and the values of it at the same time. The other function, zip, allows us to combine two lists of the same
size and iterate over the values of both! 
"""

# Enumerate example
sample_list = ['First item', 'Second item', 'Third item', 'Fourth item']
for index, value in enumerate(sample_list):
	print(str(index) + ': ' + value)

# Zip example
student_list_1 = ['Caleb', 'Andrew', 'Ethan', 'Joel']
student_list_2 = ['Bryan', 'John', 'Mary', 'Susan']
for student_1, student_2 in zip(student_list_1, student_list_2):
	print(student_1 + ' is partnered with ' + student_2)


"""
Complex Loop Control

There are often times where we can or need to stop a loop before the rest of the code block runs. Sometimes we want to
skip the current iteration of a loop, such as looking for specific values in a for loop. Other times we might want to
stop the loop entirely and get out of it early, or perhaps we were using a 'while True' loop that goes forever and need
a way to stop it.

If we want to skip the remaining code block in the current loop and go back to the top where it checks the condition, we
can use the keyword 'continue'. This will skip the remaining code in the block and go back up to the current loop's
condition check, where it will check the condition and proceed as normal.

If we want to halt the loop and get our of it immediately (don't go to the top and check again, just get out of the
loop), we can use the keyword 'break'.

Note that, as mentioned before, we can nest control structures, and that includes looping structures as well. And the
use of break or continue will only affect the loop which the code block is directly in, not the outer loop.
"""

# Example of breaking out of an infinite loop
list_of_inputs = [1, 0, 0, 0]
while True:
	if list_of_inputs.pop() == 1:
		break
	print('Still looping...')
print('Broke out of the loop!')

# Example of continuing within a loop
name_list = ['caleb', 'Andrew', 'Jackson', 'Michael', 'courtney', 'carl', 'Mitch']
for index, name in enumerate(name_list):
	if name.istitle():
		continue
	print('Modifying ' + name + ' to be titled.')
	name_list[index] = name.title()
print(name_list)
# Notice that I didn't just modify the name variable in the loop, as that wouldn't have affected the original list.
# The name variable is a copy of that value, so wouldn't have affected the name from the list.
# Instead, I used the index to access the original list object and changed the value I needed to.
# I used some other functions in here, and we'll discuss in more detail why I couldn't just use name to modify the list.


"""
Try Catch

It's not uncommon for a script to encounter an error when it's running. When this happens, the error is 'thrown' or
'raised' and this, if not handled, will cause the script to halt and display in the output what went wrong. These error
messages may look large and be difficult to read, however they include important information that can often lead you to
the exact source of the problem.

For example, an error will tell you what line the error was caused by and in what file(s). In addition, the error will
tell you what the specific error was, such as an OutOfBounds error (tried to get an item by index not in a list) or
a ValueError (the argument passed to the function was not formatted correctly for the function).

The fact that the script will tell us what the error is provides us with a lot of information on how to handle it, both
when debugging and when planning for handling errors. But how do we actually handle errors in scripts?

This is where the Try-Catch control structure comes into play. In Python, we mark the start of a try block with the
keyword 'try' (and a colon after it since we're creating a code block for it to run). The script will execute everything
in the try block as normal, until it gets an error. When an error gets raised, the script skips the remaining code in
the code block and jumps to the associated 'catch' which in Python we create using the keyword 'except'.

The creation of the except block is the same as for the try block, but we can also specify a specific type of error that
except block should handle as well as assign that error to a variable! This allows us to get information from the error
in our script if we want to, or to handle the specific error type in a specific way.

If we might encounter multiple error types in a try block's code, we can add as many except blocks as we want to, each
catching their own type (or no type) of error and handling them accordingly.

If the code block in the try doesn't raise an error, then the code in all the associated excepts are skipped. There are
also 2 other keywords we can use in our try-catch blocks with the keywords 'else' and 'finally'. The else code block
will run only if the try block ran without error, and the finally code block will always run after the try, catch, and
else have been given a chance to run, regardless of their outcomes.

Lastly, keep in mind that if an error is raised in the except block, it will be raised as well and the current try-catch
block won't handle it, so a new try-catch would be needed to handle it.
"""

# Try to type cast a string to an int, but the string isn't formatted correctly so it raises a 'ValueError'
input_string = '13.5'
try:
	parsed_value = int(input_string)  # String contains a float, not an int, ValueError raised
except ValueError:
	# We handled this error by assuming it's formatted as a float
	# We find the first index of a decimal and then slice the string on the right at that index
	# This should give us just a number without the decimal component, so essentially it rounds the float down
	decimal_index = input_string.index('.')
	parsed_value = int(input_string[:decimal_index])

print(parsed_value)

# Similar example as above, but this one handles what happens if the value isn't just a float by accident
input_string = '# 13.5'
try:
	parsed_value = int(input_string)
except ValueError:
	# Check if the value is a float instead
	try:
		float(input_string)  # Attempt to type cast the string to a float

	# The attempt to cast it to a float failed, so it's not formatted in a way we can handle easily
	except ValueError:
		print('Unable to parse "' + input_string + '"')
		parsed_value = None  # We assign parsed_value to None as a default value

	# The attempt to cast it to a float worked, so we can slice the string at the decimal to cast it to an int
	else:
		decimal_index = input_string.index('.')
		parsed_value = int(input_string[:decimal_index])

print(parsed_value)
