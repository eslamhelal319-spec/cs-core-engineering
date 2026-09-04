# The problem :
# Suppose that you’re in the habit of making a list of items you need from the grocery store.
# implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
# prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
# Treat the user’s input case-insensitively.

#The solution :

items={}
while True:
    try:
         item=input().lower()
         if item not in items:
              items[item]=1
         else:
              items[item]+=1
    except EOFError:
         break

for grocery_item in sorted(items):
     print(items[grocery_item],grocery_item.upper())

