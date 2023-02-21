from datetime import timedelta, date
print("Today: ", date.today())
print("Yesterday: ", date.today() - timedelta(days=1))
print("Tomorrow: ", date.today() + timedelta(days=1))
