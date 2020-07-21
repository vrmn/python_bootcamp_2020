to begin we need to create a text file to work with.

to tap into it say we have a text file named

myfile = open('myfilename' or "path:)

Now there are several methods you can all such as.

myfile.read() which will return a giant string of everything that is in the text file .
              if you were to do this twice you wont get anything in return.
              that is because the cursor which reads the file is at the end.
              to reset you need to type

              myfile.seek(0)

now say that we want to make a list where is object is a line in the text.
To do so type

myfile.readlines()

this is more convenient now because you can loop through the list or even index the lines.


now we also need to close the file you read to do so type

myfile.close() if you dont do this you might get an error


-----------------------------------------------------

best practice of reading files so you dont have to worry about closing it.  to do this type whats below

with open('myfilename or path') as my_new_file:        my_new_file is just the variable name you chose
    contents = my_new_file.read()                     finally what the indention means is that anything in the indention is going to use the new file as the
                                                      variable of whatever is inside open()

contents                                               now we dont need to worry about closing the file and the contents can still be retrieved.
output: file contents in long string.


-----------------------------------------------------



  READING AND WRITING INTO A FILE

There are different types of modes.

mode = 'r' which reads only
mode = 'w' which is write only (will overwrite files or create new)
mode = 'a' is append only (will add on to files)
mode = 'r+' is reading and writing
mode = 'w+' is writing and reading (overwrites existing files or creates a new file)

-------------------------------------------------------------

read mode 'r' example. say we have a file (my_new_file.txt) that says

ONE ON FIRST
TWO ON SECOND
THREE ON THIRD

with open('my_new_file.txt' , mode = 'r') as f:
        print(f.read())

output: ONE ON FIRST
        TWO ON SECOND
        THREE ON THIRD

-------------------------------------------------------


append mode

with open('my_new_file.txt' , mode = 'a') as f:
        print(f.write(' \nFOUR ON FOURTH')      keep in mind the \n to make the new line.


output: ONE ON FIRST
        TWO ON SECOND
        THREE ON THIRD
        FOURTH ON FOURTH


------------------------

WRITE OR OVERWRTIE EXAMPLE

with open('new_file_created.txt', mode = 'w') as f:
        f.write('I created this file!!!')

now to read what you just wrote.

with open('new_file_created.txt', mode = 'r') as f
        print(f.read())


OUTPUT: I created this file!!!
