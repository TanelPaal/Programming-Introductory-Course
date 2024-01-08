"""
Functions

A Function is a block of code that runs when it's called. Their use allows us to not copy-paste code over and over, and
to instead just create the function once, and call it whenever we need it. To create a function, we use the keyword
'def' followed by the name of the function we want to create, a set of parenthesis, and then a colon to indicate the
start of a block of code.

Scope
	Functions only know about variables that are
	either given to them when they are called, or that they create in their block of code. This principle of different
	parts of code not knowing about variables in other parts of code is called 'scope'.

	The basic Python script with no functions or classes or imports (we'll discuss classes and imports later) all occurs
	in the global scope. If we defined a function within our Python script, it's scope would be the inner scope. In
	Python, while functions CAN get variables from outer scopes (such as global), they will prefer to use their own
	inner scope. And if a variable is created within the scope of a function, that variable is lost when the scope
	changes to the outer scope, IE, the function ends.

	It's best practice to avoid using variables from the outer scope of a function whenever possible, and to instead
	pass those variables to the function when calling it.

Arguments
	In order to pass values to functions, the function needs to specify what it's expecting. These are called arguments.
	In Python, as with variables, we don't need to specify the data type of these arguments. This can lead to problems
	though when other developers are using our code and functions, so it's best practice to leave comments explaining
	both what the function does, what the arguments are, and what the function returns (we'll talk about this soon).

	When creating the function, the names of the arguments we want it to take go in the parenthesis separated by commas.
	In the function, we can then refer to these arguments just like we would any other variable in our code. However,
	there are some intricacies to keep in mind related to a principle called 'Pass By Reference' and 'Pass by Value'.

	Pass By Value
		This is when we pass an argument to a function by copying the value of the variable and giving that copy to the
		function to work with. This means that the function can modify that value all it wants, and it will never change
		the original variable. This is how all primitive date types are passed in Python and many other languages.

	Pass By Reference
		This is when we pass an argument to a function by giving it access to our original variable. This means, unlike
		pass by value, the function can modify the original when it modifies what it's been given. This is how any
		non-primitive data type is passed to functions, such as lists, dictionaries, and other complex data types.

	Pass by value and pass by reference are a complex topic, and it's understandable to confuse the two. when in doubt,
	perform a quick test to see if the value you're passing to the function will modify the original or not.

Return values
	As we learned, some functions are capable of modifying the original variables, but others might not be designed to.
	So how can we modify a primitive value and then send those changes back to the original caller of our function? We
	can do this using the 'return' keyword. Whenever we use this keyword, that immediately ends the function, sending
	the value we return back to the original caller.

	We can return anything that we want, including new variables we've created in the function. For example, we could
	create a function that generates a random number and return that randomly generated number to the caller! In
	Python, we can also return multiple values at once, though this is somewhat less commonly used. To do so, we simply
	separate the values or variables we want to return with commas on the return line. Additionally, we can have more
	than one point in the function where we use the return keyword, but keep in mind that whenever return is used, it
	will exit the function and return the value(s) given to the caller without finishing whatever might be left in the
	code block.
"""


# Create and call a function to print 'Hello World!'
def hello_world():
	print('Hello World!')


hello_world()


# Create and call a function to greet someone with the given name.
def say_hello(name):
	print('Hello ' + name + '!')


# We can use values or variables to pass arguments just the same
say_hello('Caleb')
person = 'Andrew'
say_hello(person)


# Create and call a function that greets multiple people
def say_hello(people):
	"""
	For this function, I've included a multi-line comment to explain what the function does.
	This is often called a 'doc-string' (documentation string).
	Also, notice how this is the same name as the previously defined example function of 'say_hello'.
	In Python, when we define a function with the same name as an existing function, it will replace the old function
	definition. Other languages would do something called 'overriding' the existing function, however we won't be
	discussing this concept or how it applies to Python. For now, just know that if you name a function something that
	already exists, the newest definition will be what's used.

	This function greets all the people given in the people argument.

	Parameters:
		people	list<str>

	Returns:
		None
	"""
	for person in people:
		print('Hello ' + person + '!')


say_hello(['Caleb', 'Andrew', 'Mason'])


# Create and call a function to tell if the first argument is divisible by the second
# This is a simple example, but it demonstrates how functions with multiple arguments are made and called
def is_divisible(x, y):
	"""
	Returns True if x is divisible by y, else returns False

	Parameters:
		x	int
		y	int

	Returns:
		bool
	"""
	return x % y == 0


print(is_divisible(10, 2))  # is_divisible is called with x=10 and y=2. Because 10 is divisible by 2, it gives us True
print(is_divisible(10, 4))  # now x=10 and y=4, and 10 isn't divisible by 4 so it gives us False


# Example of using global variables in a function
debug = True


def foo():
	global debug  # We use the keyword 'global' to say we want to reference these variables from the outer scope
	if debug:
		print('Foo')
	else:
		print('Bar')


foo()


"""
Named Arguments

When calling a function, the correct number of arguments must be given otherwise an error occurs. However, this isn't
always the case, as named arguments don't need to br provided to a function to call it. A named argument is an argument
that has a default value if it's not given.

To create a named argument in your function, put an equals sign after it, followed by its default value. Note that this
default value MUST be some static value, and can't be something that changes. While you *may be allowed to assign a
variable as a default value, the default value will just be whatever the variable happens to be at that time, not what
it might be later when the function is called. In general, avoid using variables as default values and instead just use
a value itself.

Named arguments also allow for the caller to pass them into the function call in whatever order they want to, allowing
the caller to ignore some of the named arguments while still passing others. However, unnamed arguments (also known as
positional arguments) must always be provided first and in their correct order.
"""


def say_hello(name='World'):
	print('Hello ' + name + '!')


say_hello()
say_hello('Caleb')
say_hello(name='Kaitlyn')


def print_triangle(width, fill_character='#'):
	for row in range(width):
		line = ''
		for col in range(row):
			line += fill_character
		print(line)


print_triangle(5)
print_triangle(5, '%')
print_triangle(10, fill_character='^')
