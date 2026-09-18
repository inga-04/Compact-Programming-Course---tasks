from math import pi

# task 1
if __name__ == '__main__':
    r = float(input("Input the radius of the circle: "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi* r ** 2))

# task 2
def declaration_and_output():
    # ask for input
    zahl = int(input("Input an integer number zahl: "))
    print(f"Variable zahl has the value of {zahl} and is of type {type(zahl)}")
    # check type of zahl. if it is not int, set variable to None
    if type(zahl) is not int:
        zahl = None
        print("Variable zahl is not of expected type.")

    kommerzahl = float(input("Input a float number kommerzahl: "))
    print(f"Variable kommerzahl has the value of {kommerzahl} and is of type {type(kommerzahl)}")
    # check type of kommerzahl. if it is not float, set variable to None
    if type(kommerzahl) is not float:
        kommerzahl = None
        print("Variable kommerzahl is not of expected type.")

    text = (input("Input a string value text: "))
    print(f"Variable text has the value of {text} and is of type {type(text)}")
    # check type of text. if it is not str, set variable to None
    if type(text) is not str:
        text = None
        print("Variable text is not of expected type.")

    wahrheitswert = bool(input("Input a boolean value wahrheitswert: "))
    print(f"Variable wahrheitswert has the value of {wahrheitswert} and is of type {type(wahrheitswert)}")
    # check type of wahrheitswert. if it is not bool, set variable to None
    if type(wahrheitswert) is not bool:
        wahrheitswert = None
        print("Variable wahrheitswert is not of expected type.")

declaration_and_output()

# task 3
def type_conversion():
    #1
    intNumber = int(input("Input an integer number: "))
    convertedFloat = float(intNumber)
    print(type(convertedFloat))
    #2
    floatNumber = float(input("Input a float number: "))
    convertedInt = int(floatNumber)
    print(type(convertedInt))
    #3
    convertedString = str(intNumber)
    print(type(convertedString))
    #4
    numberText = (input("Input a string containing a number: "))
    convertedIntText = int(numberText) # only works when input string is just a number and doesn't contain other characters
    print(type(convertedIntText))
    #5
    convertedBool = bool(intNumber)
    print(type(convertedBool))

type_conversion()

# task 4
def factorial_calculation(x):
    factorial = 1
    for i in range(1, x+1):
        factorial = factorial * i
    print(f"The factorial of {x} is {factorial}.")
factorial_calculation(5)