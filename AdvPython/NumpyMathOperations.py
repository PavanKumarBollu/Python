"""
Numpy mathematical operations

numpy will provides very effective and easy way to do the mathematical operations on large array or matrics

ex: like addition sutraction multiplication division .. etc operation on arrays

when you don't have the same number of elements in the arrays then you can't perform the mathematical operations


"""
import numpy as np

# import numpy as np
#
# num_1 = np.array([1,2,3,4])
# num_2 = np.array([4,5,6,7])

# #addition (two arrays should have the same number of elements)
#
# num_addition = num_1 + num_2
# print(num_addition)# [ 5  7  9 11]
#
# #multiplication
#
# num_multiplication = num_1 * num_2
# print(num_multiplication)# [ 4 10 18 28]

# #division
# num_division = num_1/num_2
# print(num_division) # [0.25   0.4    0.5  0.57142857]
#
# #subtraction
# num_subtraction = num_2 - num_1
# print(num_subtraction) # [3 3 3 3]


# square each element in the array

# num = np.array([1,2,3,4,5])
# num = num ** 2
# print(num)

# print([1,2,3,4] ** 2) # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

#
# num = np.array([1,2,3,4,7])
# num = num // 2
# print(num)



# element wise comparison(operations)
# num_1 = np.array([1,2,3])
# num_2 = np.array([1,2,3])
# num_3 = np.array([1,2,4])


# result = np.equal(num_1, num_2)
# print(result)#[ True  True  True]
# print(num_1 == num_2)#[ True  True  True]

# result = np.equal(num_1, num_2).all()
# print(result)#True
#
# result_1 = np.equal(num_1, num_3).all()
# print(result_1)#False
#
#
# result_3 = np.array_equal(num_1, num_3)
# print(result_3)#False
# result_4 = np.array_equal(num_1, num_2)
# print(result_4)#True

#
#
# num_1 = np.array([10,2,14])
# num_2 = np.array([1,3,5])
#
# num_greater = num_1 > num_2
# print(num_greater)
#
#
#
# for num in num_1:
#     print(num)
