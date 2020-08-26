List are ordered sqequendces that can hold a variety of object types.

The same way you can look into strings (slicing and indexing) you can look into list
as well as (concatenate) them together is that you can actually mutate or change a list

one thing that is different from strings is that you can

They use []  brackets and commas to separate objects in the list. [1,2,3,4,5]

List support indexing and slicing.

List can be nested and also have a variety of useful methods that can be called of them
----------------------------------------------------------------------

just like strings

my_list = ['string', 100, 23.2] flexible

len(my_list)  like strings number of elements in list
output: 3

my_list = ['one', 'two', 'three']

my_list[0]
ouput: 'one'

my_list[1:]
['two', 'three']


you can also concatenate list together

another_list = ['four', 'five']

my_list + another_list
output: ['one', 'two', 'three', 'four', 'five']

Again list unlike strings are mutable
Example

new_list = ['one', 'two', 'three', 'four', 'five' ]

new_list[0] = 'ONE ALL CAPS'

new_list
output: ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

------------------------------------------------------------------------

append and pop

new_list.   there is a lot of various methods that can be used with a list

new_list.append('six')   this methods allows you to add a new element to the end of the list

new_list
['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']



new_list.pop()  pops of the last item and returns it.
output: 'six'

new_list        now as you can see the last item was popped off
output: ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

for specific item to pop off just specify the index

new_list.pop(0)
'ONE ALL CAPS'

new_list
[ 'two', 'three', 'four', 'five']

---------------------------------------------------------

other common methods are sort and reverse

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()       NOTE THAT THIS DOES NOT RETURN ANYTHING IT JUST MODIFIES THE original new_list

new_list
['a', 'b', 'c', 'e', 'x']

if you wanted to assign it to a variable what will happen is you'll get no returns

my_sorted_list = new_list.sort()

type(my_sorted_list)    check the type
output: NoneType        the type for a None object.


to do this its best to do as follows

new_list.sort()
my_sorted_list = new_list

num_list.sort()

num_list
output: [1 3, 4, 8]

num_list.reverse()

num_list
output: [8, 4, 3, 1]
