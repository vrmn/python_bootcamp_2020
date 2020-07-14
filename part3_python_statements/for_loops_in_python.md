Many objects in python are iterable meaning we can iterate over every element in the objects

Such as every element in a list, or every character in a string.

you can iterate over every character in a string, iterate over every item in  a list, iterate over every key in a dictionary

We can use for loops to execute a block of code for every iteration

----------------------------------

Syntax of for loops

my_iterable = [1,2,3]

for item_name in my_iterable:
    print(item_name)

output:
1
2
3

-------------------------

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

output
1
2
3
4
5
6
7
8
9
10

for jelly in mylist:    it doesn't have to print whats in the list
    print('hello')

output
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello

-------------------------------------

for num in my list:

    # check for even
    if num % 2 == 0:
        print(num)

    else:
        print(f'Odd Number: {num}')

output
Odd Number:1
2
Odd Number: 3
4
ect. ..


-----------------------------

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)                 notice the identation in this line. This will print once the for loop is complete since it is not inline with for

output: 55


for num in mylist:
      list_sum = list_sum + num
      print(list_sum)

output:
1      0+1
3      1+2
6
10
15
21
28
36
45

---------------------------------

mystring = 'Hellow World'

for letter in mystring:       you can also put 'hello world ' directly  for letter in 'Hellow World'
    print(letter)

output

H
e
l
l
o

w
o
r
l
d


-------------------------------------------
mylist = [1,2,3,4,5,6,7,8,9,10]

for _ in mylist:
    print('cool')

output:
cool
cool
cool
cool
cool
cool
cool
cool
cool
cool
cool
------------------------------------

this can also be done with tuples

tup = (1,2,3)

for item in tup:
    print(item)

output:
1
2
3

tuple unpacking

mylist = [ (1,2) , (3,4) , (5,6) , (7,8)]

len(mylist)
output: 4

for item in mylist:
    print(item)

(1,2)
(3,4)
(5,6)
(7,8)

for (a,b) in mylist:             unpacking     can also be for a,b in mylist: with no paranthesis.
    print(a)
    print(b)


output:
1
2
3
4
5
6
7
8
9
10



-----------------------------

iterate in dictionary

d = {'k1':1 , 'k2':2, 'k3':3}

for item in d:     by default when you iterate in a dictionary you only iterate through the keys.
    print(item)

output:
k1
k2
k3

for item in d.item:     you need the .item method to get the values note we can also use tuple unpacking
    print(item)

output:

('k1', 1)
('k2', 2)
('k3', 3)    


for key,value in d.items:
    print(value)

output:
1
2
3


for value in d.value:
    print(value)


output
1
2
3
