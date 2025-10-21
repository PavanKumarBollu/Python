"""
Dictinory it is a built-in DS

its a key key value pair that means each value will be stored in dict with the help of key
that key will be used to do all kind of operations on that value ( hash map In other programming lang)

features
--------
key-value pair
no order (unordered)
mutable
not fixed in the size(dynamic)
much flexible
looping will also works with dict
no duplicate key should present inside the dict

"""
#examples
# human = {
#     "name": "PK",
#     "age":55,
#     "height":5.9,
#     "weight":80,
# }

"""
real time use cases of dict
---------------------------

student data
product information
sales data (unique data)
configuration details (ide , application configuration, mobile configuration)
store the data with some undestandable labels then we can go with the dict

"""
#empty dict
# dict_empty = {}

# dict with some key-value
# human = {
#     "name": "PK",
#     "age":55,
#     "height":5.9,
#     "weight":80,
# }

#by using the dict() constructor we can create the dict

# dict_dict = dict()#empty dict
#
# dict_dict_values = dict(name="PK", age=55, height=5.9, weight=80)
# print(dict_dict)
# print(dict_dict_values)


#methods
#clear()
# human = {
#     "name": "PK",
#     "age":55,
#     "height":5.9,
#     "weight":80,
# }
# print(human)
# human.clear()#removes all key values pairs form the dict
# print(human)

#copy()
# human_copy = human.copy()#shallow copy(copies all the key-values pair to new dict)
# print(human)
# print(human_copy)
# print()
#
# human_copy.clear()
# print(human)
# print(human_copy)#empty dict

# #items
# print(human.items())
#
# #keys()
# print(human.keys())
# #values()
# print(human.values())

# human = {
#     "name": "PK",
#     "age":55,
#     "height":5.9,
#     "weight":80,
# }

#pop()
# print(human)
# human.pop("weight")
#
# print(human)
# human.pop("age")
# print(human)
# # human.pop("weight")#key error
# human.pop("weight",None)#remove weight from the dict if weight is not found then removes nothing( no error)
# print(human)


#get() which we can use to get the item value bypassing the key value
# print(human.get("name"))
# print(human.get("age"))
# print(human.get("height"))
# print(human.get("weight"))

#
human = {
    "name": "PK",
    "age":55,
    "height":5.9,
    "weight":80,
}

human["email"] = "abc@gmail.com"
# print(human)

human.update({"addrs":"madhapur HYD"})
# print(human)

human["age"] = 65
# print(human)

human.update({"addrs":"HYD"})#
# print(human)

#traversing through dict
# for key in human.keys():
    # print(human[key])#print values one by one by using key

# for key in human.keys():
    # print(key)#print all the key one by one

# for value in human.values():
    # print(value) #print values one by one using direct values not tapping the dict each time

#
# for key, value in human.items():
#     print(key, value)





