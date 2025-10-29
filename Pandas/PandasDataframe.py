"""
data frame
----------

dataframe in pandas is a two-dimensional (table format) data structure which is used to work with
different types of data like booleans or string or numbers ...etc

"""

#dataframe examples

import pandas as pd

# person = {
#     "name": "Pavan",
#     "age": 22,
#     "job": "Engineer",
#     "country": "INDIA",
#     "city": "HYD",
#     "province": "HYD",
#     "countrycode": "IND",
#     "provincecode": "500081",
#     "citycode": "500081",
# }





person = {
    "names": ["PK","BPK","BPKY","AA"],
    "friends":["RV","RGV","JK","OTW"],
    "favtcolors":["red","blue","green","yellow"],
    "favtNumbers":[7,3,45,300]
}

data_frame = pd.DataFrame(person)
print("Before")
print(data_frame)
# when youare inserting the new column in the existing dataframe it has to match the element count
# otherwise ValueError: Length of values (5) does not match length of index (4)
# cities = ["HYD","VIG","WLG","BHPL"]
#
# #inserts the column at last
# data_frame["city"] = cities

# print("After")
# print(data_frame)

# insert the column at specify position
# data_frame.insert(1,"city_insert",cities)
# print(data_frame)

#inserting the multiple colmns

subs = {
    "maths":[10,20,30,40],
    "cs":[12,13,14,15],
    "stats":[11,22,33,44]
}




# inserting manually
# data_frame["maths"] = subs["maths"]
# data_frame["stats"] = subs["stats"]
# data_frame["Cs"] = subs["cs"]

#insertng using the for loop
# for sub in subs:
#     data_frame[sub] = subs[sub]
#
# print(data_frame)


#insert multiple columns at specified location
# data_frame.insert(2,"Maths_inserted",subs["maths"])
# data_frame.insert(3,"CS_inserted",subs["cs"])
# data_frame.insert(4,"Stats_inserted",subs["stats"])
# print(data_frame)

# count =2
# for sub in subs:
#     data_frame.insert(count,sub,subs[sub])
#     count += 1
#
# print(data_frame)