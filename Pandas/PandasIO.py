"""
how to read the data from a file (CSV) how to write it to a file(CSV)


CSV
---
comma separated values (CSV)
 the name it self say that the file will separtes the values by using the comma

how to read the csv file
------------------------
to read the CSV file in python we will take the help of the pandas library and there is a methad called read_csv().




"""
import pandas
#reading the data of a csv file

# import pandas as PK
#
# file = PK.read_csv("customer_data.csv") # alias import using
#
# # file = pandas.read_csv("customer_data.csv") # direct using of the pandas
#
# files_different_location = PK.read_csv("C:\\Users\\bpava\\Downloads\\salesdata.csv")
#
# # print(file.head())
# print(files_different_location.head())


"""
the complete syntax of the read_csv() method

read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    sep: str | None |
    delimiter: str | None |
    
    # Column and Index Locations and Names
    
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    
    usecols: UsecolsArgType = None,
    
    # General Parsing Configuration
    
    
    encoding: str | None = None, | utf-8
)

file_path = file location
seperator = comma (by using what symbol the values are separated in the file)

header = in the file which row contains the heading of the columns simply mention infer to make the program detect automattically

names = list of column names if you want to mention the manually the column names

useCols = total how many columns you want to read it from the file like you can mention the indexes or column names

encoding = to read the data safely with out letting other application touch in between we will mention the encoding = utf-8


.head() method is always contains the top five records of the file 
"""



# writing to a CSV file

# to write to a csv file we will use the to_csv() method


#example

# import pandas as pd
#
# students_info  ={
#     "names":['PK','AMB', 'SRK'],
#     "ages":[25,26,25]
# }
#
# data_frame = pd.DataFrame(students_info)
# print(data_frame)
#
#
# data_frame.to_csv("result.csv",index=False,mode="a")
# # data_frame.to_csv("C:\\Users\\bpava\\Downloads\\result.csv",index=False)
# #when you say index = false that means the index values will not store in the file this will save us some memory
#
