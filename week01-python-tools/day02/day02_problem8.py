# The problem :
# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for
# a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# The solution :

vowels=["a","e","i","u","o"]
origin=input("Input: ")
omitted=''
for letter in origin:
    if letter.lower() in vowels:
        continue
    omitted+=letter
print(f"Output: {omitted}")