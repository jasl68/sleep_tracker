# main.py
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    #introductory text
    print("Hello Human!")
    print("Welcome to the Sleep Tracker")

    #ask for user input for sleep date and time, 24hr time to assist with calculations
    print("When did you go to bed? Please enter the date in YYYY-MM-DD e.g. 2024-01-22: ")
    sleep_date = input()
    date = datetime.strptime(sleep_date, "%Y-%m-%d")
    print("What time did you go to bed? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
    sleep_time = input()
    time1 = datetime.strptime(sleep_time, "%H:%M")
    
    #ask for user input for awake time
    print("What time did you wake up? Please enter the time in 24hr format using HH:MM e.g. 22:30 ")
    awake_time = input()
    time2 = datetime.strptime(awake_time, "%H:%M")
    
    #if wake up time is before sleep time, +1 day so date moves forward
    if time2 < time1:
        date += timedelta(days=1)

    #calculating total hours of sleep
    sleep_hours = time2 - time1
    print("The total hours you slept was: " + str(sleep_hours) + "hours")

    hours = sleep_duration.seconds // 3600
    minutes = (sleep_duration.seconds % 3600) // 60

    print("The total hours you slept was: {} hours and {} minutes".format(hours, minutes))

if __name__ == "__main__":
    main()
    
