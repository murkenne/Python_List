#  You have a list of daily temperatures for one month, and you'd like to extract specific data from it.
# Given list of temperatures

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1 Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:

second_week_temperatures = temperatures[7:14]

print("Temperatures for the second week: ", second_week_temperatures)

'''Task 2: Extract all the temperatures above 100. HINT: add the 
temperatures over 100 to a new list, or use list slicing to get the temperatures.
'''

temperatures_above_100 = [temp for temp in temperatures if temp > 100 ]

print("Temperatures of 100: ", temperatures_above_100)