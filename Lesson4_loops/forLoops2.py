# Festival Planner

booth_types = ["Food", "Games", "Music", "Crafts"]
schedule_times = ["10:00AM", "1:00PM", "3:00PM", "5:00PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

# Iterating over the booth types with a for loop
for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, item needed {item}")