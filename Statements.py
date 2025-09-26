"""
Statements

to perform certain logics in program we need some help like when you want to use some algorithms in program
we can use the statements

statements are building blocks of the algorithms which used to perform some operations in program
1. Assignment statements
2. expression statements
3. print statements
4. input statements
5. conditional statements(if, elif, nestedif )
6. loop statements(for, while, nesting for loops)


when you write the statements and assign it to a variable
then first right side statement will be executed then at last it will assign the value to the variable
"""

# 1. Assignment statements
"""
when you try to assgin some values to any variable then we call it as a assignment statement
"""

x = 10
y = 20
z = x + y#Expression
print(z)


# 2. expression statements
z = x + y#Expression
print(x*y)

# 3. print statements
print(x/y)

"""
when you want to check the logic weather its working or not then we will use the logging in realtime development 
while learning and some times in real time development also we will use the print statement to debug the program

"""
# 4. input statements
# input function will help us to take the input from the user
# name = input("Enter your name : ")
# age = input("Enter your age : ")
# mobile = input("Enter your mobile : ")

# print(name, type(name))
# print(age, type(age))
# print(mobile, type(mobile))

# print(name, age, mobile)
amount = input("Enter your amount : ")#120.0 (String) collect the input from the user -> store it in the amount variable
amount = float(amount)#read the amount variable data -> convert it into float -> then store the float value to the same amount variable
# float will convert the value into decimal value 120(Float)
print(amount, type(amount) )

age = int(input("Enter your age : "))#input form the user -> covert it to the int type -> then assign to variable called age
print(age, type(age) )

is_having_fever= input("Is having fever? ")
is_having_fever= bool(is_having_fever)
print(is_having_fever, type(is_having_fever) )

#task for the tomorrow how the boolean input from the user works








