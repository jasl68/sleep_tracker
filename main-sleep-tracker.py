# main.py
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ask for user input for sleep date and time, 24hr time to assist with calculations
def enter_sleep_date():
    print("When did you go to bed? Please enter the date in YYYY-MM-DD e.g. 2024-01-22: ")
    sleep_date = input()
    date = datetime.strptime(sleep_date, "%Y-%m-%d")
    print()

def enter_sleep_time():
    print("What time did you go to bed? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
    sleep_time = input()
    time1 = datetime.strptime(sleep_time, "%H:%M")
    print()

#ask for user input for awake time
def enter_awake_time():
    print("What time did you wake up? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
    awake_time = input()
    time2 = datetime.strptime(awake_time, "%H:%M")
    print()

def main():
    #an empty dict
    #week_info = {}
    #store sleep data in list/dictionary where each entry -> day of the week
    #dict where keys are dates and the values are the hours of sleep
    #new variable for total accumulated hrs of sleep
    total_sleep_secs = 0

    #introductory text
    print("Hello Human!")
    print("Welcome to the Best Sleep Tracker")
    print()
    
    #need a for loop
    for sleep_date in range(2): 
    #ask for user input for sleep date and time, 24hr time to assist with calculations
        print("When did you go to bed? Please enter the date in YYYY-MM-DD e.g. 2024-01-22: ")
        sleep_date = input()
        date = datetime.strptime(sleep_date, "%Y-%m-%d")
        print()
        
        print("What time did you go to bed? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
        sleep_time = input()
        time1 = datetime.strptime(sleep_time, "%H:%M")
        print()
        
        print("What time did you wake up? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
        awake_time = input()
        time2 = datetime.strptime(awake_time, "%H:%M")
        print()

        if time2 < time1:
            date += timedelta(days=1)
            time2 += timedelta(days=1)

    #calculating total hours of sleep
        sleep_duration = time2 - time1

    # Extract the hours and minutes from the timedelta object
        hours = sleep_duration.seconds // 3600
        minutes = (sleep_duration.seconds % 3600) // 60
        print("The total hours you slept last night: {} hours and {} minutes".format(hours, minutes))
        print()
        
        total_sleep_secs += sleep_duration.total_seconds()
    
    total_sleep_hours = total_sleep_secs // 3600
    total_sleep_minutes = (total_sleep_secs % 3600) // 60
    print("The total hours you slept this week: {} hours and {} minutes".format(total_sleep_hours, total_sleep_minutes))
    print()

    

if __name__ == "__main__":
    main()
    
