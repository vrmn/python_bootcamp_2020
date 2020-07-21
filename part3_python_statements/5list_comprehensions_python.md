list comprehensions are a unique way of quickly creating a list with python

list comprehensions are a good alternative instead of using a for loop along with .append() to create a list

mystring = 'hello'
mylist = []

for letter in  mystring:
    mylist.append(letter)

mylist
output
['h','e','l','l','o']


the alternative method

mylist = [letter for letter in mystring]     this is a flattened out for loop

mylist
output
['h','e','l','l','o']

mylist = [x for x in rang(0,11)]

mylist
[0,1,2,3,4,5,6,7,8,9,10]

mylist = [x**2 for x in rang(0,11)]
mylist
[0,1,4,9,16,25,36,49,64,81,100]


mylist = [x**2 for x in rang(0,11) if x%2==0]
mylist
[0,4,16,36,64,100]

celcius = [0, 10, 20, 34.5]

fahrenheit =((9/5) * temp + 32) for temp in celcius]

fahrengheit will be the result

remember this is the same as

fahrengheit = []

for temp in celcius:
      fahrenheit.append(((9/5) * temp + 32))

adding if else possible but not recommended

results = [x if x%2==0 else 'odd' for x in range(0,11)]

results
[0, odd, 2,odd, 4, odd, ]

-------------------------------

NESTED LOOPS

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
          mylist.append(x*y)

mylist1[200,400,600,400,800,1200,600,1200,1800]      2*100
                                                     2*200
                                                     2*300
                                                     4*100
                                                     4*200
                                                     4*300
                                                     6*100
                                                     6*200
                                                     6*300
mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
