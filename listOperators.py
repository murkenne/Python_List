# Given the 2 list

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out if Alice submitted their assignment and attended class

if "Alice" in attended and "Alice" in submitted:
    print("Alice attended class and submitted assignment.")
elif "Alice" not in attended or "Alice" not in submitted:
    print("Alice did not attend and or did not submit assignment!")