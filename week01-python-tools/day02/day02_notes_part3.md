### Lists: Advanced Methods

### append()
The `append()` method adds a single new element directly to the end of an existing list.
```python
results = ["Mario", "Luigi"]
results.append("Princess")
print(results)  # Output: ['Mario', 'Luigi', 'Princess']
```

### extend()
If you try to use `append()` to add multiple items inside a list (e.g., `results.append(["Bowser", "Donkey Kong"])`), Python will append the entire list as a single nested element. 
To add elements from another list individually to the end of your original list, use `extend()` instead.
```python
results = ["Mario", "Luigi"]
results.extend(["Bowser", "Donkey Kong"])
print(results)  # Output: ['Mario', 'Luigi', 'Bowser', 'Donkey Kong']
```

### remove()
The `remove()` method searches your list for the first instance of a specific value and deletes it.
```python
results = ["Mario", "Luigi", "Bowser", "Toad"]
results.remove("Bowser")
print(results)  # Output: ['Mario', 'Luigi', 'Toad']
```

### insert()
While `append()` only adds elements to the end, `insert()` lets you inject an element at any specific position (index) in the list. It takes two arguments: the index where you want to put the element, and the element itself.
```python
results = ["Mario", "Luigi", "Princess"]
# Sneak Bowser into first place (index 0)
results.insert(0, "Bowser")
print(results)  # Output: ['Bowser', 'Mario', 'Luigi', 'Princess']
```

### reverse()
The `reverse()` method flips the order of the list in place, turning the last element into the first, and the first into the last.
```python
results = ["Mario", "Luigi", "Princess"]
results.reverse()
print(results)  # Output: ['Princess', 'Luigi', 'Mario']
```

---

### Dictionaries: Safe Lookup, Updates, and Iteration

The Dictionaries Short highlights critical techniques for working safely with key-value data, updating multiple values at once, and using dedicated iteration methods.

### KeyErrors in Python
If you try to access a key inside a dictionary that does not exist using standard bracket notation (`dictionary["missing_key"]`), Python will crash and raise a **`KeyError`**.
```python
spacecraft = {"name": "James Webb"}
print(spacecraft["distance"])  # Raises KeyError: 'distance'
```

### get()
To prevent your program from crashing when looking up a key that might be missing, use the `.get()` method. It attempts to retrieve the key, but if the key doesn't exist, it safely returns a default value (like `None` or an "unknown" string) instead of raising an error.
```python
spacecraft = {"name": "James Webb"}
# Safely look up distance, default to "unknown" if missing
distance = spacecraft.get("distance", "unknown")
print(distance)  # Output: unknown
```

### Adding and Modifying Keys On-the-Fly
You do not have to define all keys when you first create a dictionary. You can easily add a new key-value pair or update an existing one using bracket notation:
```python
spacecraft = {"name": "James Webb"}
spacecraft["distance"] = 0.01  # Adds the 'distance' key with value 0.01
```

### update()
If you want to add or update multiple key-value pairs at the exact same time, you can use the `.update()` method and pass in a new dictionary containing the keys and values you want to add.
```python
spacecraft = {"name": "James Webb"}
spacecraft.update({"distance": 0.01, "orbit": "Sun"})
print(spacecraft)  # Output: {'name': 'James Webb', 'distance': 0.01, 'orbit': 'Sun'}
```

### .keys()
To explicitly loop over all the keys in a dictionary, you can call the `.keys()` method.
```python
distances = {"Voyager 1": 163, "Voyager 2": 136}
for name in distances.keys():
    print(name)
```
Output:
```
Voyager 1
Voyager 2
```

### .values()
If you only care about the values inside the dictionary and do not need the keys, you can use the `.values()` method to loop over them directly.
```python
distances = {"Voyager 1": 163, "Voyager 2": 136}
for distance in distances.values():
    print(distance)
```
Output:
```
163
136
```

---

### Summary Table of New Methods

| Data Structure | Method / Operation | Syntax Example | What it does |
| --- | --- | --- | --- |
| **List** | `append` | `list.append("item")` | Adds a single item to the very end of the list. |
| **List** | `extend` | `list.extend(["item1", "item2"])` | Unpacks a list and adds each element individually to the end. |
| **List** | `remove` | `list.remove("item")` | Deletes the first occurrence of the specified item. |
| **List** | `insert` | `list.insert(0, "item")` | Injects an item at the specified index, shifting other items down. |
| **List** | `reverse` | `list.reverse()` | Reverses the order of the items in place. |
| **Dictionary** | `get` | `dict.get("key", "default")` | Safely retrieves a key's value, returning a default if the key is missing. |
| **Dictionary** | `update` | `dict.update({"k1": "v1", "k2": "v2"})` | Adds or updates multiple key-value pairs at once. |
| **Dictionary** | `keys` | `dict.keys()` | Returns a collection of all keys in the dictionary. |
| **Dictionary** | `values` | `dict.values()` | Returns a collection of all values in the dictionary. |




### List & Dictionary Comprehensions

Comprehensions are a quick, expressive way in Python to construct a new list or dictionary from existing data in a single line of code.

### list comprehensions
A list comprehension allows you to transform or filter elements from an existing list and compile them into a new list. 
The syntax uses **square brackets `[]`** enclosing a custom loop structure:
```python
# Unaltered copy of a list
copy_of_words = [word for word in words]

# Transform elements (converting to lowercase)
lowercase_words = [word.lower() for word in words]
```

