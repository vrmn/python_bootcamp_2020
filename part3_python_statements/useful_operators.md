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
