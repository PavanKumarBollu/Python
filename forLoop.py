"""
for loop is a control statement in python that we will use to execute some logic repeatedly
for specific number of times like 10 20 30 5 .... etc

some list with employee names -- > some number of records will be there but it's not infinite number there we can use for loop

basically for loop in python is used to iterate over sequence like list type Strings ... etc


syntax:
for variable in sequence:
    #code to be executed in each iteration

"""

#examples
# for i in range(1, 11):#if you want to execute n time mention n+1 in max range
#     print("Pavan")#Pavan will be printed for 10 times on console

#nested for loop
"""
syntax of nested for loop 
-------------------------
for outer_var in outer_sequence:
    #outer loop code
    for inner_var in inner_sequence:
        #inner loop code
    #reamaining outer code to be executed 
    
"""

for i in range(1, 5):
    for j in range(1, 5):
        print("*" ,end = " ")
    print()


# for i in range(1, 7):
#     for j in range(1, i):
#         print("*",end = " ")
#     print()


#write a program to display the stars in pyramid style

# num = int(input("enter the max number : "))



# for i in range(1, num + 1):
#     print(" " * (num-i), end = " " )
#     print("* " * i)


# what is the difference between the for and while loop
#     1. both looops are used to execute some code repeatedly
#     2. if we want to go through over a sequence then --> for loop
#     2. if we want to execute as long as the condition is true --> while loop
# how to exit from the loop
#     by using the break keyword we can come out of the loop
# how to skip the current iteration
#      by using the continue keyword we can skip the current iteration

