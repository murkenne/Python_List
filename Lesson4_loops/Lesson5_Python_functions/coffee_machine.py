# Exercise 2: The Versatile Coffee Machine.

def make_coffee(coffee_type = "espresso"):
    print(f"Making a cup of {coffee_type} coffee!")

coffee_types = ["espresso", "latte", 'cappuccino', 'americano', 'mocha']

for type in coffee_types:
    make_coffee(type)
    if type == 'cappuccino':
        print("Ah, cappuccino, a personal favorite!")

make_coffee()       