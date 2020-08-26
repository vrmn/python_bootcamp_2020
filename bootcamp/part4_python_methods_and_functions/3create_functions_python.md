Creating a function requires a very specific syntax, including the def keyword, correct indentation and proper structure

overview of the python function structure


def name_of_function():                              - the def tells python that the following is a function
                                                     - in general python uses snake_casing_for_the_name of the function
                                                     - at the end where the praranthesis is (): you can pass in arguments / parameters into the function.  
                                                     - the colon : indicates an upcoming indented block.
                                                     - Everything indented is inside the function


def name_of_function():
    '''
    Docstring explaining function for reference later
    in this case this function is only printing hello
    '''
    print("hello")

then the call the function simply type

name_of_function()                 - and then whatever code is inside the function and runs it. In this case we'll just get hello
output: hello

-----------------------------------

functions can accept arguments to be passed by the user for example

def name_of_function(name):
      '''
      Docstring explaining function for reference later
      in this case this function is only printing hello
      '''
      print("hello " + name)

when calling it the user will input the arguemtn that will be passed

name_of_function(steven)
output: hello steven


------------------------------------------
Typically we use the (return) keyword to send back the result of the function, instead of just printing it out.

instead of just using print use return

(return) allows us to assign the output of the function to a new variable. for example

def add_function(num1, num2):
      return num1 + num2

result = add_function(1,2)
print(result)
output: 3
