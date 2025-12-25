# Security Log Timestamp Analysis — Lists & Tuples (Python)

## What this project is

A Python fundamentals project that models log-timestamp processing using **hourly intervals** (0–10).  
The script demonstrates:

- Generating numerical ranges with `range()`
- Filtering even intervals
- Transforming values with a loop (squaring)
- Calculating summary statistics (`min`, `max`, `sum`)
- Using **lists** for editable data
- Converting to **tuples** to prevent accidental changes

## Files

- `list_operations.py` — original script (kept as written)
- `README.md` — documentation and line-by-line explanation

## How to run (Spyder)

1. Open Anaconda Navigator
2. Launch Spyder IDE
3. Open `list_operations.py` 
4. Run the script (Run button or `F5`)
5. Review output in the console

---

## Line-by-line explanation of the original script

> Notes:
> - A **list** is a container that can be changed (items can be added or removed).
> - A **tuple** is a container that cannot be changed after creation (immutable).

### Comments (lines starting with `#`)

Lines that start with `#` are comments.  
They are ignored by Python and exist only to explain intent.

### Creating a list using `range()`

```python
list_numbers = list(range(0, 11))
```
- `range(0, 11)` creates a sequence starting at `0` and stopping before `11`.
- That produces: 0, 1, 2, …, 10
- `list(...)` converts the sequence into a real list that can be printed and modified.

```python
print("Full list of numbers", list_numbers)
```
- `print()` writes content to the console.
- This shows the complete list so the script output is traceable.

### Printing only even numbers (loop + logic)

```python
print("\nEven numbers in the list")
```
- `\n` adds a blank line before the next text in the console.

```python
for i in list_numbers:
```
- A `for` loop walks through each number stored in `list_numbers`.
- `i` is the loop variable that temporarily holds the current number.

```python
if i % 2 == 0:
```
- `%` is the modulus operator (remainder after division).
- `i % 2 == 0` means the number divides evenly by 2, so it is even.

```python
print(i)
```
- Prints each even number that passes the condition.

### Squaring each number (loop + math operator)

```python
print("\nEach Number Squared")
```
- Adds a label for the next section of output.

```python
for i in list_numbers:
```
- Loops through the same list again.

```python
squared = i ** 2
```
- `**` is the exponent operator.
- `i ** 2` means “i multiplied by itself” (square).
- The result is stored in `squared`.

```python
print(f"{i} squared is {squared}")
```
- This is an f-string (formatted string).
- It inserts values of `i` and `squared` directly into the printed message.

### Summary statistics: min, max, sum

```python
print("\nMinimum value in list_numbers:", min(list_numbers))
```
- `min(...)` returns the smallest value in the list.

```python
print("Max vale in list_numbers:", max(list_numbers))
```
- `max(...)` returns the largest value in the list.

```python
print("Sum value in list_numbers:", sum(list_numbers))
```
- `sum(...)` adds all values together.

### Appending a new number and recalculating statistics

```python
list_numbers.append(99)
```
- `.append(99)` adds `99` to the end of the list.
- This demonstrates list mutability (lists can change).

```python
print("Updated list of number:", list_numbers)
```
- Shows the list after the change.

```python
print("\nNew Minimum value in list_numbers:",min(list_numbers))
print("New Max value in list_numbers:", max(list_numbers))
print("New sum value in list_numbers:", sum(list_numbers))
```
- Recomputes min/max/sum to show how statistics change when data changes.

### Slicing: first 3 and last 3 elements

```python
print("First three elements:", list_numbers[:3])
```
- `list_numbers[:3]` returns the first three values (index 0, 1, 2).

```python
print("Last three elements:", list_numbers[-3])
```
- `list_numbers[-3]` returns the single element that is “third from the end”.
- To print the last three elements as a group, the slice form is:
  - `list_numbers[-3:]`

### Tuple creation (fixed container)

```python
coordinates = (15,20,30)
```
- Creates a tuple named `coordinates` with three integer values.

```python
print("Original coordinates tuple:", coordinates)
```
- Prints the tuple contents.

```python
#coordinates[0] = 99
```
- This line is commented out.
- If it were active, it would raise an error because tuples cannot be modified.

```python
print("Tuple statement cannot be change because is immutable")
```
- Prints the immutability message.

### Converting the list into a tuple

```python
number_tuple = tuple(list_numbers)
```
- Converts the current list into a tuple.
- This creates a fixed snapshot of the numeric data.

```python
print("This is my list which is in parenthesis", list_numbers)
print("This is my tuple which is in brackets", number_tuple)
```
- Prints both containers for comparison.
- Note:
  - Lists display with **square brackets**: `[...]`
  - Tuples display with **parentheses**: `(...)`

### Tuple slicing

```python
print("I am slicing my tuple and printing the first 5 values:", number_tuple[:5])
```
- `number_tuple[:5]` slices the tuple to show the first five elements.
- Slicing works the same way on lists and tuples; the difference is mutability.

---

## What you learned

- Demonstrates Python control flow: loops, conditionals
- Demonstrates list operations: creation, append, slicing
- Demonstrates built-in aggregation: min, max, sum
- Demonstrates data integrity concept: converting to tuples for immutability
- Provides traceable console output suitable for validation


----

screenshots of my work:


<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/13236ad5-7188-4467-93a8-ae37cbc73fef" />


----


<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/c5cc9896-7c5e-4ef7-8f6b-ae82314e4bc8" />


