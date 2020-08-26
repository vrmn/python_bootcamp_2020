# LESSER OF TWO EVENS: Write a function that returns the less of two given numbers. If both numbers are even,but returns the greater if one or both numbers are odd.
# a = input("enter first number:" )
# print("")
# print(a)
# b = input("enter second number:")
# print("")
# print(b)
# print("")

def lesser_of_two_evens(a,b):
    a = input("enter first number:" )
    b = input("enter second number:")

    if a%2 == 0 and b%2 == 0:
        # BOTH NUMBERS ARE EVEN
        if a < b:
            result = a
        else:
            result = b
    else:
        # ONE OR BOTH NUMBERS ARE ODD
        if a > b:
            result = a
        else:
            result = b
    return result

print("test")
print("result = {}".format(result))
