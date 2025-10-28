"""

histogram is a visual representation which is used for comparing the frequency of the data distribution
example: when use have student marks with you like 20 students and you want to understand the range of students by dividing them
in ranges like from 30- 40, 40 - 50 ...etc to do this we can take the help of histogram chart to visually represent

"""
import matplotlib.pyplot as plt

arr_ranges= [0,10,20,30,40,50,60,70,80,90,100]
std_marks = [50,55,60,65,70,75,80,85,90,95,100,50,55,60,65,70,75,80,40,45,50,35,30,20,15,5,0,80,90,30,40,50,55,60,65,70,75,80,60,70,45,65,50,65,47,80,50,23,24,
             56,60,75,50,55,60,65,70,75,80,60,30,32,42,52,62,72,50,55,60,65,70,75,80,82,92,53,66,65,60,56,58,64,25,64,65,67,69,70]


plt.hist(std_marks,bins=arr_ranges, edgecolor='black')
plt.xlabel('range')
plt.ylabel('frequency')
plt.title('Student categorization')
plt.show()