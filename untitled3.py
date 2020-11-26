import calendar
print(calendar.weekheader(3))

print(calendar.firstweekday())

print(calendar.month(2020,11))

print(calendar.monthcalendar(2020,11))

print(calendar.calendar(2020))

dayOfTheWeek= calendar.weekday(2020,11,6)
print(dayOfTheWeek)

isLeapYear= calendar.isleap(2020)
print(isLeapYear)

howManyLeapDays= calendar.leapdays(2000, 2005)
print(howManyLeapDays)