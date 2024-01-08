import typing
from random import randint

"""
Classes

Python (like many other programming languages) is Object Oriented and uses what's called Object Oriented Programming
(OOP). While OOP is a key principle in understanding the versatility in the use of classes, we'll save the detailed
discussion of OOP for later. Classes can be thought of as Objects, and everything in Python is an Object built off
another Object (except the very base "Object"). Classes may have properties (values associated with the class or with
that instance of the class) and functions, and while it's technically allowed to create a new class with no new
properties or functions, that wouldn't be of much use at all.
"""


# We can create a class with syntax very similar to creating a function
# In this example, we're creating a simple class called MyClass with a set property value
class MyClass:
	my_prop = 'MyClass property: my_prop'


# We can create an instance of our newly created class similarly to calling a function as well
my_class_instance = MyClass()
print(my_class_instance.my_prop)

# And we can modify the properties of our created class instance
my_class_instance.my_prop = 'Modified MyClass property: my_prop'
print(my_class_instance.my_prop)

"""
The __init__ Class Function

There are several functions which all Objects must have and since they're required, they have default implementations
when creating a new class. These functions are named with a double underscore before and after their name, such as
__init__ which is short for initialization. This function naming convention in python is known as a dunder function.

Even though these functions already have default definitions for our classes, we can re-define them to do whatever we
want. For example, we can define the __init__ function in our class to require certain parameters in order to create an
instance of the class.

Of note, is that these dunder functions are typically used by other functionality in python, and are rarely called
directly by the programmer, although they can be if needed. It's best to not mess around with the dunder functions which
you don't fully understand.

In the case of __init__, this is the function that's called when a new instance of the class is being created, and the
first argument is ALWAYS called self (you technically can rename it... but I'm not responsible for the confusion this
may cause), followed by any other arguments that you might want to be required to create the class instance.

I also need to touch on the use of this 'self' argument in both the __init__ function as well as its use in the rest of
the class. In the context of defining our class and its functions, 'self' will refer to that instance of the class. As
such, we can use self.prop_name to refer to this instance's properties or functions in order to get or modify the values
as well as call the class's functions.

The __init__ function is also where we typically create class variables, contrary to the first 'MyClass' example which
created one variable directly in the class without the use of the __init__ function.
"""


# Create a simple animal class
class Animal:
	def __init__(self, name, age, sound):
		self.name = name
		self.age = age
		self.sound = sound


# Create some instances of our animal and use some of their properties
animal_list = [
	Animal('Doggo', 14, 'Bork'),
	Animal('Birb', 4, 'Twt'),
	Animal('Snek', 7, 'SsSsSs')
]

for animal in animal_list:
	print(f'{animal.name} ({animal.age}) says "{animal.sound}"')

"""
The __str__ Class Function

The other dunder function we'll cover is the __str__ function which is responsible for representing the class as a
string. This process can also be thought of as 'serializing' the class, however that's  aconversation for another time.
Since the __str__ function is responsible for representing our class as a string, that means it's called whenever we
want to print the class out, or convert it to a string using the str() function for example. Typically, the default
__str__ function is not very useful to us, so if we think we'll be using it, we can implement it as we will below.
"""

# Let's first take a look at what the default __str__ function gives us for our Animal class
for animal in animal_list:
	print(animal)


# Now let's redefine our Animal class to include a __str__ function
class Animal:
	def __init__(self, name, age, sound):
		self.name = name
		self.age = age
		self.sound = sound

	# Note that for all class instance functions of our class, the first argument refers to this instance itself (self)
	def __str__(self):
		return f'{self.name} ({self.age}) says "{self.sound}"'


# Before we can check what that did, we'll need to re-create our animals because they're still using the old definition
animal_list = [
	Animal('Doggo', 14, 'Bork'),
	Animal('Birb', 4, 'Twt'),
	Animal('Snek', 7, 'SsSsSs')
]
# Now let's take another look at what we get when printing our Animal class
for animal in animal_list:
	print(animal)

"""
Creating Custom Class Functions

We aren't just limited to functions that are already defined for our classes. We can define our own functions to do
whatever we like, such as modify values of the class instance, interact with another given class instance or object,
return a value, etc. We do this just like we define any other function in our class, being sure to remember the first
argument for class instance functions refers to the class itself (self).

Keep in mind that if you don't use the self keyword when trying to modify class properties, you may end up modifying the
base class itself instead of the instance who's calling that function! And because python actually allows you to add
properties to a class from anywhere, it won't throw an error if you do this either!
"""


# Create a basic GameEntity class
class GameEntity:
	def __init__(self, name, x_pos=0, y_pos=0, x_vel=0, y_vel=0):
		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel
		# We can also set properties which aren't given in the parameters, sort of like default values for all instances
		self.is_alive = True

	def respawn(self, x, y):
		# De-spawn the entity
		self.is_alive = False
		# Move the entity
		self.x_pos = x
		self.y_pos = y
		# Zero the entity's velocity so they don't respawn and fly off to infinity haha
		self.x_vel = 0
		self.y_vel = 0
		# Re-spawn the entity
		self.is_alive = True

	# This '@staticmethod' is called a decorator. This one in particular tells python the first argument isn't actually
	# supposed to be referring to this instance of the class, so I cna leave out 'self' in the arguments.
	# We might talk more about this later.
	@staticmethod
	def step_axis(seconds, axis_position, axis_vel, axis_limits):
		lower_bound = min(axis_limits)
		upper_bound = max(axis_limits)
		axis_position += seconds * axis_vel
		if axis_position < lower_bound:
			return lower_bound
		if axis_position > upper_bound:
			return upper_bound
		return axis_position

	def step_position(self, seconds, x_limits, y_limits):
		"""
		Moves the entity based on the amount of time that has been given and its own stored velocity. IF the entity
		would travel beyond a given axis limit, it is instead set to the limit. (Note that this is a VERY simple bounds
		check and would only work for checking a single point moving around a box. Not a very good bounds check for
		anything more complicated)

		:param seconds: The amount of time to simulate movement for in seconds
		:param x_limits: The x-axis min and max values in any order
		:param y_limits: The y-axis min and max values in any order
		:param z_limits: The z-axis min and max values in any order
		"""
		self.x_pos = self.step_axis(seconds, self.x_pos, self.x_vel, x_limits)
		self.y_pos = self.step_axis(seconds, self.y_pos, self.y_vel, y_limits)

	def __str__(self):
		return f'{self.name} ({self.x_pos}, {self.y_pos})'


# Not let's use our new GameEntity some
entity_list = [
	GameEntity('Entity 0'),  # Creating an entity with the default values
	GameEntity('Entity 1', 5, 5)  # Creating an entity at 5,5 but with default velocity still
]

# Let's create a few random entities
for index in range(2, 10):
	entity_list.append(
		GameEntity(
			f'Entity {index}',
			randint(-50, 50),
			randint(-50, 50),
			randint(-5, 5),
			randint(-5, 5)
		)
	)

# Now let's create some bounds for them and do some simulation
x_bounds = (-100, 100)
y_bounds = (-100, 100)

for sim_step in range(0, 10):
	print('-' * 10)  # Separator between iterations
	for entity in entity_list:
		entity.step_position(1, x_bounds, y_bounds)
		print(entity)
