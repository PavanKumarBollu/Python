"""
string is a datatype in python which is used to store the sequence of characters or collection of characters
it built in data type -- it store all types of values or textual data

to store something inside a string we need to use either single or double quotes ('' ,"")





"""

#Examples
# string_single = 'here is the single quote string'
# string_double = "here is the double quote string"
# multi_line_string = """
# this is a multi line string
# used to store the multiple lines of string
# """
# print(string_single)
# print(string_double)
# print(multi_line_string)


#accesing the string
"""
in python we can access the individual characters form a string 
"""

# movie = "Iron Man"
#
# #accessing the first character
# first_char = movie[0]
# print(first_char)
#
# #accessing the sixth character
# first_char1 = movie[5]
# print(first_char1)
#
# #negative indexing
#
# last_char = movie[-1]
# print(last_char)
#
# last_second_char = movie[-2]
# print(last_second_char)

#slicing -> slicing allows us to extract the portion of the string , we can specify start and end index, step up value


# i_name = "ANUDIP FOUNDATION MADHAPUR"
#
# #SLICING TO GET ONLY ANUDIP FORM i_name
# first_name = i_name[0:7]#ANUDIP
# print(first_name)
#
# #SLICING TO GET ONLY FOUNDATION  FORM i_name
# mid_name = i_name[7:17]
# print(mid_name)
#
# step_up = i_name[::2]
#
# print(step_up)#AUI ONAINMDAU


#string length to find the total number of characters present inside the string we can use len() function
# i_name = "ANUDIP FOUNDATION MADHAPUR"#26

# total_char = len(i_name)
# print(total_char)


#iterating over a string

# for char in i_name:
#     print(char)# each character will be printed in a single line
# if you have total 10 characters in string then the for loop is going to run for 10 time and each time you will have the
# single(current character) in char variable


# i = 0
# while i < len(i_name):
#     print (i_name[i])
#     i +=1


#special characters
"""
python provies some special string operations and functions that we can use to perform various actions(operations) on strings
+ concatenation 
* mutliplication(repetition)
% format operator
.format()
in and not in (membership operator)
comparision operators
==
!=
<
<=
>
>=


"""
#examples
# str_1 = "Python "
# str_2 = "Programming "
#
# programming_lang = str_1 +  str_2
# print(programming_lang) #Python Programming
#
# programming_lang = str_2 +  str_1
#
# print(programming_lang) #Python Programming

#repeatation operator
# str_3 = "-Python-"
# str_4 = str_3 * 3
# print(str_4) # -Python--Python--Python-

# name = "Anudip"
# place = " Hyderabad"
# str_name = '%s Foundation Madhapur%s Telangana India' %(name,place)
# print(str_name) #'AnudipFoundation Madhapur Hyderabad Telangana India'

# name = "Anudip "
# place = "Madhapur "
# str_address = "{} Foundation {} Hyderabad Telanagana".format(name, place)
# print(str_address) # Anudip Foundation Madhapur Hyderabad

# name = "Anudip"
# place = "Madhapur"
#
# str = f"{name} Foundation {place} Hyderabad"
#
# print(str) #Anudip Foundation Madhapur Hyderabad

# Membership operators
# i_name = "Anudip Foundation Madhapur Hyderabad Telangana India"
# word = "Anudip"
# print(word in i_name)#True
# print(word not in i_name)#False
# print("Foundation Madhapur" in i_name)#True
# print("Hyd" in i_name)#True


#lexicographically
# str_1 = "Pavan"
# str_2 =  "Kumar"
# res_1 = str_1 == str_2 #False
# res_2 = str_1 >= str_2 #True
# res_3 = str_1 <= str_2
# res_4 = str_1 != str_2
# res_5 = str_1 > str_2
# res_6 = str_1 < str_2
# print(res_1)
# print(res_2)
# print(res_3)
# print(res_4)
# print(res_5)
# print(res_6)

#write a program to take the input from the user then revers the that string

#take the input from the user
# u_string = input("Enter a name : ")
#
# #defnie an empty string to store the string in reverse order
# u_reverse_string = ""
#
#
# for char in u_string:
#     u_reverse_string = char + u_reverse_string
# """ Bala
# 1st -> b + "" --> b
# 2nd -> a + "b" --> ab
# 3rd -> l + "ab" --> lab
# 4th -> a + "lab" --> alab
# output --> alab
#
#
#  """
#
# print(u_reverse_string)



# take any string from the user and reverse it

# u_input = input("Enter Anythig here : ")
# result = u_input[::-1]#inbackgroud there will be a loop to reverse the string on be half of the programmer
# print(result)




u_input = input("Enter Anythig here : ")

reversed_string = ""  #empty variable to store the results

len = len(u_input)

#sai jyothi --> input
print(u_input[9]) # i
print(u_input[8]) # h

while len > 0:
    reversed_string = reversed_string + u_input[len-1]
    print(reversed_string)
    len -= 1
# print(reversed_string)


#
# u_string = input("Enter a name : ") #input from the user
#
# len = len(u_string)# getting the number of charecters present in the user given string
# # if user enter sai jyothi -> then in len variable we will have 10
#
#
# while len > 0:
#     reverse += u_string[len-1]
#     len -= 1
# print(reverse)

"""
the above loop is going to run for 10 times from 10 - 0 when the len value becomes 0 then the loops is going to terminate

1st iteration
len = 10 -> 10 > 0 -> true
reverse = reverse + u_string[len-1]
"" = "" + u_string[10-1]
"" = "" + "i" 
len -= 1 --> len = 9

2nd iteration
len = 9 -> 9 > 0 -> true
reverse = reverse + u_string[len-1]
"i" = "i" + u_string[9-1]
"i" = "i" + "h"
 len -= 1 --> len = 8
 .
 .
 .
 .
 .
 .
 .
 10th iteration
len = 0 -> 1 > 0 -> true
reverse = reverse + u_string[len-1]
"ihtoyj ia" = "ihtoyj ia" + u_string[1-1]
"ihtoyj ia" = "ihtoyj ia" + "s"
 len -= 1 --> len = 0
 reverse = "ihtoyj ias"

 11 th iteration 
 len = 0 -> 0 > 0 -> false 
 come out of the loop



"""














