"""
Files and JSON

Files are how programs can remember things from past iterations, or communicate with other programs asynchronously.
JSON, is typically used to do the latter, communicate some data or information between programs asynchronously. It's a
way to format data into a string so that any program can read it in and convert it to various Objects.

Opening and Closing Files
	In Python, the first step to manipulating a file (be it reading or writing) is to open it. This can be done in
	multiple ways, though whatever method you use to open a file, you must remember to close it when you're done. Files
	that are "open" in a program can't be "open" in another program.

	If, for example, a file is open in a long running script and that script doesn't "close" it when it's done reading,
	other programs won't be able to read or write to that file until that other script either closes the file or exits.

	Additionally, when opening a file in python, you must specify the mode you wish to open it in (read, write, append,
	or a combination). Once opened in one of these modes, it can't be opened by the program or any others until it's
	closed. If opened in a write mode, the changes won't be applied to the file until it's closed.
"""

from json import loads, dumps
from random import randint

"""
The first way we'll cover reading from a file in Python is using the 'open' function and assigning the resulting file
Object to a variable just like any other function call.

As actually reading the data, we'll use the simple 'read' function for now, which returns us ALL the content of the file
in one string.
"""

r"""

*****

----- WARNING!!!!! -----

Change this filename to point to some file you wish to open. While it doesn't have to be a text file, if it's not
it might not print correctly if at all. It should point to a file you don't care about, as we'll read from and write to
the file over the course of this example script! To prevent anyone from running this without reading this line, I've
added a variable below filename which needs to be set to True in order for the script to run.

*****

Note the use of an "r" string where an r is before the actual string. This creates a "raw" string where the backslash
"\" escape characters get ignored instead of interpreted as special characters like "\n" would be a newline normally.
This makes creating windows filepath strings much easier since we don't need to double up on the escape characters
"""''
filename = r'C:\Testing\test_file.txt'
i_have_read_the_warning = False  # This is to prevent you from running this without reading it first.
if not i_have_read_the_warning:
	raise Exception('''----- WARNING!!!!! -----

Change the variable "filename" to point to some file you wish to open. While it doesn't have to be a text file, if it's
not it might not print correctly if at all. It should point to a file you don't care about, as we'll read from and write
to the file over the course of this example script! To prevent anyone from running this without reading this line, I've
added a variable below "filename" which needs to be set to True in order for the script to run.''')
# The filename if we didn't us an 'r' string
# filename = 'C:\\Testing\\test_file.txt'

"""
open the file to a variable
Specify the mode with the second argument
r = read
w = write
a = append
More modes can be found in the python documentation or commonly on W3schools for python
"""
data_file = open(filename, 'r')

# Read the data from the file into a single string and save that string to a variable
data_string = data_file.read()

# REMEMBER TO CLOSE THE FILE!
data_file.close()

# We read the string data into a variable so we still have it even though the file is closed.
print(data_string)

"""
There are other ways to open a file, such as using the 'with' keyword.

This will create a code block where, inside the block, the file is opened as the variable name specified. Once the block
ends, the opened file is closed and the variable drops out of scope (we covered scope in the Functions section). This is
generally a safer way to open a file, as it ensures that you can't forget to close a file when you're done with it.
"""

with open(filename, 'r') as data_file:
	data_string = data_file.read()

# Now that the 'with' code block ended, the opened file is closed
# But we've already read the data into the data_string variable so we still have that to work with
print(data_string)

"""
There's other functions to read data from an opened file besides just 'read'. These have their own use cases, and I
woudl encourage you to experiment with some of these to get an understanding of them yourself as well. We'll cover the
readlines function which returns a list of all the lines in the file.
"""

with open(filename, 'r') as data_file:
	data_list = data_file.readlines()

print(type(data_list))
print(data_list)

"""
When it comes to writing to a file, there are 2 modes we mentioned, 'write' and 'append'. In write mode, whatever you
write to the file will REPLACE EVERYTHING in the opened file once closed. However, in append mode, all changes are
applied to the end of the file instead of replacing existing data.

Keep in mind though, that no changes will go through until the file is closed!

We can write data to a file by using functions similar to the read functions from before. Keep in mind though, that it
won't add any newline characters in for you
"""

with open(filename, 'a') as data_file:
	# Let's create a small string to add on the end of this file
	sample_string = 'Hello World! This is new data added to the file!'
	data_file.write(sample_string)

# Now let's re-open the file for reading and see what we have
with open(filename, 'r') as data_file:
	# Let's skip the step where we read to a variable andjus tprint it out instead
	print(data_file.read())


"""
Now that we've covered some basic file I/O (input / Output), let's discuss how we cna manipulate some JSON data. Python
has a library specifically for working with JSON, the json library. In it, there are 2 functions we'll focus on. These
functions are loads and dumps, short for load string and dump string. These functions load JSON data from a string into
a variable (in the form of a dict or list), and convert json data (from a dict or list) to a string respectively.

What we'll do here, is create a JSON string manually, though you would never do this normally, and load it into a
variable. Then, we'll create some JSON data programmatically and output that to a file. You can view the JSON data that
we output to a file using an online JSON viewer such as https://codebeautify.org/jsonviewer.

When working with JSON, keep in mind it's just dicts and lists which we covered back in one of our ealier classes. Refer
to those notes for working with JSON data once it's read into a variable.
"""

# Manually create a JSON string as if we read it from some source like a file
json_string = '{"grade": "100%", "lastname": "Raczka", "firstname": "Robert", "year": 9, "dob": "06/02"}'

# Load the JSON data into a variable
json_data = loads(json_string)

# let's take a look at what it gave us
print(type(json_data))
print(json_data)

# Now just to complete the understanding, let's take a look at what we get when we call 'dumps' on our data
# It should match what we originally had in the string
print(dumps(json_data))

# Alright, now we'll programmatically create some JSON data and output that to our sample file.
json_data = []
for index in range(0, 30):
	item = {
		'id': index,
		'itemName': f'Item {index+1}',
		'itemValue': randint(0, 30)
	}
	json_data.append(item)

# Now let's convert this json data (a list of dictionaries) into a string and output it into our sample file
json_string = dumps(json_data)
with open(filename, 'w') as json_file:
	json_file.write(json_string)

print(f'Open {filename} at https://codebeautify.org/jsonviewer to easily view the generated JSON we created.')
