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

import numpy as np
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


"""Creating arrays using numpy """
import numpy as n


nums = n.array([1,2,3,4,5], dtype=int)
print(nums)



#creating the arrays using list
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nums_arr = n.array(numbers, dtype=int)
print(nums_arr, type(nums_arr))






