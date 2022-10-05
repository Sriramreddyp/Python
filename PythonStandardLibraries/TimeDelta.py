from datetime import datetime, timedelta
import time

dt1 = datetime(2018, 1, 1) + timedelta(days=1)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)

print("Days", duration.days)
print("seconds", duration.seconds)
print("TotalSeconds", duration.total_seconds())
