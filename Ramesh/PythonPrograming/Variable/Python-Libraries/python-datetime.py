from datetime import datetime, timedelta


curr_date_time = datetime.now()
print(curr_date_time) # 2026-04-08 16:57:24.054756
print(curr_date_time.day)
print(curr_date_time.month)
print(curr_date_time.year)
print(curr_date_time.minute)
print(curr_date_time.date())

unique_name = datetime.now().strftime("%d_%m_%H_%M_%S")
print(unique_name)

# 5 days back date.
result = curr_date_time - timedelta(days=1)
print(result.date())


# 5 days ahead date.
result2 = curr_date_time + timedelta(days=5)
print(result2.date())
