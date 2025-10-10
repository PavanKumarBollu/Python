# write a program to print the even number until the user specified number
# if user say 10 -> 2 4 6 8 10

# num = int(input("Enter the Max Number: "))
#
# count = 1
# while count <= num:
#     if(count % 2 == 0):
#         print(count)
#     count += 1

"""

num = 10 
count = 1
count <= num -> 1 <= 10 -> true
count % 2 == 0 -> 1 % 2 == 0 -> false 
count += 1 -> 1 + 1 = 2


count = 2
count <= num -> 2 <= 10 -> true
count % 2 == 0 -> 2 % 2 == 0 -> true 
print(count) -> 2
count += 1 -> 2 + 1 = 3


count = 3
count <= num -> 3 <= 10 -> true
count % 2 == 0 -> 3 % 2 == 0 -> false 
count += 1 -> 3 + 1 = 4


count = 4
count <= num -> 4 <= 10 -> true
count % 2 == 0 -> 4 % 2 == 0 -> true 
print(count) -> 4
count += 1 -> 4 + 1 = 5

.
.
.
.
.

count = 10
count <= num -> 10 <= 10 -> true
count % 2 == 0 -> 10 % 2 == 0 -> true 
print(count) -> 10
count += 1 -> 10 + 1 = 11

while count <= num
        11  <= 10 -> False

"""


# write a program to print the odd number until the user specified number
# if user say 10 -> 1 3 5 7 9


# num = int(input("Enter the Max Number: "))
#
# count = 1
# while count <= num:
#     if( count % 2 != 0):
#         print(count)
#     count += 1



# num = int(input("Enter the Max Number: "))
#
# count = 1
# while count <= num:
#     if( not count % 2 == 0):
#         print(count)
#     count += 1

# num = int(input("Enter the Max Number: "))
#
# count = 1
# while count <= num:
#     if( count % 2 == 0):
#         count += 1
#         continue
#     print(count)
#     count += 1
#

# continue is a keyword which is used skip the current iteration and move to next iteration

num = int(input("Enter any Number : "))#10
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print(sum)#55


