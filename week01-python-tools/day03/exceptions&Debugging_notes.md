# Exceptions in Python

An **exception** refers to a problem in your code. When something is exceptional in your program, it means something has gone wrong that you need to solve.

---

### Syntax Error vs. Runtime Error

There are two main types of errors you will encounter:

1. **Syntax Errors**: Errors where you have typed something incorrect (like violating the grammar of Python). These are entirely on you to go back and fix before the code can even run.
2. **Runtime Errors (Exceptions)**: Errors that happen *while* your program is running. You must write defensive code to handle these, especially because you cannot control what users might input.

```
Syntax Error (Typo in code) ───> Code won't run at all. Must be fixed by programmer.
Runtime Error (Exception)  ───> Happens during execution. Can be handled defensively.
```

---

### SyntaxError
A syntax error occurs when Python cannot parse your code.
**Example:**
```python
print("hello, world
                  ^
                  missing closing quote
```
*Error Message:* `SyntaxError: unterminated string literal`

---

### ValueError
A value error occurs when a function receives an argument of the correct type but an inappropriate value.
**Example:**
```python
x = int(input("What's x? "))
```
If the user types `"cat"` instead of a number:
*Error Message:* `ValueError: invalid literal for int() with base 10: 'cat'`

---

### try & except
You can use `try` and `except` blocks to handle exceptions gracefully, preventing your program from crashing and showing scary error messages to the user.

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

```
   ┌──────────────────────────────────────────┐
   │                  try:                    │
   │  Try running the code inside this block  │
   └────────────────────┬─────────────────────┘
                        │
             Did an exception occur?
               ╱                ╲
             YES                 NO
             ╱                    ╲
   ┌────────▼─────────┐    ┌───────▼──────────┐
   │     except:      │    │  Skip except and │
   │ Handle the error │    │  continue code   │
   └──────────────────┘    └──────────────────┘
```

---

### NameError
A name error occurs when you try to use a variable or name that is not defined or does not exist.

#### The Assignment Bottleneck
Look at this code:
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
If the user inputs `"cat"`, this code will raise a `NameError: name 'x' is not defined` on the last line. 

**Why?** Let's trace the assignment operator (`=`):
```
  x    =    int(input("What's x? "))
  ^         └──────────────────────┘
Left side          Right side
                 (Raises ValueError if input is "cat")
```
Because the `ValueError` occurs on the **right side** of the assignment, the assignment process is interrupted before anything is copied to the **left side** (`x`). Therefore, `x` is never created! When you try to print `x` on the last line, it does not exist.

---

### else
The `else` block runs **only if** the code in the `try` block succeeds without raising any exceptions. This is a best practice because you should minimize the amount of code in your `try` block to avoid catching unintended errors.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

---

### Re-prompting with Loops
Instead of letting the program crash or quit immediately when a user makes a mistake, you can use an infinite loop (`while True`) to repeatedly ask for input until they cooperate.

#### Method 1: Using `else` and `break`
```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break # Exit the loop because we successfully got an integer

print(f"x is {x}")
```

#### Method 2: Shorter execution (Breaking early)
If nothing goes wrong on the first line inside `try`, Python will naturally proceed to the next line and run `break`.
```python
while True:
    try:
        x = int(input("What's x? "))
        break # Runs only if the line above succeeds!
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```

---

### Custom Functions & return
We can abstract our input-validation logic into a reusable custom function, such as `get_int()`.

Inside a loop within a function, `return` is stronger than `break`. It will not only break you out of the loop, but it will also immediately exit the function and return the value.

```python
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? ")) # break and return all in one!
        except ValueError:
            print("x is not an integer")

main()
```

---

### pass
If you want to catch an error but silently ignore it (without printing error messages or quitting), you can use the `pass` keyword. The program will stay in the loop and simply prompt the user again.

```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass # Silently catch the error and prompt again
```

---

### Writing Reusable Code (Parameters)
To make your custom function truly reusable, you shouldn't hardcode the variable name or the prompt message. Instead, let the caller function (like `main`) pass the prompt as an argument.

```python
def main():
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    print(f"x + y is {x + y}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
```

