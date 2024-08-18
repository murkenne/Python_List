# Exercise 6: The payment Splitter

def split_payment(expenses, number_of_friends):
    total_expenses = sum(expenses)
    individual_share = total_expenses / number_of_friends
    return total_expenses, individual_share

expenses =  []

number_of_friends = int(input('Enter the number of friends: '))

while True:
    expense = input("Enter an expense or 'done' to finish: ")
    if expense.lower() == 'done':
        break
    expenses.append(float(expense))
    
total, share = split_payment(expenses, number_of_friends) 

print(f'\nTotal expenses: ${total:.2f}')
print(f"Each person must pay: ${share:.2f}")   