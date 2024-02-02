"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

import datetime

def date_passed(todays_date, scheduled_date):
    # Function to remove the 'th', 'st', 'nd', 'rd' suffixes from the day:
    def remove_day_suffix(date_str):
        # first separate the numeric (day) and non-numeric (month and suffix) parts of the string:
        day_part= ''.join([i for i in date_str if i.isdigit()])
        month_part= ''.join([i for i in date_str if not i.isdigit()])
        # remove the 'st', 'nd', 'rd', 'th' suffixes from the non-numeric part:
        for suffix in ['st', 'nd', 'rd', 'th']:
            month_part = month_part.replace(suffix, '')
        # return the formatted date string, combining the day and cleaned month parts
        return day_part + ' ' + month_part.strip() # .strip() 方法用于移除字符串两端的空白字符。这是为了确保最终的字符串没有前导或尾随的空格
            
       
    # Now convert the formatted date strings to date objects:
    today = datetime.datetime.strptime(remove_day_suffix(todays_date), "%d %B")  #strptime函数根据'%d %B'的格式说明符，将todays_date字符串解析成一个datetime对象，并将其赋值给today变量。
    scheduled= datetime.datetime.strptime(remove_day_suffix(scheduled_date), "%d %B")
        
    # Compare the two dates
    if today == scheduled:
        print("The scheduled date is today.")
    elif today > scheduled:
        print("The scheduled date has passed.")
    else:
        print("The scheduled date is yet to pass.")
    

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
date_passed("2nd February", "12th February")

