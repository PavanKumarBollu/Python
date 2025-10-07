"""
calculator
----------

addition
subtraction
multiplication
division

task
----
modules
floor division
exponentiation
keep the repeated lines in a function and call that function



"""

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2




while True:
    print("Please Enter 1 for addition ")
    print("Please Enter 2 for Subtraction ")
    print("Please Enter 3 for Multiplication ")
    print("Please Enter 4 for division ")
    print("Please Enter 5 for Quit")

    u_input = input("What would you like to do? ")

    if u_input == "1":
        print("Addition")
        print("--------")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        res = addition(num1, num2)
        print(res)
        print()

    elif u_input == "2":

        print("Subtraction")
        print("--------")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        res = subtraction(num1, num2)
        print(res)
        print()
    elif u_input == "3":

        print("Multiplication")
        print("--------")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        res = multiplication(num1, num2)
        print(res)
        print()
    elif u_input == "4":
        print("Division")
        print("--------")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        res = division(num1, num2)
        print(res)
        print()
    else:
        print("Quit")
        break
