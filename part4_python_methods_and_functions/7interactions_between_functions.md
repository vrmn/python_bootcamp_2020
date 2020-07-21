typically a python script or notebook contains several functions interacting with each other.

lets create a few functions to mimic the carnival guessing game "three cup monte"
----------------------

example = [1,2,3,4,5,6,7]

from random import shuffle

def shuffle_list(mylist):

        shuffle(mylist)

        return mylist

  result = shuffle_list(exampole)

  result Output
  [3,4,1,5,6,7,2]    


------------------

so does the game look like

mylist = [ '', 'o', '']  

def shuffle_list(mylist):
        shuffle(mylist)
        return mylist

def player_guess():

      guess = ''
                                                              ### we can add while so that we make sure its the right
      while guess not ['0', '1', '2']:                        ### so why are these strings? because input always returns a string
              guess = input('pick a number: 0, 1, or 2')

      return int(guess)


player_guess()
Output: pick a number: 0, 1, or 2  ____input____
outuut


def check_guess(mylist,guess):      here we pass in our shuffled list and our guess
      if mylist[guess] == '0':
            print('correct!')
      else:
            print('wrong guess')     here it doens't matter to return because this is the end.
            print(mylist)

--------------------------------

LETS PUT THIS ALL TOGETHER. FIRST WHAT ARE THE PRACTICAL STEPS

STEP ONE HAVE AN INITIAL list
mylist = ['', 'o', '']

STEP TWO SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

STEP THREE USER GUESS
guess = player_guess()

STEP FOUR CHECK GUESS
check_guess(mixedup_list , guess)
