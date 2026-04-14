# In python is not use switch case statement. It is use match case statement.

# Example 1
day=3
match day:
    case 1 : print("Sunday")
    case 2 : print("Monday")
    case 3 : print("Tuesday")
    case 4 : print("Wednesday")
    case 5 : print("Thursday")
    case 6 : print("Friday")
    case 7 : print("Saturday")
    case _ : print("Invalid week day,Please try again") # Underscore is default case


# Example 2 - Combine value
days = 4
match days:
    case 2|3|4|5|6 : print("weekday")
    case 1|7 : print("Weekend")
    case _ : print("Invalid week day")