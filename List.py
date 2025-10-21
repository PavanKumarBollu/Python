"""
List
----
list is a dataStructure in python which will be used to store the different types of elements (all different types of data types)

list stores the elements in the order means it will remembers the order in which to stored the elements

in-built DS --> All the features are inbuilt no need to write any code we just need to know how to use the list
ordered --> remebers the order in which we are stores the elements
mutable --> we can change the list of modify the list at any point of time in the program
dynamic in size --> size of the list (length) is not fixed we can store n number of elements inside the list
heterogeneous data --> all basic data types we can store inside the list like string, wholenumber, decimal numbers, True..etc
"""

#How to create the list

# nums = [1,2,3,4,5,6,7,8,9]
# print(nums)
#
# user = ["Ganesh", 23, 5.7, "120kg", True]#5
# print(user)



#how to modify the list
# user = ["Ganesh", 23, 5.7, "120kg", True]#5
# print(user)
# user[1] = 24
# print(user)
# user[3] = "121Kg"
# print(user)

#how to update the list
# user = ["Ganesh", 23, 5.7, "120kg", True]
# print(user)
# user.append("Anudip")#when ever we use the append() function it will add at the last
# print(user)

#accessing elements
# user = ["Ganesh", 23, 5.7, "120kg", True]
# print(user[0])
# print(user[1])
# print(user[2])
# print(user[3])
# print(user[4])

#slicing of the list
# user = ["Ganesh", 23, 5.7, "120kg", True]
# print(user)
# print(type(user))
# print(user[-len(user)])
# print(user[::])
# print(user[:3])
# print(user[::-1])

#Functions on list
# user = ["Ganesh", 23, 5.7, "120kg", True]
# #len()
# print(len(user))
#
# #append()
# user.append("Anudip")

# print(user)

# extend()
# user_2 = ["UG", 1234567890, "HYD"]

# user.append(user_2)
# print(user[6])

# user.extend(user_2)
# print(user)


# insert()will work by using the index value we can insert at any position by using the index
# print(user_2)
# user_2.insert(1, "MI")
#
# print(user_2)
# user_2.insert(len(user_2), 264)
# print(user_2)



# remove()
# user_2.remove("HYD")
# user_2.remove(2) # error will come as we don't have the 2 in our list
# print(user_2)


# pop()
# user_2.pop(1)
# print(user_2)
# print(user_2.pop())
# print(user_2)




# sort() will sorts the elements in the aschending order it modifies the orginal list
nums = [55,24,17,56,85,98,174,624,75,74,6,1,45,62,58,63,87]
# print(nums)
# nums.sort()
# print(nums)

# nums_copy = sorted(nums)
# print(nums)
# print(nums_copy)

# reverse()
# print(nums)
# nums.reverse()
# print(nums)


# traversing over a list
#
# for num in nums:
#     print(num, end=" ")
# print()
#
# for i in range(len(nums)):
#     print(nums[i], end=" ")



#comprehension of the list

# names = ["Pavan", "Genesh", "Sushmitha", "Rao", "Dheraj", "Naveen", "Kranthi", "Rishi", "Sri"]
#
# names_with_a = []

# for name in names:
#     if "a" in name:
#         names_with_a.append(name)
#     else:
#         continue
# print(names)
# print(names_with_a)


#
#
# names = ["Pavan Kumar", "Genash Kumar", "Sushmitha", "Rao", "Dheraj", "Naveen Kumar", "Kranthi", "Rishi", "Sri Kumar"]
# names_with_a = [name for name in names if "K" in name and "u" in name]
#
#
# print(names)
# print(names_with_a)


# nums = [10,25,14,35,68,45,124,15,47,1,21,3,4,6,78,9,46]
#
# for num in nums:
#     if num % 2 == 0:
#         print(num, end=",")# 10,14,68,124,4,6,78,46








