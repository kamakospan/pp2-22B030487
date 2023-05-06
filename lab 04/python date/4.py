from datetime import datetime, timedelta, time

today = datetime.now()
newdate = today + timedelta(days = 16)

# differenceinseconds = (newdate - today).total_seconds()
differenceinseconds = (newdate - today).total_seconds()
print(differenceinseconds)