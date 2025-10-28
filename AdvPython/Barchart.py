# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.ma.core import outer
#
# sub_name = ('maths', 'Cs', "physics","stats")
# sems= {
#     'sem_1' : np.array([60,65,55,80]),
#     'sem_2' : np.array([75,65,70,90])
# }
#
# fig, ax = plt.subplots()
# bottom = np.zeros(4)
#
# for sub, sub_count in sems.items():
#     # p = ax.bar(sub_name, sub_count, label=sub, bottom=bottom, color= 'lightgreen',edgecolor= 'black' )
#     p = ax.bar(sub_name, sub_count, label=sub, bottom=bottom, color= ['lightblue','pink',"lightgreen"],edgecolor= 'black',)
#     bottom += sub_count
#
#     ax.bar_label(p,label_type="center")
# ax.set_title("Subject wise marks of 2 semisters")
# ax.set_xlabel("Marks")
# ax.set_ylabel("Subject Names")
#
# plt.show()
#
#
#


#BarChart
#
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.ma.core import outer
#
# sub_name = ('maths', 'Cs', "physics","stats")
# sems= {
#     'sem_1' : np.array([60,65,55,80]),
#     'sem_2' : np.array([75,65,70,90])
# }
#
# fig, ax = plt.subplots()
# bottom = np.zeros(4)
#
# for sub, sub_count in sems.items():
#     # p = ax.bar(sub_name, sub_count, label=sub, bottom=bottom, color= 'lightgreen',edgecolor= 'black' )
#     p = ax.barh(sub_name, sub_count, label=sub, color= ['lightblue','pink',"lightgreen"],edgecolor= 'black',)
#     bottom += sub_count
#
#     ax.bar_label(p,label_type="center", color='red')
# ax.set_title("Subject wise marks of 2 semisters")
# ax.set_xlabel("Marks")
# ax.set_ylabel("Subject Names")
#
# plt.show()




import matplotlib.pyplot as plt



sub_name = ('maths', 'Cs', "physics","stats")
sub_marks = [50,65,54,80]

chart = plt.bar(sub_name,sub_marks)

plt.show()



