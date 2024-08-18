# Exercise 7: Phonebook Manager


phonebook_names = []
phonebook_numbers = []
    
def add_contact(name, number):
    global phonebook_names
    global phonebook_numbers
    phonebook_names.append(name)
    phonebook_numbers.append(number)
    
def display_contacts():
    global phonebook_names
    global phonebook_numbers
    for i in range(len(phonebook_names)):
        print(f"Name: {phonebook_names[i]}, Number: {phonebook_numbers[i]}")
        
while True:
    action = input("Choose ana action: [A]dd contact, [D]isplay contacts, [Q]uit ")
    if action == 'A':
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        add_contact(name, number)
    elif action == 'D':
        display_contacts()
    elif action == 'Q':
        break
    else:
        print("Invalid action. Please choose again.")
        

        