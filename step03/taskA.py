# Name: Michael McCarty
# Date: 2026/11/13
# Program: Movie Ticket Price Calculator
# Description: Calculates the price of a single movie ticket based on age,
#              day of the week, and 3D option.

CHILD_PRICE = 7.00
ADULT_PRICE = 11.00
SENIOR_PRICE = 8.00
TUESDAY_DISCOUNT = 3.00
THREE_D_CHARGE = 2.50

# Input
name = input("Name: ")
age = int(input("Age: "))
day = input("Day of the week: ")
is_3d = input("3D movie? (y/n): ")

# Output
if age < 0 or age > 120:
    print("Error: age must be 0 to 120.")
else:
    if age < 13:
        ticket_type = "Child"
        base_price = CHILD_PRICE
    elif age >= 65:
        ticket_type = "Senior"
        base_price = SENIOR_PRICE
    else:
        ticket_type = "Adult"
        base_price = ADULT_PRICE

    total = base_price

    is_tuesday = (day.lower() == "tuesday")
    if is_tuesday:
        total -= TUESDAY_DISCOUNT

    has_3d = (is_3d.lower() == "y")
    if has_3d:
        total += THREE_D_CHARGE

    print()
    print(f"--- Ticket for {name} ---")
    print(f"Ticket type:   {ticket_type}")
    print(f"Base price:    ${base_price:.2f}")
    
    if is_tuesday:
        print(f"Tuesday deal: -${TUESDAY_DISCOUNT:.2f}")
        
    if has_3d:
        print(f"3D charge:     ${THREE_D_CHARGE:.2f}")
        
    print(f"Total:         ${total:.2f}")
