# Exercise 3: The battery charger with efficiency check
# Initialize the battery level
battery = 0
increment = 10 # Initialize charging increment

# Start charging the battery
while battery < 100:
    # Charge the battery
    battery += increment
    print(f"Battery is now at {battery}%")
    
    # Check the efficiency and adjust the charging rate
    if battery == 50:
        print("Efficiency check: increasing charge rate.")
        increment = 15
    elif battery == 80:
        print("Efficiency check: Reducing charge rate to prevent overcharging.")
        increment = 5
        
# Battery is fully charged
print("The battery is now fully charged.")