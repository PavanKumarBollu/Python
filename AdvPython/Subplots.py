"""
subplots are like a photo frame where we can divide the frame into multiple subparts and add the picture accordingly
here the subplots also exactly same we can add any number of figures into the subplots() form 1toN


when you use the subplots it will create a grid on that grid we can do the partition
in general we will use the subplots() to do the multiple data set comparison of multiple charts comparison .. etc

"""
from matplotlib import pyplot as plt

# student data example
# sample dummy data
student_names = ['PK',"AMB","AA",'NTR','PBR', 'RC', 'Murty', 'VJK', 'MGS', 'BK','NA', 'Nani']
computer_science = [95,90,90,90,99,80,85,75,99,99,65,75]
stats = [60,65,80,70,55,60,35,36,75,54,56,58]



# create the subplot()

fig, ax = plt.subplots(1,2,figsize=(10,5)) # horizontal
# fig, ax = plt.subplots(2,1,figsize=(10,5)) #vertical

#when you are not mentioning any values for rows and columns in subplots() function then it will considers the default
# values which are 1 , 1

# cs subject comparison
ax[1].bar(student_names,computer_science,color=['grey','g','b'])



# stats subject comparison
ax[0].barh(student_names,stats,color=['blue','green', "purple"])


plt.show()

#python naming conversions
