# load the student data file with custom heading

col_names = ['Std_Id','Std_Name','Age',"Grade","Sub","Std_Marks", "Std_City"]


import pandas as p

student_data = p.read_csv("student_data.csv",names=col_names,header=0)
# print(student_data)


# file_information = student_data.info()
# print(file_information)
# infor function is used to know the basic information of the file like total records total columns ...etc

#describe()
# displys the basic information of the numarical columns present in the file like count min max ..etc

# file_describe = student_data.describe()
# print(file_describe)


# to check unique occurence of the values we can use the values_count()

# sub_count =  student_data['Sub'].value_counts()
# print(sub_count)
#
#
# for sub in sub_count:
#     if sub > 20:
#         print(sub)
#

# dropna() is used to remove the null values or NAN values form the sheet

# print(student_data.info())
#
# student_data.dropna(inplace=True)
# print(student_data.info())

# duplicated() fucntion is used for removing the duplicates for the file and use the unique records

# print(student_data.info())

# duplicate_rows = student_data.duplicated(keep="first",subset=None)
#
# print(f"Total Duplicate Records removed is {duplicate_rows.sum()}")
# print(duplicate_rows) # print on each row like weather the value is duplicated or not
