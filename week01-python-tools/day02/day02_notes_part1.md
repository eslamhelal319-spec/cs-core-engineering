### Comparison Operators
Python comes with built-in syntax to compare values mathematically and logically:

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `>` | Greater than | `x > y`  |
| `>=` | Greater than or equal to | `x >= y` |
| `<` | Less than | `x < y` |
| `<=` | Less than or equal to | `x <= y`  |
| `==` | Equal to (checks equality) | `x == y`  |
| `!=` | Not equal to | `x != y`  |

> **Note:** A single equal sign (`=`) represents **assignment** (copying the value from right to left), whereas a double equal sign (`==`) represents **equality comparison**.

---

### The `if` Statement
An `if` statement asks a question using a **boolean expression**—a question that evaluates to either `True` or `False` . 

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```


*   **Colon (`:`):** Every conditional statement line must end with a colon .
*   **Indentation:** Python does **not** use curly braces to group blocks of code; it strictly relies on indentation (usually 4 spaces or 1 tab) [5, 24]. If indentation is omitted, your program will not work .

---

### Design Optimization: `if`, `elif`, and `else`

#### 1. The Repetitive Approach (Independent `if`s)
```python
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```
*   **Drawback:** The computer is forced to ask all three questions sequentially, even if the first condition was already found to be `True` [10]. This is repetitive and inefficient .

#### 2. The Mutually Exclusive Approach (`elif`)
By using `elif` (else if), we make the conditions mutually exclusive. Once Python finds a condition that evaluates to `True`, it executes that block and stops asking further questions :
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```


#### 3. The Catch-All Approach (`else`)
If we already know that `x` is neither less than `y` nor greater than `y`, it mathematically *must* be equal to `y` . We don't need to ask a third question; we can use `else` :
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```


---

### Logical Operators

#### `or`
Used to check if at least one of multiple questions evaluates to `True`:
```python
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```


#### `and`
Used to check if multiple questions are all simultaneously `True` :
```python
if score >= 90 and score <= 100:
    print("Grade: A")
```


---

### Chaining Comparison Operators
In Python, you can chain comparisons together just like in mathematics, which is much cleaner than using `and` :

```python
# Instead of: score >= 90 and score <= 100
if 90 <= score <= 100:
    print("Grade: A")
```
[29, 30]

---

### Modulo Operator `%` and Parity
The modulo operator (`%`) calculates the remainder when dividing one number by another . 
*   `4 % 3` yields `1` (3 goes into 4 once, with 1 left over).
*   `5 % 3` yields `2` .
*   `6 % 3` yields `0` (divides cleanly) .

#### Checking for Even or Odd (Parity)
An even number divides cleanly by 2 with a remainder of 0 . We can check this programmatically :
```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```


---

### Boolean Values (`bool`)
A `bool` is a Python data type that can only hold one of two values: `True` or `False` (both must be capitalized) .

We can write custom functions that return boolean values :
```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
```


---

### Pythonic Code: Shortening Logic
"Pythonic" refers to writing code in the elegant, concise style favored by the Python community . We can optimize our `is_even` function in two ways:

#### 1. Inline Conditional Expression (Ternary Operator)
You can collapse an entire `if-else` return block into a single readable line that reads almost like english :
```python
def is_even(n):
    return True if n % 2 == 0 else False
```


#### 2. Direct Boolean Return
Since the expression `n % 2 == 0` itself evaluates to `True` or `False`, we can just return that result directly without using `if` or `else` at all :
```python
def is_even(n):
    return n % 2 == 0
```


---

### The `match` Statement
The `match` statement (similar to `switch` in other languages) matches a value against several potential patterns . It is highly readable and avoids long chains of `elif` statements .

```python
name = input("What's your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")
```


#### Key features of `match`:
*   **Or operator (`|`):** Allows you to group multiple patterns together into a single case block (e.g., `"harry" | "hermione" | "ron"`) 
*   **The Wildcard (`_`):** A single underscore serves as the catch-all case (similar to `else`) for any values not explicitly handled .
*   **No Break Required:** Unlike languages like Java or C, Python's `match` statement does not require a `break` keyword to stop execution from falling through to the next case .
