def say_hell():
      print('hello')

say_hello()
output hello

--------------------------------------

functions with argument inputs

def say_hello(name):
      print(f'Hello {name}')

say_hello('steven')
output: hello steven

you can also provide a default in case you dont get an argument

def say_hello(name='stranger':
      print(f'Hello {name}')

say_hello()
output: hello stranger

------------------
if you want to save the variable that the function outputs the use RETURN print doesnt save just displays.

return vs print

def add_num(num1,num2):
    return num1 + num2

result = add_num(10,30)

result
output: 40
