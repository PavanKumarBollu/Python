"""
pandas are open-source library which is used to manipulate the data and to work with structured based or label based data
we will use the pandas

pandas provides some data structures and operations for manipulating data
mostly padas are used to work with structured data

Note: pandas library is built on top of numpy library of the python

the main important features of pandas library
---------------------------------------------

series:
dataFrame:
input and output:
data cleaning:
grouping and aggregation:
data transformation:
index and select:
time series data:
.
.
.
.
etc



how to install the pandas library
----------------------------------

we have two to install the pandas library
    1. using terminal(cmd)
    2. ide UI

1. terminal
    pip install pandas
    note: before installing the pandas you should also install the pip without installing pip you can't install the pandas
2. using ide UI

go to file --> select setting --> select Python --> select interpreter --> the click + icon
--> then type the library name(pandas) in the search box --> click install package --> then automatically library files will
be downloaded and we can use them in the list of installed libraries


pandas vs numpy
---------------



"""
import pandas as pd

# import pandas as pd
# print(pd.__version__)



"""
pandas data structures
----------------------

pandas have two data structures for manipulating the data
    1. series
    2. dataframe
    
    
    
1. series
---------
series is 1d array and it is one of the core ds of the python
to make it more simple just thing like series is nothing but a single column in excel

each element in pandas series have been identified (associated) with index or label 
which will be auto generated or we can specify manually also 
these index or label values are used for accessing the elements of the series

series can contain the homogeneous and heterogeneous data
same data type --> homogeneous
different data type --> heterogeneous

Note: when you want to give the index manually you need to verify the length of the index sequence with the values sequence
other wise we will get error of ValueError: Length of values (3) does not match length of index (4)

"""


# example

# import pandas as pd
#
# marks = [50,76,56,45,34]
# series = pd.Series(marks)
# print(series)
#
# print(series[0])
#
#
#
# sub_names = ["maths", 'cs', 'stats',"telugu"]
# sub_marks = [50, 45,60,46]
#
# series = pd.Series( sub_marks, index=sub_names, name="sub")
#
# # series = pd.Series( sub_names, index=sub_marks, name="sub")
# print(series)
# print(series['maths'])
# # print(series[50])
#













