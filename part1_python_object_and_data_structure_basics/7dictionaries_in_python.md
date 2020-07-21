Dictionaries are unordered mappings for storing objects.

Recall that Strings store objects in an ordered sequence.

Dictionaries store objects using a key-value pairing instead.

The advantage of key-value pairing is that it allows the user to quickly grab objects without needing to know a n index location.


Dictionaries use curly braces and colons to signify the keys and their associated values. for example

{ 'key1':'value1' , 'key2':'value2' }

---------------------------------------

so when to choose a list and when to chose a dictionary? pretty much when you dont what to deal with indexing.

The con to this is that a dictionary is unordered therefore is can not be sorted.
Because a dictionary uses key value mapping its going to insert new key value pairs wherever it deems most efficient.

Remember with list on the other hand you can retrive objects based off locations so that allows the list to
be indexed sliced and then sorted.
--------------------------------------
How to construct a dictionary

my_dict = {'key1':'value1' , 'key2':'value2' }

my_dict['key1']
output: value1

price_lookup = {'apple':2.99 , 'oranges':1.99}
price_lookup['orange']
output: 1.99

----------------------------------

dictionaries are actually super flexible in the data types they can hold
They can actually hold list as well as other dictionaries

d = {'k1':123 , 'k2':[0,1,2] , 'k3':{'insideKey':100} }

d['k2']
output: [0, 1, 2]

d['k2'][2]   you can also stack the indexcalls/keycalls to get back the values sought
output: 2

d['k3']
output: {'insideKey': 100}

d['k3']['insideKey']     you can also stack the indexcalls/keycalls to get back the values sought
output: 100

-------------------------

special functions

d.keys() shows all the keys in the dictionary

d.values() shows all the values in the dictionary

d.items() shows all the pairings in a the dictionary
