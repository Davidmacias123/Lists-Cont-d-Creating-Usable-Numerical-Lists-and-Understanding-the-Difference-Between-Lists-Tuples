"""
Security Log Timestamp Practice (Lists + Tuples)

Purpose
- Build a numeric list of hourly intervals (0–10)
- Identify even-hour intervals
- Print each interval squared (simple transformation loop)
- Calculate summary statistics (min, max, sum) and re-calculate after an update
- Demonstrate why tuples are used when values should not be changed
"""

# 1) Generate a list of numbers from 0 to 10 (inclusive) using range()
list_numbers = list(range(0, 11))
print("Full list of numbers:", list_numbers)

# 2) Print only the even numbers (logic)
print("\nEven numbers in the list:")
for n in list_numbers:
    if n % 2 == 0:
        print(n)

# 3) Use a loop to print each number squared
print("\nEach number squared:")
for n in list_numbers:
    squared = n ** 2
    print(f"{n} squared is {squared}")

# 4) Summary statistics: minimum, maximum, sum
print("\nSummary statistics (original list):")
print("Minimum value:", min(list_numbers))
print("Maximum value:", max(list_numbers))
print("Sum value:", sum(list_numbers))

# 5) Add a new number and re-calculate summary statistics
list_numbers.append(99)
print("\nUpdated list of numbers:", list_numbers)

print("\nSummary statistics (after append):")
print("Minimum value:", min(list_numbers))
print("Maximum value:", max(list_numbers))
print("Sum value:", sum(list_numbers))

# 6) Slicing: first 3 and last 3 elements
print("\nFirst three elements:", list_numbers[:3])
print("Last three elements:", list_numbers[-3:])

# 7) Tuples: create a tuple with three values
coordinates = (15, 20, 30)
print("\nOriginal coordinates tuple:", coordinates)

# 8) Attempting to modify a tuple value (kept as a safe demo via try/except)
try:
    coordinates[0] = 99  # tuples are immutable, so this raises TypeError
except TypeError as e:
    print("Tuple modification attempt blocked:", e)

# 9) Explain why tuples cannot be changed
print("Tuples cannot be changed because they are immutable (fixed once created).")

# 10) Convert the numerical list to a tuple
number_tuple = tuple(list_numbers)
print("\nList (uses square brackets):", list_numbers)
print("Tuple (uses parentheses):", number_tuple)

# 11) Slice the tuple and print results
print("Tuple slice (first 5 values):", number_tuple[:5])
print("Tuple slice (last 5 values):", number_tuple[-5:])
