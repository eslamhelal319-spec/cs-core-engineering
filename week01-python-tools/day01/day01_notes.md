# strip()
strip() fuction is used to remove all the white spaces in a string ,note that  "the ones removed are the ones at the beginning and end, but not between words".

```
"   eslam helal     "
 ^^^             ^^^
 removed         removed

       eslam  helal
             ^
       internal space stays
```

# capitalize()
capitalize() function is used to capitalize only the first word of a string .
capitalize() → first letter uppercase, everything else lowercase.

# title()
title() function is used to capitalize all words of a string.


| Method         | Example input   | Output          |
| -------------- | --------------- | --------------- |
| `capitalize()` | `"eslam helal"` | `"Eslam helal"` |
| `title()`      | `"eslam helal"` | `"Eslam Helal"` |
| `upper()`      | `"eslam helal"` | `"ESLAM HELAL"` |
| `lower()`      | `"ESLAM HELAL"` | `"eslam helal"` |


# split()
split() breaks a string into separate pieces based on something you specify.

for example split(" ") looks for the space " " and splits the string there:

```
"Eslam Helal"
       ↑
     split here
```

then you can assign the full name givin by input function into two diffrient variables after you had split it

# round()
round() function is used to round a number to a certain number of decimal places.
round(number) → rounds the number to the nearest whole number.
You can give round() a second argument:
for example round(3.14159, 2)
     Output: 3.14
  The 2 means: "Keep 2 digits after the decimal point."

print(f"{3.14159:.2f}") this has the same function as round(3.14159, 2)

note : round() uses "banker's rounding" for .5 cases — e.g. round(2.5) gives 2, not 3, because it rounds to the nearest even number.

# def function()
you define your own function using the def keyword.
The basic structure is:

```
def function_name():
   # code that the function should execute
```


# scope
scope means where a variable can be accessed or used.

```
def main():
    name = "Eslam"
    print(name)
main()
```

Here, name was created inside main().
That means name belongs to the scope of main().

But not here:

```
def main():
    name = "Eslam"
print(name)       # error
```

Why? Because name only exists inside the function.
think of it like this :

```
Outside the function
        |
        |   can't access "name"
        ↓
   ┌───────────────┐
   │   main()      │
   │               │
   │ name = Eslam  │ ← name exists here
   │               │
   └───────────────┘
```

What about variables outside functions?

```
name = "Eslam"
def main():
    print(name)
main()
```

This works because name was created outside the function, so it's a global variable.
the most important thing to remember is:
Variable created inside a function → local scope → normally only usable inside that function.
Variable created outside a function → global scope → can generally be accessed from functions.
