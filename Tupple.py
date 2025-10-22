"""
Tuples is an in-built ds
it must follow the order and it is immutable means once you create you can't modify the tuples

future
------
ordered
immutable
heterogeneous
indexing
iteration
used as Dictionary keys ( Cache )

"""

#creting the tuple
# nums = (1,2,3,4,5)
#
# print(type(nums))
# print(nums)
#
# nums_list = [1,2,3,1,23,14,31,32,53,1,2]
# tuple_cons = tuple(nums_list)
#
#
# print(tuple_cons)
# print(type(tuple_cons))

#empty tuple
# empty_tuple = ()
# print(empty_tuple)

#tuple with single value
# tuple_single_value = (1,)
# print(tuple_single_value)
# print(type(tuple_single_value))

# nums = (1,2,3,45,6,7,8,9,10)

# for num in nums:
#     print(num)

#slicing
# print(nums[-1])
# print(nums[2:5])
# print(nums[::-1])

# nums[0] = 10 # TypeError: 'tuple' object does not support item assignment
# print(nums)

# nums = (1,2,3,45,6,7,8,9,10)
# print("tuple before")
#
# print(nums,type(nums))
# nums_list = list(nums)
# nums_list.append(11)
# nums = tuple(nums_list)
#
# print("tuple after")
# print(nums, type(nums))

#membership operators
#len()
#min() max()
#count()

# print(min(nums), max(nums))


#unpacking
tuple_num = (100,101,102)

# x,y,z = tuple_num
# print(tuple_num)
#
# print(x,y,z)


nums = (1,2,3,45,2,6,7,8,9,1,10,2)

# print(nums)
# tuple_sorted = tuple(sorted(nums))
# print(tuple_sorted)

# print(len(nums))
# print(nums.count(2))


t = (1,2,3,4,5,6,7,8,9)
t1 = t[::-1]
print(t1)#output in the reverse format


