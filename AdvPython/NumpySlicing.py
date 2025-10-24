"""
multidimensional array

Slicing basic slicing

view() and copy()

"""
import numpy as np

# #2d array
# arr_2d = np.array([["Pl","PK"],["Pl","PK"]])
# print(arr_2d)
#
# #3d array
# arr_multi = np.array([[1,2,3],[1,2,3],[12,13,14]])
# print(arr_multi)
#
# #MultiDimensional array
# arr_multi = np.array([[1,2,3],[1,2,3],[12,13,14],[34,35,36]])
# print(arr_multi)


# arr_num = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr_num)#accessing every element
#
# print(arr_num[5:8])#accessing inbetween the range
#
# print(arr_num[::-1])#negitive indexing
#
# print(arr_num[::2])#step up value
#
# print(arr_num[::])#everything from start to end




# multi dimensional array slicing
# arr_multi = np.random.randint(low=5, high=15,size=(5,7))
# print(arr_multi)
""" 
sample output
-------------
[[ 8  6  9  8 11 12 12]
 [10 14  6 11 11 12 14]
 [ 9  8 10 13 12  5  6]
 [12 11  5  5 13 14 12]
 [ 9 14 12 14 10 12 12]]


"""

# arr_multi = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr_multi)
# # print(arr_multi[1:])#skips the first row and extracts all other rows
# # print(arr_multi[1,:])#extracts only the second row and skips the rest of the rows
# print(arr_multi[:,2])
#
#
#

#view() and copy()
#when you say view that means it will not create any copy instead it will create another reference in the memory
# to the same array location where as when you say copy() then it will creates the exact copy() of the original array

#the main difference between the both is when you use the view then automatically it will modify the original array where
# as when you use copy it will not effect the original array

# arr_num = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
# print(f"before  {arr_num}")
#
# arr_num_view = arr_num.view()
# print(f"before view {arr_num_view}")
#
# arr_num_view[0] = 11
#
# print(f"after {arr_num}")
# print(f"after view {arr_num_view}")


# arr_num = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
# print(f"before  {arr_num}")
#
# arr_num_copy = arr_num.copy()
# print(f"before copy {arr_num_copy}")
#
# arr_num_copy[0] = 11
#
# print(f"after {arr_num}")
# print(f"after copy {arr_num_copy}")

# #MultiDimensional array
# arr_multi = np.array([[1,2,3],[1,2,3],[12,13,14],[34,35,36]])
# print(arr_multi)
# print(arr_multi.shape)#this will tell the total rows and columns of the array
#
#
# #when you use the reshape then we need to count the total number of elements in the array then
# #accordingly we need to divide that into row and coulmns like for example if you have 24 elements in total
# # then you need to divide that like 6 x 4 or 2 X 12 or 4 x 6 or 7 x 4 ... etc then we can reshape that with the above
# # ways apart from this if you try to reshape that into anything else then we will get and reshape error
# arr_reshaped = arr_multi.reshape(2,6)
# print(arr_reshaped)


#native libraries
# -----------------

"""
when two programming languages want to communicate then it will use the native labraries


"""
