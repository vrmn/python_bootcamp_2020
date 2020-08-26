<!-- *args(arguments) and **kwargs(keyword arguments) -->

Eventually if you work with python functions long enough, youre going to want a way to accept an arbitrary
number of argumetns and keyword arguements, without having to pre define a bunch of parameters in your function calls.



def myfunc(a,b):

      # returns 5% of the sum of a and b

      return sum((a,b)) * 0.05

myfunc(40,60)


what if we want to use more number.

one way is by applying defaults to arguments like below.

def myfunc(a,b,c=0,d=0,e=0):

But a limit is reached after


Its better to use * args for this so you can put in an arbitrary number of arguements. python recognizes this and puts arguemtns in a tuple. s
def myfunc(*args):
    return sum(args) * 0.05


**kwargs builds a dictionary of key value pairs

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My Fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print(" I did not find any fruit here")

myfunc(fruit='apple', veggie='lettuce')

output: my fruit of chice is apple


def myfunc(*args, **kwargs):

    print("I would like {} {}". format(args[0],kwargs['food']))


myfunc(10,20,30, fruit='orange', food= 'eggs', animal = 'dog')
