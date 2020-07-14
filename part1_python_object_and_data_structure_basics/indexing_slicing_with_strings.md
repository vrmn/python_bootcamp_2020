example of indexing

mystring = "hello world"
output: 'hello world'

mystring[0]
output: 'h'

mystring[1]
output: 'e'

mystring[-2]
output: 'l'

examples of slicing

mystring = 'abcdefghijk'

mystring[2]
output: 'c'

mystring[2:]      from c all the way to the end
output: 'cdefghijk'

mystring[3]
output: 'd'

mystring[:3]
output: 'abc'

mystring[3:6]
output: 'def'

mystring[1:3]
output: 'bc'

mystring[::]      pretty much the same as just calling the string
output: 'abcdefghijk'     

mystring[::2] adding the step size skips two characters
output: 'adgj'

mystring[2:7:2]  start at index 2 go up to index 7 with a step size of 2
output: 'ceg'


Cool trick to reverse a string

mystring[::-1]
output: 'kjihgfedcba'
