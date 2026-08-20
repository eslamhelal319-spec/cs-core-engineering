#the problem:
#In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost.
#dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
#remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
#percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
#remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
#Assume that the user will input values in the expected formats.


#the solution :
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    removed_sign=d.replace("$","")
    float_dollars=float(removed_sign)
    return float_dollars


def percent_to_float(p):
    removed_sign=p.replace("%","")
    float_percent=float(int(removed_sign)/100)
    return float_percent


main()
