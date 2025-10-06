#Functions are used to write some blocks(some lines of code grouped together) of code and reuse them
# anywhere in the program any number of times


#Functions Syntax

"""
def function_name(Parameters):
    #Function body(lines of code)
    #return (optional)

def -> is a keyword to indicate to the interpreter saying that we are gonna create a function

function_name ->  name of the function which you want to create( Some meaning full names you should use)

paramters-> inputs to the function, parameters are also called as arguments

function body -> functionality of the function

return -> used to return some value back to the calling thing. -> optional if we don't want to return anything

"""


"""
types of functions
in python we have two types of functions 
    1. user defined 
    2. inbuilt functions

-> when a function is created by the programmer then that function we will call it as userdefined function 
-> when we use the already created function in python then those functions are inbuilt functions 
Example-> print() input() and() or() ..etc are inbuilt functions
add() get_salary_details() ...etc are used defined functions

"""

# def add():
#     print(10+20)
#     print(10+20)
#
# add()
# add()
# add()
# add()
# add()

#local variables and global variables
# local variables are available inside the block which we created that variables
# where are global variable is available to use anywhere in the program(note: after creation of the variable only)
#java script also uses the interpreter
# java , c , c++ languages uses compiler


# def add(a,b):
#     # print(a+b)
#     if(a<=0 and b<=0):
#         print("Nagitive Number")
#     else:
#         print("possitive number")
#     print(a,b)
#     print(a+b)
#
#
# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# add(num_1,num_2)
#
#
# num_3 = int(input("Enter the third number: "))
# num_4 = int(input("Enter the fourth number: "))
# add(num_3,num_4)


# def add(a,b):
#     sum = a + b
#     return sum
#
# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# result = add(num_1,num_2)
# print(result)
#
# if(result > 50):
#     print("more than 50")
#
# if(add(num_1,num_2)>50):
#     print("more than 50")


def check_Eligile(age):
    if age >= 18:
        return "Eligile"
    else:
        return "Not Eligile"

age = int(input("Enter Your age"))
res = check_Eligile(age)
print(res)

if(res == "Eligile"):
    print("Go and fill the application")
else:
    # print(f"come back at " + 18-age + "years later")
    print("Come back when you cross 18 years")



