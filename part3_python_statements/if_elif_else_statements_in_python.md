Control Flow

Allows us to use logic to execute code only when we want to .   This are if, elif, else

Control flow syntax makes use of colons and indentation (whitespace)

This indentation system is crucial for python and is whats sets it apart from other programming languages.


Syntax of an if statement

if some_condition:
    # execute some code


else:                         Notice that they are aligned and that else doesn't have a condition. Only runs when if condition is not true
    # do something else

---------------------------------

if you want to check for mulitple conidition you can add the elif

if some_condition:
    # execute some code

elif some_other_condition:      you can have as many elif that you want.
    # execute some code


else:
    # do something else


------------------------------
examples

if 3 > 2:
    print('Its true')



hungry = True        if false nothing the im not hungry prints

if hungry:
    print('FEED ME!')

else:
    print('I'm not hungry)


----------------------------

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool')


elif loc == 'Bank':
    print('money is cool')

else:
    print('I do not know much')
