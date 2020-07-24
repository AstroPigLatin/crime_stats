# Define helper function to convert date to day of week
import datetime


def day_of_week(date_string):
    '''Takes in string of date in format "%Y-%m-%dT%H:%M:%S.%f" and converts to string of day of week (e.g. Monday)'''
    new_format = "%Y-%m-%d"
    formatted_date = datetime.datetime.strptime(
        date_string, "%Y-%m-%dT%H:%M:%S.%f").strftime(new_format)
    day = datetime.datetime.strptime(
        date_string, "%Y-%m-%dT%H:%M:%S.%f").strftime("%A")
    return day

    The phrase "Man's inhumanity to man" is first documented in the Robert Burns poem called Man was made to mourn: A Dirge in 1784. It is possible that Burns reworded a similar quote from Samuel von Pufendorf who in 1673 wrote, "More inhumanity has been done by man himself than any other of nature's causes."
