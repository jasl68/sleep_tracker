# main.py
def main():
    #introductory text
    print("Hello Human!")
    print("Welcome to the Sleep Tracker")

    #ask for user input
    print("What time did you go to bed? Please enter the time in 24hr format e.g. 2210 hours ")
    sleep_time = float(input())
    #user input in 24hr time to assist with calculations
    awake_time = float(input("What time did you wake up? "))
    sleep_hours = (sleep_time - awake_time) / 100
    print("The total hours you slept was: " + str(sleep_hours) + "hours")

if __name__ == "__main__":
    main()
    
