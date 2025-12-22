# Security Log Timestamp Practice — Lists and Tuples (Python)

## Project Summary

A small Python project that simulates security log timestamp processing by working through hourly intervals (0–10).  
The script demonstrates when to use a flexible structure (**list**) for updates, and when to use a fixed structure (**tuple**) to prevent accidental changes.

## Cybersecurity Context

Security monitoring tools often generate alerts tied to time windows (hourly intervals).  
This script treats hours as numeric intervals and performs simple analysis steps that match common automation patterns:
- build a list of time intervals
- filter values (even hours)
- apply a transformation (square each value)
- compute summary statistics (min, max, sum)
- “lock” data in a tuple to reduce accidental edits

## Files

- `list_operations.py` — runnable Python script
- `README.md` — project documentation

## How to Run (Spyder / Anaconda)

1. Open **Anaconda Navigator**
2. Launch **Spyder IDE**
3. Create or open `list_operations.py`
4. Run the script (green play button or `F5`)
5. View output in the Console

## What Each Part Does (Explained Simply)

### 1) Creating the list with `range()`

- `range(0, 11)` generates numbers starting at 0 and stopping before 11.
- `list(...)` turns that range into a real list that can be printed and edited.

### 2) Printing the full list

- `print(...)` shows the entire list so the current state is visible.

### 3) Printing even numbers

- A loop visits each number.
- `% 2` checks whether a number is evenly divisible by 2.
- Values with remainder `0` are even and get printed.

### 4) Printing each number squared

- `** 2` multiplies a number by itself.
- Example: `3 ** 2` becomes `9`.

### 5) Summary statistics

- `min(...)` finds the smallest number.
- `max(...)` finds the largest number.
- `sum(...)` adds all numbers together.

### 6) Updating the list and re-checking statistics

- `.append(99)` adds a new value to the end of the list.
- Statistics are printed again to show how the list changes affect results.

### 7) Slicing (first 3 and last 3 values)

- `list_numbers[:3]` returns the first three values.
- `list_numbers[-3:]` returns the last three values.

### 8) Tuples (fixed containers)

- A tuple stores values that should not change by accident.
- Trying to edit a tuple produces a `TypeError` because tuples are immutable.

### 9) Converting a list into a tuple

- `tuple(list_numbers)` creates a fixed snapshot of the list.

### 10) Slicing a tuple

- Tuple slicing works the same way as list slicing.
- Examples:
  - `number_tuple[:5]` returns the first five values.
  - `number_tuple[-5:]` returns the last five values.

## Recruiter Notes (Skills Demonstrated)

- Python fundamentals: `range`, loops, conditionals, formatting
- List operations: creation, iteration, append, slicing
- Basic analytics: min/max/sum
- Data integrity concept: tuple immutability for safer “read-only” data snapshots
- Clear, traceable console output for validation and troubleshooting
