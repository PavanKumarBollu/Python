"""
Numpy is library which contains the set of logics to work with Numerical Operations
Numpy is stands for Numerical Python - it is used for doing the scientific computing ( calculations )

numpy is used to work with large data like arrays multidimensional arrays and matrics


ML( Machine Learning )
Data Science
Research Purpose
 in all the above cases the numpy used in real life

Features of Numpy: -
multidimensional arrays
BroadCasting
ElementWise Operations
Mathematical Operations
Random Number Generation
Open Source
provides the support of collaborating with other libraries



use the following to install the numpy library in your project

pip install numpy


other way of installing the libraries
go to file --> select setting --> select Python --> select interpreter --> the click + icon
--> then type the library name in the search box --> click install package --> then automatically library files will
be downloaded and we can use them

to check the numpy version do the following

create any python file then enter the following code

import numpy as np
print(np.__version__)

if you are able to see the numpy version in the console then numpy is successfully installed in your system


"""

# import numpy as np
# print(np.__version__)



#Data Types in Numpy
""" int64, int32, int16, int8 --> signed integer datatypes 

    when we want the type as whole number we will say the type as int only bassed on internal algorithm it will choose
    one type or else if we want to any specific type then we can also mention like int32, or int64 ..etc
    
"""
""" uint64, uint32, uint16, uint8 --> unsigned integer datatypes """
"""Boolean Data Types """
"""float64, float32, float16 --> floating point datatypes"""
"""String Data Types """
"""DateTime Data Types """
"""Object Type """


"""Creating arrays using numpy """
# import numpy as n
#
#
# nums = n.array([1,2,3,4,5], dtype=int)
# print(nums)



#creating the arrays using list
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# nums_arr = n.array(numbers, dtype=int)
# print(nums_arr, type(nums_arr))

# int64, int32, int16, int8 --> signed integer datatypes

# import numpy as np
#
# int_arr_64 = np.array([1,2,3,4,5], dtype=np.int64)
# print(int_arr_64, type(int_arr_64))
#
# int_arr_32 = np.array([1,2,3,4,5], dtype=np.int32)
# print(int_arr_32, type(int_arr_32))
#
# int_arr_16 = np.array([1,2,3,4,5], dtype=np.int16)
# print(int_arr_16, type(int_arr_16))
#
# int_arr_8 = np.array([1,2,3,4,5], dtype=np.int8)
# print(int_arr_8, type(int_arr_8))
#
# nums = np.array([1,2,3,4,5], dtype=int)
# print(nums, type(nums))




""" uint64, uint32, uint16, uint8 --> unsigned integer datatypes """

# import numpy as np
#
# arr_uint64 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=np.uint64)
# print(arr_uint64, type(arr_uint64))
#
# arr_uint32 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=np.uint32)
# print(arr_uint32, type(arr_uint32))
#
# arr_unit16 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=np.uint16)
# print(arr_unit16, type(arr_unit16))
#
# arr_uint8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=np.uint8)
# print(arr_uint8, type(arr_uint8))








"""Boolean Data Types """
# import numpy as np
#
# arr_bool = np.array([True, False], dtype=np.bool)
# print(arr_bool, type(arr_bool))


"""float64, float32, float16 --> floating point datatypes"""
# import numpy as np
# arr_decimal_64 = np.array([1.5,2.5,3.5,7.5], dtype=np.float64)
# print(arr_decimal_64, type(arr_decimal_64))
#
# arr_decimal_32 = np.array([1.5,2.5,3.5,7.5], dtype=np.float32)
# print(arr_decimal_32, type(arr_decimal_32))
#
# arr_decimal_16 = np.array([1.5,2.5,3.5,7.5], dtype=np.float16)
# print(arr_decimal_16, type(arr_decimal_16))
#






"""String Data Types """
# import  numpy as pavan
#
# arr_string = pavan.array(["PK","SRK","AA","1","True","#"],dtype=pavan.str_)
# print(arr_string,type(arr_string))



"""DateTime Data Types """
# import numpy as np
#
# arr_date = np.array(['2024-01-01','2025-02-28',1,45953],dtype=np.datetime64)
# print(arr_date, type(arr_date))


"""Object Type """
# import numpy as np
#
# arr_object = np.array(["Pavan", 1234, 5.9, 120, "Madhapur", "Python",'Java'],dtype = object)
# print(arr_object, type(arr_object))


# we can create the arrays from tuple of list

# nums = [1,2,3,5,6,89,234,56,12,345,2]
# nums_tuple = (1,2,3,5,6,89,234,56,12,345,2)
#
#
# nums_dict = {
#     1:"Pkg",
#     2:"Pkg",
#     3:"Pkg",
# }
#
#
# import numpy as n
# arr_list = n.array(nums)
# print(arr_list , type(arr_list))
#
# arr_tuple = n.array(nums_tuple)
# print(arr_tuple , type(arr_tuple))
#
# arr_dict = n.array(nums_dict)
# print(arr_dict , type(arr_dict))#prints the things in dict format only not in array format


#creating the arrays with 1 or 0 as default values

import numpy as np
#
# arr_ones = np.ones((1,15))
# print(arr_ones)
#
# arr_zeros = np.zeros((1,15))
# print(arr_zeros)
#
# # generate array from 1-20 (n+1)
# arr_rand = np.arange(1,21)
# print(arr_rand)
#
# #generate array from 20-40
# arr_generate = np.arange(20,41)
# print(arr_generate)


#generate random array between 0 - 1  --> 0 is included and 1 is excluded

# arr_random = np.random.rand(1,5)
# print(arr_random)
#
#

# generate random array

# arr_random_1 =np.random.randint(size=10,low=500,high=550)
# print(arr_random_1)
#
#
#
# arr_random_2 = np.random.randint(size=(5,2),low=100,high=101)
# print(arr_random_2)


#generate the 5 x 5 arrays with 23 as a default value

arr_rand_23 =np.random.randint(size=(5,5), high=24,low=23)
print(arr_rand_23)


