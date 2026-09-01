### Loops
Loops allow us to repeat a block of code multiple times. Instead of repeating ourselves by copy-pasting lines, we can write a clean loop to handle the repetition for us.
For example, if we want to print "meow" three times, we could do:
```python
print("meow")
print("meow")
print("meow")
```
But if we wanted to do this 50 or 500 times, copy-pasting is not a good design because:
* It makes our code excessively long and ugly.
* If we want to change "meow" to "woof", we would have to change it in many places.

---

### while loops
A `while` loop repeats a block of code as long as a certain boolean expression (a question that evaluates to `True` or `False`) remains `True`.

To write a `while` loop, you typically need to:
1. Create a counter variable (often called `i` for integer) and initialize it.
2. Ask a question using the `while` keyword.
3. Update the counter variable inside the loop so it eventually stops.

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```

### infinite loops
An infinite loop is a loop that continues to run forever because its boolean expression never becomes `False`.
This usually happens by accident if you forget to update your counter variable inside the loop.
```python
i = 3
while i != 0:
    print("meow")
    # i is always 3, so this loop never stops!
```
note: If you ever get stuck in an infinite loop in your terminal, press **Control + C** (Ctrl+C) to cancel or interrupt the execution and regain control of your computer.

### shorthand operators
Since updating counter variables (adding or subtracting 1) is incredibly common in programming, Python provides a more succinct syntax to do it:
* `i += 1` is shorthand for `i = i + 1` (increments `i` by 1)
* `i -= 1` is shorthand for `i = i - 1` (decrements `i` by 1)

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```
note: Programmers and computer scientists conventionally start counting from `0` instead of `1`. When starting at `0`, we loop while `i < 3` to run exactly 3 times (for `i = 0`, `i = 1`, and `i = 2`).

---

### lists
A list is a Python data type that can contain multiple values in a single variable. In the real world, a list is a list of things; in Python, it's the same!
To create a list, you place your values inside **square brackets `[]`** separated by commas:
```python
students = ["Hermione", "Harry", "Ron"]
```

### indexing into lists
Lists in Python are **zero-indexed**. This means the very first item is at position `0`, the second is at `1`, and so on. To access a specific item, we use square brackets with the index number:
```python
students = ["Hermione", "Harry", "Ron"]
print(students[0]) # Output: Hermione
print(students[1]) # Output: Harry
print(students[2]) # Output: Ron
```

### len()
The `len()` function returns the total number of items (the length) in a list or other collection.
```python
students = ["Hermione", "Harry", "Ron"]
print(len(students)) # Output: 3
```

---

### for loops
A `for` loop is a cleaner way to iterate (loop) over a specific list of items or range of numbers. Unlike `while` loops which require you to manually initialize and increment your variables, a `for` loop manages this automatically!

```python
for student in ["Hermione", "Harry", "Ron"]:
    print(student)
```
Why? In this loop, Python automatically assigns `student` to the first item ("Hermione"), prints it, then assigns it to "Harry", prints it, and finally to "Ron" and prints it.

### range()
The `range()` function returns a sequence of numbers. It takes an integer as input and by default returns numbers starting at `0` up to, but not including, that integer.
This is incredibly useful when you want a loop to run a specific number of times without writing out a list of numbers manually.

```python
for i in range(3):
    print("meow")
```
note: If we need a variable to satisfy Python's syntax but we don't actually use the variable's value in our code, the pythonic convention is to name the variable as a single underscore `_`.
```python
for _ in range(3):
    print("meow")
```

---

### string multiplication
In Python, you can use the multiplication operator `*` to repeat strings! This allows you to print repeated text in a single line.
```python
print("meow" * 3) # Output: meowmeowmeow
```

To format them on separate lines, you can include the new line escape sequence `\n`:
```python
print("meow\n" * 3, end="")
```
note: By default, the `print()` function automatically adds a newline (`\n`) at the end of its output. By adding `end=""`, we tell Python not to add that default extra blank line, keeping our output perfectly formatted.

