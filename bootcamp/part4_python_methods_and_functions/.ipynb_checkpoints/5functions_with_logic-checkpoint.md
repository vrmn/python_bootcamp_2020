def even_check(number):
    result = number % 2 == 0
    return result

even_check(20)
Output: True

def even_check(number):
    return number % 2 == 0    - the above can be written like this as well.

    ----------------------------


This function will return true if any number is even inside a list

def check_even_list(num_list):

      for number in num list:

              if number % 2 == 0:
                    return True
              else:
                    pass


check_even_list([1,3,5])
Output will be nothing since there is no even numbers

check_even_list([1,2,5])
Output 2

------------------------------

say you want to have check_even_list() return false instead of nothing
What not to do

def check_even_list(num_list):

      for number in num list:

              if number % 2 == 0:
                    return True
              else:
                    return False   #### dont do this because it will just run once

INSTEAD DO


def check_even_list(num_list):

      for number in num list:

              if number % 2 == 0:
                    return True
              else:
                    pass

      return False       ###### the return false should be aligned with the for
                        ##### this gives the for loop permission to cycle through the list instead of just cycling once



---------------------
return only the even numbers in a list.

def check_even_list(num_list):


    # place holder variables for what you intend to return
    even_numbers = []             #### start of with an empty list

    for number in num list:

            if number % 2 == 0:
                  even_numbers.append(number)
            else:
                  pass

    return even_numbers

      
