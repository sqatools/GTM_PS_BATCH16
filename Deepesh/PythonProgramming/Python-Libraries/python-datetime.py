from datetime import datetime, timedelta

curr_date_time = datetime.now()
print(curr_date_time) # 2026-04-06 08:44:22.318772
print("today day:", curr_date_time.day) # today day: 6
print("current month:", curr_date_time.month) #  4
print("current Year", curr_date_time.year) # 2026
print("minutes :", curr_date_time.minute) # 46
print("today date :", curr_date_time.date()) # 2026-04-06


unique_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
print("unique_name:", unique_name)

#5 days back date.
result = curr_date_time - timedelta(days=5)
print("5 days back date :", result.date()) # 2026-04-01

#5 days ahead date.
result2 = curr_date_time + timedelta(days=5)
print("#5 days ahead date :", result2.date())
