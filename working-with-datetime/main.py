from datetime import date, datetime, time

today = date.today()
print("Today's date: ", today)
print("Day: ",today.day)
print("Month: ",today.month)
print("Year: ",today.year)

print(today.strftime("%A %d %B %Y"))
print(today.strftime("%a %d %b %y"))

now = datetime.now()
print("now it is: ", now)
print("hour", now.hour)
print("minute: ", now.minute)
print("second: ", now.second)
print("micro-seconds: ", now.microsecond)

t = time(15,30, 20)
print("Time: ", t)

print(t.strftime("%A %B %D"))
print(t.strftime("%a %b %d"))


