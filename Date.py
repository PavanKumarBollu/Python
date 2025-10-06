from datetime import datetime

date = input("Enter Date (YYYY-MM-DD): ")
date = datetime.strptime(date, "%Y-%m-%d")
print(date)
