"""
String are collection of character of sequence of characters

in Python we can create the strings by using single, double, triple quotes

"""

# #Examples
# single_quotes = 'hey this string is created using single quotes'
# double_quotes = "hey this string is created using double quotes"
# triple_quotes = """
# hey this string is
# created using triple quotes
#
# extra lines we can add by using the triple qoutes
# """
# print(single_quotes)
# print(double_quotes)
# print(triple_quotes)

#accessing the string
# name = "ANUDIP FOUNDATION MADHAPUR HYDERABAD"
# print(name[0])#A
# print(name[5])#p
# print(name[-1])#D
# print(name[-2])#A
#
# #slicing of the string
# # slicing is used to extract a portion of string which you can specify the start index, end index, step value
# print(name[0:6])#ANUDIP
# print(name[7:17])#FOUNDATION
#
# print(name[::2])#each alternative charecters will be displayed

#if you want to find out total number of charecters in a string then we can use the len() method

# name = "ANUDIP FOUNDATION MADHAPUR HYDERABAD"# len() 36
# print(len(name)) #36


#iterating over the string
# name = "ANUDIP FOUNDATION MADHAPUR HYDERABAD"# len() 36
#
# for char in name:#this loop will run for 36 times
#     print(char)

#special charecters to work with strings(string operators ) (interview Imp One)
# name = "Anudip "
# location = "Madhapur "
#
# cen_location = name + location# + -> concatination
# print(cen_location)#Anudip Madhapur
#
# repeat_name = name * 3 # repetion operator
# print(repeat_name) # Anudip Andip Anudip
#
# name = "ANUDIP FOUNDATION MADHAPUR HYDERABAD"# len() 36
# center_name = "MADHAPUR"
# print(center_name in name) #True
# print ("Anudip " in name) #False
# print("HYDERABAD" in name) #True
# print ("Anudip " not in name) #True

#string Formating
#we can use % and .format(), f"" to format the string
#
# state  = "Telangana"
# name = "Anudip "
# location = "Madhapur "
#
# str_1 = "%s %s %s India"%(name,location,state)
# print(str_1)# Anudip  Madhapur  Telangana India
#
# str_2 = "{} {} {} India".format(name,location,state)
# print(str_2)# Anudip  Madhapur  Telangana India
#
# str_3 = f"{name} {location} {state} India"
# print(str_3)# Anudip  Madhapur  Telangana India

# take any string from the user and reverse it -- interview question
# print(u_input[::-2])

u_input = input("Enter a String : ")


# reversed_string = u_input[::-1]
# print("Reversed string is " , reversed_string )


# logic by using for loop
u_input = input("Enter a String : ")


# login by using while loop
u_input = input("Enter a String : ")


# check weather user inputed values is palindrome or not

# logic by using for loop
u_input = input("Enter a String : ")

# login by using while loop
u_input = input("Enter a String : ")














