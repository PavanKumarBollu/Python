"""
Student Data Set With Three Subject Marks
maths
computerScience
physics

then we need to figure out the following
find the passed student marks in each subject
find out the student who passed in all the subjects


"""

import numpy as np

computer_science = np.random.randint(low=0,high=100,size=10)
maths = np.random.randint(low=0,high=100,size=10)
physics = np.random.randint(low=0,high=100,size=10)

print(f"cs : {computer_science}")
print(f"maths : {maths}")
print(f"physics : {physics}")



cs_passed = computer_science >= 35
print(f"cs_passed {cs_passed}")


maths_passed = maths >= 35
print(f"maths_passed {maths_passed}")

physics_passed = physics >= 35
print(f"physics_passed {physics_passed}")


# find out the student who passed in all the subjects
all_passed = cs_passed & maths_passed & physics_passed
print(f"all_passed {all_passed}")


# find out weather all the students got passed or not
all_passed_all_subjects = cs_passed.all() and maths_passed.all() & physics_passed.all()
print(f"all_passed {all_passed_all_subjects}")

