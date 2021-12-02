from datetime import datetime
new_date = datetime.strptime("2021-08-03","%Y-%m-%d").strftime("%d-%m-%Y")
print(new_date)
