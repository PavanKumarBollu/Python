from Pandas.FileOperations import student_data

col_names = ['Std_Id','Std_Name','Age',"Grade","Sub","Std_Marks", "Std_City"]

file_name = "student_data.csv"

import pandas as pd

df = pd.read_csv(file_name,names=col_names,header=0)

#print the total number of records present in the file
print(f"records before cleaning the data {df.shape}")


# find out the duplicated rows
duplicated_rows = df.duplicated()
# print(duplicated_rows) # print true if the record has been duplicated in the data else false against each record of the data


# find out howmany duplicate rows are present in the data
print(f"Total duplicates found in the data is {duplicated_rows.sum()}")
print(df[duplicated_rows])# to get the duplicated records we can do this


#drop the duplicate row of the data
data_cleaned = df.drop_duplicates()
print(f"records after cleaning the data {data_cleaned.shape}")


#save the cleaned data to the file
data_cleaned.to_csv("student_data_cleaned.csv",index=False)






