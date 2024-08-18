'''
**Problem Statement**:
You are creating a feature for a travel app that allows users to view the temperature in both Celcius and Fahrenheit,
so rhey can easily understand the weather forecast no matter where they travel.  

*Instructions**:

1. Create a list of temperature in Celsius that you want to convert. 
2. Loop through the list, and for each temperature in Celsius, convert it to Fahrenheit.
3. Print out both the Celsius and Fahrenheit temperature using f-strings for formatted output.  
'''
celsius_temperatures = [10, 20, 25, 30, 35]

for celsius in celsius_temperatures:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} C is equivalent to {fahrenheit} F")