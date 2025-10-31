"""
to create the pivot in the python we will take the help of pandas library in pandas library there is a method called
pivot_table(parameters) which will creates the pivot table for us

    data: DataFrame,--> we need to pass the data frame
    values=None, --> include the column names which we wanna do the aggregation default none
    index=None, --> what are the column names which you want to prefer as index names (here we can do the basic filtering)
    columns=None, --> for grouping the data what columns it should use
    aggfunc: AggFuncType = "mean", --> aggregative function name like sum min or mx .. etc default value is mean(avg)
    fill_value=None, --> to replace the na values what value it should replace with
    margins: bool = False, -->  total value column at last and bottom
    dropna: bool = True, --> don't include the if the values are NAN
    margins_name: Hashable = "All",--> name of the last column (total column)
    sort: bool = True,-->  if we want the result to be in the sorted format or not

"""
# example
import pandas as pk
from matplotlib.pyplot import title

data = pk.read_csv("sales-data.csv")
# print(data.head())
# print(data.shape)

pivot_table = pk.pivot_table(data,index=["Manager","Product"],values=['Quantity', 'Sales'],aggfunc="sum",margins=True,margins_name="Total")
# pivot_table = pk.pivot_table(data,index=["Manager","Product"],values=['Quantity', 'Sales'],aggfunc="min",margins=True,margins_name="Total")
# print(pivot_table)

# print(pk.pivot_table(data,index=["Product"],values=['Quantity', 'Sales']))# default aggfunc is mean(avg)
#
# print(pk.pivot_table(data,index=["Product"],values=['Quantity', 'Sales'],aggfunc="max",margins=True,margins_name="Total"))
# print(pk.pivot_table(data,index=["Product"],values=['Quantity', 'Sales'],aggfunc="min",margins=True,margins_name="Total"))
# print(pk.pivot_table(data,index=["Product"],values=['Quantity', 'Sales'],aggfunc="count",margins=True,margins_name="Total"))



import matplotlib.pyplot as plt


plot = pivot_table['Sales'].plot.pie(
    labels=pivot_table['Sales'],
    autopct="%1.1f%%",
    y="Sales",
    figsize=(5,5),
    legend=True,
    title="Sales vs Products",
)
# print(pivot_table)
plot = pivot_table.plot.bar(x="Quantity",y="Sales",)
plt.show()