---
---


### KeyError
A **KeyError** is raised when you attempt to look up a key in a dictionary that does not exist.

**Example:**
```python
distances = {
    "Voyager 1": "163",
    "Pioneer 10": "8 au",
}
# Attempting to access a key that is not in the dictionary:
spacecraft = "James Web Space Telescope"
print(distances[spacecraft])
```
*Error Message:* `KeyError: 'James Web Space Telescope'`

---

### MemoryError
A **MemoryError** occurs when an operation runs out of available memory. In Python, this can happen if you accidentally perform string multiplication on a massive scale instead of numerical multiplication.

**Example of the String Multiplication Trap:**
If you have a distance stored as a string `"163"` instead of a float/int, and you try to multiply it by a huge number (like a conversion constant of `149597870700`):
```python
au = "163"  # Oops, this is a string!
conversion_constant = 149597870700
meters = au * conversion_constant
```
Python interprets `string * integer` as **string repetition**. It will try to repeat the text `"163"` nearly 150 billion times, instantly overflowing your computer's RAM and triggering a crash.
*Error Message:* `MemoryError`

---

### Handling Multiple Exceptions
Often, a single block of code or line of code can trigger multiple different types of errors depending on the user's input. You can define multiple `except` blocks for a single `try` block to handle each potential issue with a specific, friendly message.

#### Example: Spacecraft Distance Converter
We want to look up a spacecraft in our dictionary, convert its distance from astronomical units (AU) to a float, and convert it to meters. This line can raise:
1. `KeyError` — if the spacecraft isn't in our dictionary.
2. `ValueError` — if the distance string contains non-numeric text (like `"8 au"`) and cannot be converted to a float.

```python
distances = {
    "Voyager 1": "163",
    "Pioneer 10": "8 au",
}

def print_meters(spacecraft):
    try:
        # 1. Can raise KeyError if key doesn't exist
        # 2. Can raise ValueError if float() conversion fails
        au = float(distances[spacecraft])
    except KeyError:
        print(f"Spacecraft '{spacecraft}' is not in the dictionary.")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float.")
        return
    else:
        meters = au * 149597870700
        print(f"{spacecraft} is {meters:.2f} meters away from Earth.")
```

> **Best Practice:** While you could use a generic `except Exception:` to catch all errors, it is considered bad and lazy practice because it hides bugs you didn't expect. Always be as specific as possible with the exceptions you catch.

---

### Raising Exceptions (`raise`)
You don't just have to handle exceptions—you can also intentionally trigger them yourself using Python's `raise` keyword. This is incredibly useful when writing functions to alert other programmers (or yourself) when they supply invalid arguments or use your code incorrectly.

#### Choosing the Right Exception Type
- Use the most specific exception name possible.
- If a value has the correct data type (e.g., an integer) but is outside of your expected range (e.g., negative minutes or zero), the standard exception to raise is a **ValueError**.
- Avoid using the generic `Exception` class if a more specific one exists.

#### Adding Custom Error Messages
You can pass a descriptive string inside the parentheses of the exception to explain exactly what went wrong.

```python
def get_pace(miles, minutes):
    if minutes <= 0:
        # Raise a specific ValueError with a clear message
        raise ValueError("minutes must be greater than zero")
    return minutes / miles
```

#### Conventions for Error Messages
There are two primary schools of thought when writing exception messages:
1. **State the error directly:** Explain what is wrong with the value (e.g., `"invalid value for minutes"`).
2. **Instruct on what to change:** Explain what the parameter must be to succeed (e.g., `"minutes must be greater than zero"`).

---

## Debugging in Python

Debugging is the systematic process of finding and fixing mistakes (bugs) in your code. 

### Types of Bugs
1. **Syntax Errors**: Grammatical typos that prevent Python from running your code at all.
2. **Logical Bugs**: Code that runs successfully without throwing any errors or crashing, but produces incorrect, unintended, or buggy output.

```
Syntax Error ───> Code fails to run. Crash occurs immediately.
Logical Bug  ───> Code runs perfectly but produces the WRONG output.
```

---

