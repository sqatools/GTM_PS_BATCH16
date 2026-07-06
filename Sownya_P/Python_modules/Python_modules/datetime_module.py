from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()  

print("Current Date and Time:", current_datetime)

print("date:", current_datetime.date())
print("time:", current_datetime.time())
print("month:", current_datetime.month)

# output in string formating

formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# PAST DATE or future date
from datetime import timedelta

# Get the past date (2 days ago)
past_date = current_datetime - timedelta(days=2)
print("Past Date (2 days ago):", past_date)

# Get the future date (7 days from now)
future_date = current_datetime + timedelta(days=7)
print("Future Date (7 days from now):", future_date)