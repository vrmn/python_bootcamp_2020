rules for variable names

names cannot start with a number
there can be no spaces in the name use _ istead
cant use any of these symbols           : ''"" ,< >/?| \ ()! @#$%^& * ~ - +

best practice to have variable names in all caps
global variable names will usually be in all caps

avoid using words that have a special meaning n python like "list" and "str"

note python uses dynamic typing, which means you can reassign variables to different data types
This makes python very flexible in assigning data types, this is different than other languages that are "statically-typed"
Below is an example of what is meant

my_dogs = 2

my_dogs = ["sammy", "frankie"]

this is ok in python

an example of static typing such as c ++

int my_dog = 1;

later on you will not be able to assign another data type

my_dog = "Sammy"; //RESULTS IN ERROR because no longer an integer




PROS OF DYNAMIC TYPING

very easy to work with
faster development time

CONS OF DYNAMIC TYPING

may result in bugs for unexpected data types
you need to be aware of type() which tell you the variable type


a = 5
a = a + a

type(a) will be int

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

my_taxes will be 10.0
