"""To produce a calendar formatted for a locale other than the current default, use LocaleTextCalendar or
LocaleHTMLCalendar"""

import calendar

c = calendar.LocaleTextCalendar(locale='en_US')  #TODO
print(c.prmonth(2022, 8))
