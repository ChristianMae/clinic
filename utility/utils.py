import calendar
from datetime import timedelta


def date_offset_generator(date):
    days_available = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if calendar.day_name[date.weekday()] in days_available:
        return date
    elif calendar.day_name[date.weekday()] == 'Sunday':
        return date + timedelta(days=1)
    else:
        return date + timedelta(days=2)
