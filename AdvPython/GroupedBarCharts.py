import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageChops import offset

std = ('PK', "AA", "SMB")
subs = {
    "maths":(18.35,18.43,14.98),
    "Cs":(38.79,48.83,47.50),
    "Stats":(189.95,195.82,210.19)
}

label = np.arange(len(std)) #taking the student names and arranging them in order

width = 0.35 #bars width
multi = 0 #used to specify the count of the bars


fig, ax = plt.subplots() #creates the subplot() grid to add the chart

for sub, subin in subs.items():
    offset = width * multi
    reacts = ax.bar(label + offset, subin,width, label=sub)
    ax.bar_label(reacts, padding=2)
    multi += 1



#formatting the charts
ax.set_ylabel("marks ")
ax.set_xlabel("students")
ax.set_xticks(label + width, std)
ax.legend(loc="upper left", ncol=3)
ax.set_ylim(0,250)


plt.show()