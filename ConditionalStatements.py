#first commit test
"""
conditional statements are used to execute some lines of code based on some condition
conditions means rule or rules come criteria


syntax:

if condition :
    statements to execute when the condition is true
else :
    statements to execute when the condition is false


nested conditional statements

if condition :
    statements to execute when the condition is true
elif condition :
    statements to execute when the condition is false
else :
    statements to execute when the condition is true

by mixing the both single and multi conditional statements we can full fill any conditional requirements



"""
#when you write anything in python programming the thing we should keep in mind is indentation(Spaces)



#Check the eligibility for voting

# age = int(input("Enter your age: "))

# if age >= 18 and age <= 45:
#     print("You are young.")


# if age >= 18 and age <= 80:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


#guess the number length by checking the range of the number
"""
input from the user then accroding to the number i need say how many digits are there in that number
ex: 20 -> 2 digits , 12345 -> 5 digits 1234567 -> more that five numbers ... so on
"""

# number = int(input("Enter your number: "))

#ex : 12345

# if number >= 0 and number < 10:
#     print("1 Digit Number")
# elif number >= 10 and number <100:
#     print(" 2 Digit Number")
# elif number >= 100 and number < 1000:
#     print(" 3 Digit Number")
# elif number >= 1000 and number < 10000:
#     print(" 4 Digit Number")
# elif number >= 10000 and number < 100000:
#     print(" 5 Digit Number")
# else:
#     print(" more than 5 Digit Number")



#ternary operator
#syntax :
# statements  if true if condition else statements if false
# print("Even Number") if number % 2 == 0 else print("Odd Number")

# check the given alphabet is vowel or not ( a e i o u )
#
# alphabet = input("Enter alphabet: ")
# print(alphabet)
#
#
# if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
#     print(f"{alphabet} is a vowel")
# elif alphabet == "A" or alphabet == "E" or alphabet == "I" or alphabet == "O" or alphabet == "U":
#     print(f"{alphabet} is a vowel")
# else:
#     print(f"{alphabet} is not a vowel")




#lader conditional statements
#find out the day of the week(take the input from the user)
print("Enter any number between 1 and 7")
day = int(input("Enter day: "))
"""
1-> sunday
2-> monday
3-> tuesday
4-> wednesday
5-> thursday
6-> friday
7-> saturday
"""
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Enter Valid Number from 1 to 7")





















