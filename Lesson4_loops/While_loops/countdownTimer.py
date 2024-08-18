'''# Initialize timer
timer = 10

# Start the countdown
while timer > 0:
    print(timer)
    timer -= 1 # Decrement
    
# Print the final message
print("Time is up!")'''


# Exercise 2: The Patient Queue
# Initialize the number of patients in the queue
patients = 5

# Process the queue
while patients > 0:
    print(f"Patient number {patients} please come in.")
    patients -=1 # Call the next patient
    
# All patients have been called
print("There are no more patients in the queue.")