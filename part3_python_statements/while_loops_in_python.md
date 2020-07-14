While loops will continue to execute a block of code while some condition remains true.

For example while my pool is not full, keep filling my pool


syntax

while some_boolean_condition:
    # do something

else:
    # do something else

--------------------------

examples

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1        or x += 1 the same

output
The current value of x is 0
The current value of x is 1
The current value of x is 2
The current value of x is 3
The current value of x is 4


while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1   

else:
    print('x is not less than 5')

    output
    The current value of x is 0
    The current value of x is 1
    The current value of x is 2
    The current value of x is 3
    The current value of x is 4
    x is not less than 5



----------------------------
BREAK, CONTINUE, PASS

break: breaks out of the current closest enclosing loop
continue: Goes to the top of the closest enclosing loop
pass: does nothing at all just a place holder

example of pass

x = [1,2,3]

for item in x:
      pass                                  if you leave this blank you will get an error      

print('end of my script')

output: end of my script

---------------------------
example of CONTINUE

mystring = 'sammy'

for letter in mystring:

    if letter == 'a':
        continue                goes to the top of the closes enclosing loop which happens to be  for letter in mystring

    print(letter)

output:
S
m
m
y


-----------------------

example of break

mystring = 'sammy'

for letter in mystring:

    if letter == 'a':
        break             this just breaks or stops this loop helpful with while

    print(letter)

output:
S



x = 0

while x < 5

    if x == 2:
          break
    print(x)
    x += 1


output
0
1
