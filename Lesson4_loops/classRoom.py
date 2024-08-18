# Class room seating
# 30 students - 5 rows
# Each row can seat an equal number of students.
# Use a for loop with the range function to assign and print a seat number for each student.
# Seat number should start at 1 and increase sequentially.

total_students = 30
rows = 5

students_per_row = total_students // rows

for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row-1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat_number}")