### filtering list comprehensions
You can append an `if` statement to the end of a list comprehension to filter which items are included in the new list:
```python
# Only include words longer than 4 letters
interesting_words = [word.lower() for word in words if len(word) > 4]
```

### dictionary comprehensions
Similar to list comprehensions, dictionary comprehensions let you dynamically build a dictionary from an iterable.
The syntax uses **curly braces `{}`** and pairs keys to values using a colon `:`:
```python
# Build a dictionary counting word occurrences
counts = {word: lowercase_words.count(word) for word in lowercase_words}
```
note: Using list and dictionary comprehensions allows you to significantly condense your code. A program that would typically take 15 to 20 lines using traditional loops can be written in as few as 4 clean, highly readable lines.

---

### Advanced List Methods

While basic lists can be indexed and iterated over, lists support dedicated methods to mutate their content in place.

### pop()
The `pop()` method removes the very last item from a list and returns it. This is highly useful when you need to know which item was removed (such as tracking actions that can be undone).
```python
history = ["up", "down", "left", "right"]

# Remove and retrieve the last action
undone = history.pop() 
print(undone)   # Output: right
print(history)  # Output: ['up', 'down', 'left']
```

### clear()
The `clear()` method removes every single item from the list in place, resetting it back to an empty list `[]` without having to reinitialize or re-declare the variable.
```python
history = ["up", "down", "left"]
history.clear()
print(history)  # Output: []
```

---

### String Slicing

String slicing is a feature in Python that allows you to extract smaller substrings from a larger string by specifying indices inside square brackets `[]`.

### basic slicing
Slicing uses the syntax `string[start:end]`. 
* The **start index is inclusive** (the character at this index is included).
* The **end index is exclusive** (Python goes up to, but does not include, the character at this index).
```python
phone = "617-555-1000"

# Extract the area code (indices 0, 1, and 2)
area_code = phone[0:3] 
print(area_code)  # Output: 617
```

### slicing shortcuts
* **Omitting the start index (`[:end]`)**: Tells Python to start slicing from the very beginning of the string.
  ```python
  area_code = phone[:3] # Output: 617
  ```
* **Omitting the end index (`[start:]`)**: Tells Python to slice from the start index all the way to the end of the string.
  ```python
  last_four = phone[8:] # Output: 1000
  ```

### negative indexing
Instead of counting indices from left to right starting at `0`, Python allows you to count backwards from the end of a string using negative numbers.
* The last character is at index `-1`.
* The second to last character is at index `-2`, and so on.

Using negative indexing is extremely robust because it continues to work even if characters are added to the beginning of the string.
```python
# Grab the last four characters, regardless of string length
last_four = phone[-4:]
print(last_four)  # Output: 1000
```

---

### Tuples

A tuple is a Python data structure used to group multiple distinct values into a single package. While they behave very similarly to lists, they have some critical differences in design and performance.

### creating and indexing tuples
To create a tuple, place your comma-separated values inside **parentheses `()`**:
```python
# Group latitude and longitude together
coordinates = (42.376, -71.115)

# Access items using bracket notation
latitude = coordinates[0]
print(latitude)  # Output: 42.376
```

### tuple unpacking
Unpacking allows you to take the individual components of a tuple and assign them to distinct variables in a single step:
```python
latitude, longitude = coordinates
print(latitude)   # Output: 42.376
print(longitude)  # Output: -71.115
```

### immutability
The most important rule of tuples is that they are **immutable**. Once a tuple is created, you cannot change, add, or assign any values inside of it. Attempting to do so will raise an assignment error.
```python
coordinates = (42.376, -71.115)
coordinates[0] = 42.0  # Raises a TypeError
```

### memory efficiency
Because tuples cannot be modified, Python can represent them much more efficiently in memory than mutable lists. 

You can measure the size of any object in bytes by importing the `sys` module and using the `sys.getsizeof()` function:
```python
import sys

coordinate_tuple = (42.376, -71.115)
coordinate_list = [42.376, -71.115]

print(sys.getsizeof(coordinate_tuple))  # Output: 56 bytes
print(sys.getsizeof(coordinate_list))   # Output: 72 bytes
```
note: While a difference of 16 bytes is small, utilizing tuples over lists can lead to significant memory savings when processing datasets with millions of rows of coordinates or records.

---

### Summary Table of New Features and Methods

| Data Structure / Concept | Syntax Example | When to use | Key Feature |
| --- | --- | --- | --- |
| **List Comprehension** | `[x.lower() for x in list]` | When you want to transform elements from an existing list into a new one | Single line, compact |
| **Filtered List Comprehension** | `[x.lower() for x in list if len(x) > 4]` | When you want to select and transform specific elements | Inline filtering with `if` |
| **Dictionary Comprehension** | `{k: list.count(k) for k in list}` | When you want to construct a dictionary dynamically in one step | Key-value pairs inside `{}` |
| **pop()** | `item = list.pop()` | To remove and return the last item from a list | Useful for reversing or undoing operations |
| **clear()** | `list.clear()` | To wipe out all items in a list in place | Resets list to `[]` without re-allocation |
| **String Slicing** | `string[start:end]` | To extract a portion of a string as a substring | Left index inclusive, right index exclusive |
| **Negative Slicing** | `string[-4:]` | To extract a trailing substring regardless of string length | Counts backwards from the end |
| **Tuple** | `(item1, item2)` | When grouping coordinates or values that must never change | Immutable and highly memory-efficient |



