"""Calling yeardays2calendar() produces a sequence of “month row” lists. Each list includes the months as another list
of weeks. The weeks are lists of tuples made up of day number (1-31) and weekday number (0-6). Days that fall outside
of the month have a day number of 0."""

import calendar
import pprint

cal = calendar.Calendar(calendar.SUNDAY)
cal_data = cal.yeardays2calendar(2022, 8)
print('len(cal_data)   :', len(cal_data))

top_month = cal_data[0]
print('len(top_month)   :', len(top_month))

first_month = top_month[0]
print('len(first_month) :', len(first_month))

print('first_month:')
pprint.pprint(first_month, width=65)