### Tool 1: Print Debugging
The simplest and most immediate tool for debugging is inserting temporary `print()` statements. By printing out active values or loop counters, you can see exactly what the computer is seeing.

#### Drawbacks of Print Debugging:
- It gets very tedious to add and remove them.
- It makes your code messy.
- In complex programs, you can easily forget to clean them up, cluttering the final output.

---

### Tool 2: The Built-In Debugger
For complex logical errors, modern text editors (like VS Code) include a built-in **debugger**—a specialized program designed to let you pause and step through your code line by line.

```
       ┌────────────────────────────────────────────────────────┐
       │                  DEBUGGER CONTROLS                      │
       ├────────────────────────────────────────────────────────┤
       │ 🔴 Breakpoint   │ Pauses execution on a specific line  │
       │                 │ just BEFORE that line runs.           │
       ├─────────────────┼──────────────────────────────────────┤
       │ ➔ Continue      │ Resumes running the code until the   │
       │                 │ next breakpoint or the program ends. │
       ├─────────────────┼──────────────────────────────────────┤
       │ ↷ Step Over     │ Executes the current line and moves  │
       │                 │ to the next line of your script.     │
       ├─────────────────┼──────────────────────────────────────┤
       │ ⇣ Step Into     │ Steps INSIDE a custom function to    │
       │                 │ debug it line-by-line.               │
       ├─────────────────┼──────────────────────────────────────┤
       │ 💻 Local Vars   │ A panel that displays all variables  │
       │                 │ in the current scope and their values│
       └─────────────────┴──────────────────────────────────────┘
```

---

### Concrete Case Study: Mario's Brick Pyramid

Let's look at a logical bug and trace how to solve it using debugging.

#### The Goal
Print a textual representation of a Mario brick pyramid of height `3`, where row 1 has `1` hash, row 2 has `2` hashes, and row 3 has `3` hashes.

```
#
##
###
```

#### The Buggy Code
```python
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

main()
```

#### Running the Buggy Code (Height = 3)
```
(blank line)
#
##
```
This prints a pyramid of height 2 instead of 3, starting with a completely blank line!

#### Identifying the Bug:
1. **Using Print Debugging:** By temporarily printing `i` alongside the hashes:
   ```python
   # Inside the for loop:
   print(i, "#" * i)
   ```
   We would see:
   ```
   0 
   1 #
   2 ##
   ```
   *Lightbulb moment:* Python's `range(n)` starts iterating from `0`. Since `0` times any string is empty, the first row prints `0` hashes (a blank line).

2. **Using a Debugger:**
   - Place a **Breakpoint (🔴)** on the line calling `main()`.
   - Click **Step Into (⇣)** to go inside `main()`.
   - Click **Step Over (↷)** to execute the user input, typing `3`.
   - Click **Step Into (⇣)** to enter the `pyramid` function.
   - Look at the **Local Variables Panel** to see `n = 3`.
   - Step over the loop and watch `i` start at `0` and increment to `1` and `2`, showing why the math was off by one.

#### The Fix
Parenthize `i + 1` before performing string multiplication so that the loop multiplies the hash by `1`, `2`, and `3` instead of `0`, `1`, and `2`.

```python
def pyramid(n):
    for i in range(n):
        # Multiply by (i + 1) to account for 0-indexed loops
        print("#" * (i + 1))
```

#### Correct Output (Height = 3)
```
#
##
###
```

---

### Expanded Summary of Exceptions

| Exception | Core Cause | Typical Code Example |
| :--- | :--- | :--- |
| **SyntaxError** | Typos and grammatical mistakes in the written code. | `print("Hello` (missing closing quote) |
| **ValueError** | A function receives an argument with the correct type but an invalid value or range. | `int("cat")` (cannot convert letters) or raising for negative minutes in `get_pace` |
| **NameError** | Trying to use a variable name that hasn't been successfully defined. | Printing `x` when the assignment of `x` was interrupted by an error. |
| **KeyError** | Trying to access a dictionary key that does not exist. | `distances["James Web"]` where the key isn't in the dict |
| **MemoryError** | An operation overflows the available RAM. | Multiplying a string by a massive integer instead of a number, repeating it billions of times. |
