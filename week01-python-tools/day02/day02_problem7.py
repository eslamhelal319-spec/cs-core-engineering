# The problem :
# uppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these 
# denominations: 25 cents, 10 cents, and 5 cents.

# implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, 
# and ignore any integer that isn’t an accepted denomination.


# The solution :

amount_due=50
total=0
allowed=[25,10,5]
while amount_due>0:
    print(f"Amount Due: {amount_due}")
    insert=int(input("Insert Coin: "))
    if insert not in allowed :
        continue
    amount_due-=insert
    total+=insert
   
change_owed=total-50
print(f"Change Owed: {change_owed}")