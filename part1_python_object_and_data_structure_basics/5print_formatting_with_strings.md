There are times you will want to "inject" a variable into your string for printing. For example

my_name = 'Steven'
print('Hello ' + my_name)

There are multiple ways to format string for printing variables in them.
This is known as string (INTERPOLATION)


one method is .format() method

the other is f-strings which stand for formatted string literals and is a newer method for some never version of python 3

example of .format() method

'String here {} then also {}'.format('something1', 'something2')

example

print('This is a string {}'.format('INSERTED'))
output: This is a string INSERTED

one advantage is that string can be inserted by index position

print('The {} {} {}'.format('fox, 'brown', 'quick'))
output: The fox brown quick

now include the index positions

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
output: The quick brown fox

you can also repeat
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
output: The fox fox fox

another way to insert is with variable assignments

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

______________________________

float formatting

result = 100/777
result
output: 0.1287001287001287

print("The result was {}".format(result))
output: The result was 0.1287001287001287

float formatting follows "{value:width.precision f}"

print('The result was {r:1.3f}'.format(r=result))
output: The result was 0.129


-------------------------------------------------

f strings  literals

name = 'Steven'

print(f'Hello, my name is {name}')
output: Hello, my name is Steven

age = 25

print(f'{name} is {age} years old.')
output: Steven is 25 years old.
