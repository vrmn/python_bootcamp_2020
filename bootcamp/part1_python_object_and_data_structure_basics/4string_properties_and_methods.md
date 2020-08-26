immutability of strings - cannot change

name = "Sam"

say you want to change the name to Pam so you do whats below

name[0] = 'P' not possible to change the S since the string is immutabel

The way to do this you'll have to create a new string.
This is done with concatenation that is kind of merging two string together.
Example below of string concatenation


last_letters = name[1:]
output: 'am'

'P' + last_letters
output: 'Pam'

another example

x = 'Hello world'
x + " it is beautiful outside!"
output = 'Hello world it is beautiful outside!'


example of multiple string concatenation in one time

letter = 'z'
letter * 10
output: 'zzzzzzzzzz'

Note you will get errors if you try to concatenation with a number

2 + 3
output: 5

'2' + '3'
output: '23'

-------------------------------------------------------------------------------------------------------------

Built in string methods
So objects in python usually have built in methods and these methods themselves are essentially functions that are inside the object


x = 'hello world'  note you must define x first

x.  will make a list appear

x.upper()    an example of the functions inside the object
output: 'HELLO WORLD'  note this will not affect the original string. if you want it to you need to reassign it.

x.lower()
output: 'hello world'

x.split()     this allows you to create a list out of a string
output: ['hello', 'world']

x = 'Hi this is a string'    note the way it creates a list is by splitting were there is white space
x.split()
output: ['Hi', 'this', 'is', 'a', 'string']

x.split('i')    you can also specify how you want to split
output: ['H', ' th', 's ', 's a str', 'ng']


----------------------------------------------------------------------

next were going to look into string formatting for printing
there are a lot of useful methods you can use to quickly print out other objects along your strings

so far we only now print('hello')
