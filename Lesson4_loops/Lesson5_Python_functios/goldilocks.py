'''
Goldilocks wants to find the warmest and coolest rooms in her house based on the current temperature readings.
She has a list of temperatures for each room and needs a quick way to determine which rooms are the warmest and coolest.  

**Instructions** :

1. Create a list of temperatures and rooms for each room in the house.  
2. Determine the warmest and coolest temperature using the 'max()' and 'min()' function.  
3. Identify the rooms with these temperatures and print out the results using string formatting.  
'''

room_temperatures = [22, 24, 19, 21]
room_names = ['living room', 'kitchen', 'bedroom', 'bathroom']

warmest_temp = max(room_temperatures)
coolest_temp = min(room_temperatures)

warmest_room_index = room_temperatures.index(warmest_temp)
coolest_room_index = room_temperatures.index(coolest_temp)

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f"The {warmest_room} is the warmest with {warmest_temp}C")
print(f"The {coolest_room} is the coolest with {coolest_temp}C")

'''print(warmest_room_index, coolest_room_index)
print(room_names[warmest_room_index])'''