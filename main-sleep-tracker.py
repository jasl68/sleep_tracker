# main.py
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ask for user input for sleep date and time, 24hr time to assist with calculations
def enter_sleep_date(day):
    print("What was the date on " + str(day) + "? Please enter the date in YYYY-MM-DD e.g. 2024-01-22: ")
    sleep_date = input()
    date = datetime.strptime(sleep_date, "%Y-%m-%d")
    print()
    return date

def enter_sleep_time(day):
    print("What time did you go to bed on " + str(day) + "? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
    sleep_time = input()
    time1 = datetime.strptime(sleep_time, "%H:%M")
    print()
    return time1

#ask for user input for awake time
def enter_awake_time():
    print("What time did you wake up? Please enter the time in 24hr format using HH:MM e.g. 08:00 ")
    awake_time = input()
    time2 = datetime.strptime(awake_time, "%H:%M")
    print()
    return time2

def calculate_sleep_duration(time1, time2):
    if time2 < time1:
            time2 += timedelta(days=1)
    #calculating total hours of sleep
    sleep_duration = time2 - time1
    return sleep_duration

def sleep_summary(week_info, total_sleep_secs):
    print("Here is a summary of your sleep for this week: ")
    for day, info in week_info.items():
        if info:
            date, duration = info
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            print(f"{day}: Date - {date}, Sleep duration - {hours} hours and {minutes} minutes")
        else:
            print(f"{day}: No data")
    
    total_sleep_hours = total_sleep_secs // 3600
    total_sleep_minutes = (total_sleep_secs % 3600) // 60
    print()
    print("The total hours you slept this week: {} hours and {} minutes".format(total_sleep_hours, total_sleep_minutes))
    print()

    #average hours of sleep throughout week
    average_sleep_secs = total_sleep_secs / 7
    average_sleep_hours = average_sleep_secs // 3600
    average_sleep_minutes = (average_sleep_secs % 3600) // 60
    print("The average number of hours you slept over the week: {} hours and {} minutes".format(int(average_sleep_hours), int(average_sleep_minutes)))

     

def main():
    #an empty dict with days of week as keys and empty values
    #dict where keys are dates and the values are the hours of sleep
    week_info = {
        "Monday": None,
        "Tuesday": None,
        "Wednesday": None,
        "Thursday": None,
        "Friday": None,
        "Saturday": None,
        "Sunday": None
        }
    #new variable for total accumulated hrs of sleep
    total_sleep_secs = 0
    
    #introductory text
    print("Hi there!")
    print("Welcome to the Best Sleep Tracker :)")
    print()
    
    #list days of week to run through
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #need a for loop
    for day in days_of_week: 
    #ask for user input for sleep date and time, 24hr time to assist with calculations
        date = enter_sleep_date(day)
        
        time1 = enter_sleep_time(day)
        time2 = enter_awake_time()

        sleep_duration = calculate_sleep_duration(time1, time2)

    # Extract the hours and minutes from the timedelta object
        hours = sleep_duration.seconds // 3600
        minutes = (sleep_duration.seconds % 3600) // 60
        print("The total hours you slept last night: {} hours and {} minutes".format(hours, minutes))
        print()
    
    #add to dictionary
        week_info[day] = (date.strftime("%Y-%m-%d"), sleep_duration)
    
    #update total sleep time
        total_sleep_secs += sleep_duration.total_seconds()

    sleep_summary(week_info, total_sleep_secs)
    print()
    print("Thank you for trying me out! Feel free to come back again if you want to track a different week of sleep :)")
    print()  

if __name__ == "__main__":
    main()
    