---

### while True (getting valid input)
A common paradigm in Python for getting valid user input is to create a deliberate infinite loop using `while True`, and then break out of it only when the user gives us a value that meets our expectations (like a positive integer).

To control this loop, we use two key statements:
* **`continue`**: Forces the loop to immediately skip the rest of the current iteration and go back to the top of the loop to ask the question again.
* **`break`**: Breaks out of the loop completely, jumping down to the next line of code outside the loop.

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
```
Why? This keeps asking the user "What's n?" until they enter an integer that is greater than `0`. Once they do, the `break` statement runs and stops the loop.

---

### returning values from loops
When wrapping input validation inside a function, we can use the `return` keyword to both exit the loop and return the validated value to the caller immediately.
```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
```
note: `return` has the side effect of breaking out of any loop it is currently inside, meaning you don't even need to use `break` when you use `return`!

---

### dictionaries (dict)
A dictionary is a powerful Python data structure that allows you to associate one value with another. It represents a collection of **key-value pairs**, where each "key" acts like a word in a real-world dictionary, and its "value" acts like the definition!

To create a dictionary, we use **curly braces `{}`** and colons `:` to separate keys and values:
```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
```

### indexing into dictionaries
Unlike lists which must be indexed with numbers (`0, 1, 2`), dictionaries allow us to index using actual words (the keys):
```python
print(students["Hermione"]) # Output: Gryffindor
print(students["Draco"])    # Output: Slytherin
```

### iterating over dictionaries
When you use a `for` loop to iterate over a dictionary, it iterates over all of the **keys** by default.
```python
for student in students:
    print(student)
```
Output:
```
Hermione
Harry
Ron
Draco
```

To print both the key and the associated value, we use the key to look up the value inside the dictionary:
```python
for student in students:
    print(student, students[student], sep=", ")
```
Output:
```
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
```

---

### lists of dictionaries
To represent more complex data, we can store multiple dictionaries inside a single list. This is extremely useful when representing databases of items or people where each item has multiple pieces of associated data (e.g., a student's name, their house, and their patronus).

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
```

### None
In Python, `None` is a special keyword that represents the official **absence of a value**. It's useful when you want to explicitly state that a piece of data is missing, rather than leaving it empty or using a blank string.
In the example above, `None` is used to represent that Draco has no known patronus.

### iterating over a list of dictionaries
We can use a `for` loop to iterate through the list of dictionaries and access each individual key-value pair:
```python
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```
Output:
```
Hermione, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell Terrier
Draco, Slytherin, None
```

---

### nested loops
A nested loop is simply a loop inside another loop. This is very useful when working with two-dimensional spaces, like printing a grid or a square of characters.

Let's look at printing a 3x3 square of hashes (`#`):
```python
for i in range(3):      # Outer loop (controls the row)
    for j in range(3):  # Inner loop (controls each brick in the row)
        print("#", end="")
    print()             # Prints a new line at the end of each row
```
Output:
```
###
###
###
```

### loop decomposition & abstraction
Instead of nesting loops directly, we can use **abstraction** by decomposing our problem into smaller functions. This makes our code much more readable and easier to maintain.
For example, we can create a `print_row` function and then call it inside our main square-printing function:

```python
def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
```
Why? This achieves the exact same 3x3 square output, but it makes the code modular and easier to understand because we don't have to look at complex nested loops all in one place.

---

### Summary Table of Data Structures

| Data Structure | Syntax Example | When to use | Key Feature |
| --- | --- | --- | --- |
| **List** | `["Harry", "Ron"]` | When you have a collection of individual, ordered items | Zero-indexed |
| **Dictionary (dict)** | `{"Harry": "Gryffindor"}` | When you want to associate key-value pairs (words and definitions) | Key-based lookup |
| **List of Dictionaries** | `[{"name": "Harry", "house": "Gryffindor"}]` | When representing a database of records, where each item has multiple attributes | Multi-dimensional and highly organized |




