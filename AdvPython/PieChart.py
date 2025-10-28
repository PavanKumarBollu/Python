

"""
pie chart is best suited when we were comparing the values below 7 because when the values are more then 7  the comparision
of the values will becomes difficult

"""

brands = ['allonsolly', "BMW", "Nike", "Apple"]
online_sales_count = [12450,85246,56457,99999]

import matplotlib.pyplot as plt

pie_colors = ['red','green','blue','purple']

plt.pie(online_sales_count,labels=brands, colors=pie_colors, autopct='%1.1f%%')
plt.title('Online sales count')
plt.legend(pie_colors, loc='best')
plt.show()