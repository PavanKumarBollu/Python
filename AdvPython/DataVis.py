
"""
Basically the data visualization is used for story telling which means explaning the numbers or other data in the form
of charts we call it as data visualization


in  we have several types of data visualization
    1. matplotlib
    2. seaborn
    3. Tableau
    4. power bi
    5. D3.js


    by using any of the above visualizations we can create different types of plots


in python we have some different types of libraries for creating the visualizations
    1. matplotlib
    2. seaborn
    3. Bokeh
    4. plotly
    5. ggplot
    .
    .
    .
    etc


"""










# import matplotlib.pyplot as plt
#
# arr_1 = [1,2,3,4,5,6,7,]
# arr_3 = [8,9,5,11,12,3,14]
#
#
# #create the line plot
#
# plt.plot(arr_1,arr_3)
# plt.title("line plot")
#
#
# #display the plot
# plt.show()

#create a barchart for the following data of the students
sub_names = ["Maths", "Cs", "Physics", "Stats","English"]
sub_marks = [55,65,75,50,90]

import matplotlib.pyplot as plt

# bars = plt.subplots()
# charts = bars.bar(sub_names, sub_marks)

charts= plt.bar(sub_names, sub_marks,c)

plt.bar_label(charts,label_type="edge",color = "black")


plt.title("Subject Wise Marks")
plt.xlabel("Subject Name")
plt.ylabel("Subject Marks")


plt.show()

