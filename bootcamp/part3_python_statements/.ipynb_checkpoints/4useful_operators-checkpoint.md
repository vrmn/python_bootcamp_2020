operator for list

a generator like range() is a special type of function that will generate information instead of saving it all to memory

for num in range(10):
    print(num)

output:
0
1
2
3
4
5
6
7
8
9

for num in range(3,10):
    print(num)

output:
3
4
5
6
7
8
9

for num in range(0,10,2):
    print(num)

utput:
0
2
4
6
8


list(range(0,11,2))


-------------------------

index_count = 0

for letter in 'abcde':
    print(' at index {} the letter is {}'.format(index_count, letter))
    index_count += 1

output:
at index 0 the letter is a
at index 0 the letter is b
at index 0 the letter is c
at index 0 the letter is d
at index 0 the letter is e



another way

index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

output
a
b
c
d
e


-+------------------------------

The enumerate functions takes any interable object and returns some sort of index counter and the object itself or the elements at that particular iteration

word = 'abcde'

for item in enumerate(word)
    print(item)

output
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')

for index,letter in enumerate(word)
    print(index)
    print(letter)
    print('\n')

output
0
a

1
b
ect...

-----------------------------------
The zip function

mylist = [1,2,3]
mylist2 = ['a','b', 'c']

for item in zip(mylist, mylist2):
    print(item)

output:
(1, 'a')
(2, 'b')
(3, 'c')

list(zip(mylist1,mylist2))
output

[(1, 'a'),(2, 'b'),(3, 'c')]


---------------------
check if an element is in a list (in)

'x' in [1, 2, 3]  False
'x' in ['x', 'y', z]   True
'a' in 'apple'   True

'mykey' in {'mykey':345}

d = {'mykey':345}
345 in d.values

-----------------------------------

min max

mylist = [10,20,30,40]

min(mylist)   10
max(mylist)   40
---------------


from random import shuffle            --> so this means from the random library import the function shuffle

mylist = [1,2,3,4,5,6,7]

shuffle(mylist)

mylist
output: [7,4,6,3,1,2,5]


from random import randint

randint(0,100)    a random integer between 0 to 100


-------------------


user input

result = input('Enter a number here: ')

Now python will ask you to enter a number

caveat python will accept the input as a string

in order to transform

float(result)
int(result)
