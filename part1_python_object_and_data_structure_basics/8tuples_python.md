Tuples are very similar to list, however they have one key difference - IMMUTABILITY

Once an element is inside a tuple, it can not be reassigned.

Tuples use parenthesis (1,2,3)


mytuple = (1,2,3)
mylist = [1,2,3]


just like a list a tuple could hold a mix of object types.

mytuple = ('one', 2)

just like a list you can also use slicing and indexing

t[0]
output: 'one'


---------------

There are two basic built in methods for tuples.INDEX METHOD AND COUNT METHOD

for exampole
t = ('a', 'a', 'b')

t.count('a')
output: 2

t.index('a')
output: 0    shows the first index the object appears in .
