#Creating a list with some duplicate values in it

a_names = ["PK", "AA", "SMB", "VJK","VJT", "SRK", "SRK", "AA", "VJK","NTR"]
print(a_names)

#converting the list into a set to remove the duplicate elements

a_set = set(a_names)
print(a_set)

#adding some other elements to the set
a_set.add("JrNTR")
print(a_set)


#removing the elements form the set
a_set.remove("NTR")
print(a_set)


#checking of the set is set subset of the another set

a_set_name = {"AA", "SRK"}

print(a_set_name)
print(a_set_name.issubset(a_set))#True
print((a_set.issuperset(a_set_name)))#True
print(a_set.issubset(a_set_name))#False
print(a_set_name.issuperset(a_set))#False


