# Exercise 4: The Group Expense Tracker

def track_expenses(*expenses):
    total_expenses = sum(expenses)
    print(f'The total expenses are: {total_expenses}')
    
    highest_expense = max(expenses)
    spender = expenses.index(highest_expense)+1
    print(f'Person {spender} is the highest spender with an expense of: {highest_expense}')

group_expenses = []

while True:
    expense_input = input("Enter an expense amount or 'done' to finish: ")
    
    if expense_input.lower() == 'done':
        break
    else:
        expense = float(expense_input)
        group_expenses.append(expense)
        
track_expenses(*group_expenses)