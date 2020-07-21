strings are a sequence of characters, using the syntax of either single quotes or double quotes:

"hello"
'goodbye'
" I don't do that"

Because strings are ordered sequences mean one can index and slice to grab sub sections of the string.

Indexing notation uses [] notation after the string (or variable assigned to the string)

Indexing allows you to grab a SINGLE character from the string

Index actions uses [] square brackets and a number index to indicate positions of what you wish to grab. For example

Character:         h     e    l    l    o
Index :            0     1    2    3    4
Reverse Index:     0    -4   -3   -2   -1


Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.

The syntax looks like this [start:stop:step]

start is a numerical index for the slice start

stop is the index you will go up to (but not include)

step is the step size you take


'hello'

'this is also a sting'  the white spaces count as characters

how to print a string

print("hello my name is slim shady")
output: hello my name is slim shady

Escape sequences allow you to have special commands inside of your string
example

print('hello \n world')   \n treats world as a new line
hello
world

print('hello \t world')   \t tabs world
hello   word



To find the length of string

len('hello')
output(5)
