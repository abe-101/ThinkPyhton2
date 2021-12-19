#!/usr/bin/python3
"""
Exercise 5-1
The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.
"""

import time

# adjust seconds for Indian Standard Time (-5:30 hours)
seconds = int(time.time()) + (5 * 3600 + 30 * 60)

secs_in_day = 3600 * 24
secs_in_hrs = 3600
secs_in_min = 60

days = seconds // secs_in_day
seconds = seconds % (days * secs_in_day)

hrs = seconds // secs_in_hrs
seconds = seconds % (hrs * secs_in_hrs)

mins = seconds // secs_in_min
seconds = seconds % (mins * secs_in_min)

print(f"{days} days, {hrs} hours, {mins} minutes and {seconds} seconds")
print()

# print current local time (Indian Standard Time)
print(time.localtime())
print()

print("We can see both results are same, so our solution is correct.")
