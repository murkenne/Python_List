# Import the random module to use its choice selection capabilites
# Create a list of participants names, including 'Alex'.
# Use a while loop to repeatedly draw a name randomly from the list of participants.    
# The loop should only terminate when 'Alex' is drawn.
# Ensure that the loop does not produce any output until 'Alex' is drawn.  

import random 

participants = ['John', 'Lila', 'Sarah', 'Alex', 'Max']

while 'Alex' not in random.choices(participants, k=1):
    pass

print("Congratulations, Alex! You've won the lucky draw")