"""
its a built in DS
it is a unique collection of elements unordered
set contains unique elements in the sense no duplicate values

unordered
unique elements
mutable
no duplicate values

"""

#creating the set

# nums = {1,2,3,4,5,6,7,8,9}
# print(nums, type(nums))
#
# names = set(['PK',"AA", "SMB"])
# print(names, type(names))

#empty set
# set_empty = set()
# print(set_empty)
#
# empty_set_1 = {}
# print(empty_set_1, type(empty_set_1))
#

# str = "Madhapur"
# char_set = set(str)
# print(char_set) #{'d', 'M', 'h', 'u', 'a', 'p', 'r'}
#



# function on set

# nums = {1,2,3,4,5,6,7,8,9}
# print(f"Set Before Adding {nums}")
# nums.add(10)
# print(f"Set After Adding {nums}")


#clearing the set
# nums = {1,2,3,4,5,6,7,8,9}
# print(nums)
# nums.clear()
# print(nums)

# nums = {1,2,3,4,5,6,7,8,9}
# print(nums)
# nums.remove(7)#it is taking the input as value not index since it is a unordered ds
# print(nums)
# nums.remove(10)#KeyError: 10


set_t = {"PK", "AA", "SMB", "VJK","VJT", "SRK"}
set_b = {"SRK", "AA", "VJK","NTR"}
print(set_t)
print(set_b)
#union for getting the unique ele from both sets no duplicates
# set_union = set_t.union(set_b)
# print(set_union)


#intersection is for the getting the common elements in the both sets
# set_intersection = set_t.intersection(set_b)
# print(set_intersection)

#difference for getting the elements form the first set but not present in the second set
# set_difference = set_t.difference(set_b)
# print(set_difference)
#

num_1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
num_2 = {12,13,15,16}
print(num_1)
print(num_2)
print(num_2.issubset(num_1))#True
print(num_1.issubset(num_2))#False
print(num_2.issuperset(num_1))#False
print(num_1.issuperset(num_2))#True











