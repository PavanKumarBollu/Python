"""
String methods --> python programing language provides us wide range of string methods
we have wide range of in-build methods support to work with the string to full fill all of our requirements

"""
#upper() lower()
# str1 = "anudip foundation"
#
# print(str1.upper()) #""" Return a copy of the string converted to uppercase. """
# print(str1.lower()) #""" Return a copy of the string converted to lowercase. """
# print(str1.capitalize())
# """ Return a capitalized version of the string.
#     More specifically, make the first character have upper case and the rest lower case.
# """

#strip() lstrip() rstrip()
# this function is gonna help us to remove the white spaces, tab , new line characters \n
# str_2 = "  Foundation  "
# str_3 = " \n Anudip     \n  "
#
# print(str_2)
# print(str_2.strip())
# print(str_3)
# print(str_3.strip())

# print(str_2.lstrip()) #Foundation followed by spaces # Return a copy of the string with trailing whitespace removed from left side of the string
# print(str_2.rstrip()) #Return a copy of the string with trailing whitespace removed from right side of the string.

# replace("old_character", "new_character")

# str_4 = "abcabcabcabcabcabcabcabc"
# print(str_4)
# print(str_4.replace("bc", "a"))#it will replace all the occurences of the mentioned character in the string

#join()
# combines all the elements into a single string
# names = ["anudip", "foundation", "madhapur"]
# print(" ".join(names))
# print("@".join(names))
# print("#".join(names))
# print("1".join(names))


#count(sub_string, startindex, end_index) this methods will help us to count the number of times the sub string is prasent

# str_5 = "Anudip foudation anudip Anudip foundation Anudip anudip"
# print(str_5.count("Anudip",0,))
# print(str_5.upper().count("ANUDIP",0,))#5

#find(sub_string, startindex, end_index)
#find function will help us to find the first occurrence of the given substring in the string

str_6 = "IndiaFoundationIndiaMadhapurTelanganaIndia"
#
# print(str_6.find("India",))
# print(str_6.find("India",1))
# print(str_6.find("India",19))

#isalpha() isdigit() ..etc
"""
isalpha() is going to check weather the string contains only characters are not
isdigit() is going to check weather the string contains only digits are not
even it is gonna consider the spaces also

"""

print(str_6.isalpha())#True
print(str_6.isdigit())#False

"""
==
the following will use some internal algorithm which python din't disclose to us lexicographic order
>=
<=
!=
>
<

"""

































