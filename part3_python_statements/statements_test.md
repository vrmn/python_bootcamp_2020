NOTE USE PYTHON IN TERMINAL TO CHECK

use for, .split(), and if to create a statement that will print out words that start with 's':

Hint string_propterties_and_methods.md

st = 'Print only the worlds that start with s in this sentence'

when we do st.split we get [ 'print', 'only' ect]. Note like a list a string can also be indexed


plan: separate the words into list then scan into each list to see if the index(0) == s

for letter_1 in st.split():
    if 's' == letter_1[0]    actually its if letter_1[0].lower == ' s'
    print(letter_1)

--------------------------------------------

use range() to print all the even number from 0 to 10

for x in range(0,11):            dont forget you can use iterations range(0,11,2)
    if  x%2 == 0
    print(x)

---------------------------------------------
use a list comprehension to create list of all number between1 and 50 that are divisible by 3

result_list = [x if x%3 == 0 for x in range(0,51)] actuall its [ x for x in range(1,5) if x%==0]


----------------------------------------------------------------

go through the sting below and if the length of a word is even print even.

st = 'print every world in this sentence that has an even number of letters'

for word in st.split()
    if len(word)%2 == 0
    print(word)
---------------------------------------------

write a program that print the integers from 1 to 100. but for multiples of 3 print 'fizz' instead of the number, and for multiples of five print 'buzz'
for numbers which are multiplls of both three and five print 'fizzbuzz'

for num in range(1,101):

    if num%3 != 0 and num%5 != 0:           theres a better order if you check both fist then 3 then 5
        print(num)

    elif num%3 == 0 and num%5 !=0:
        print(fizz)

    elif num%3 != 0 and num%5 == 0:
        print(buzz)

    else:

        if num%3 == 0 and num%5 == 0
              print(fizzbuzz)

-------------------------------------------
use list comprehensions to create a list of the first letters of every word in the string below:

st = 'create a list of the first letters of every word in this string'

for first_letter in st.split():               list comprehension [word[0] for word in st.split()]
    print(first_letter[0])
