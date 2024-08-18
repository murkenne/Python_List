'''
Exercise 1: The Smart Home Morning Routine:

You are programming a smart home system to perform a series of actions as pasrt of a morning routine.
The system should greet you, inform you of the weather, remind you of your first calender event, and tell you if you have unread emails.  

**Instructions**:

1. Define a function called 'morning_routine()' that takes no arguments.     
2. Inside the funtion, print "Good Morning!" to simulate a greeting. 
3. Create a list of weather conditions for the week.
4. Use a loop to iterate over the weather list and use an 'if' statement to check if the current day's weather is "Rain". If it is, print a reminder to take an umbrella. 
5. Create a list of calender events for the week.   
6. Use a loop to find today's event and print it as a reminder.
7. Create a variable to store the number of unread emails. 
8. Use an 'if' statement to check if there are any unread emails and print the number if there are. 
9. Call the 'morning_routine()' function to execute the morning routine.  

**Hint**:
You can use the 'datetime' module to get the current day of the week if you want to match the weather and events to the actual day.
'''

import datetime 

def morning_routine():
    print("Good morning!")
    
    weather_conditions = ["Sunny", "Rainy","Cloudy","Rainy","Sunny","Cloudy", 'Windy']
    
    today_weather = weather_conditions[datetime.datetime.today().weekday()]
    # print(datetime.datetime.today().weekday())
    # print(today_weather)
    if today_weather == "Rainy":
        print("Don't forget your umbrella, it's rainy today.")
        
    calender_events = ['Gym', "Meeting with Bob", "Dentist appointment", 'Lunch with Sarah', "Grocery shopping"]
    today_event = calender_events[datetime.datetime.today().weekday()]
    
    print(f"Today's event: {today_event}")
    
    unread_emails = 5
    if unread_emails > 0:
        print(f"You have {unread_emails} unread emails.")
        
morning_routine()