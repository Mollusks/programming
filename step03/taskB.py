# Name: Michael McCarty
# Date: 2026/11/13
# Program: Shipping Calculator
# Description: Calculates shipping cost, grand total, and delivery time

ZONE1_RATE = 0.50
ZONE2_RATE = 0.75
ZONE3_RATE = 1.25
MINIMUM_SHIPPING = 4.00
FREE_SHIPPING_AMOUNT = 50.00
RUSH_FEE = 10.00

# Input
order_total = float(input("Order total: "))
weight = float(input("Package weight (lbs): "))
zone = int(input("Shipping zone (1-3): "))
rush = input("Rush delivery? (y/n): ")

# Output
if order_total <= 0 or weight <= 0:
    print("Error: order total and weight must be more than 0.")
elif zone not in (1, 2, 3):
    print("Error: zone must be 1, 2, or 3.")
else:
    is_rush = (rush.lower() == "y")

    if zone == 1:
        rate = ZONE1_RATE
        days = 2
    elif zone == 2:
        rate = ZONE2_RATE
        days = 4
    else:
        rate = ZONE3_RATE
        days = 6

    shipping = weight * rate

    if shipping < MINIMUM_SHIPPING:
        shipping = MINIMUM_SHIPPING
    if order_total >= FREE_SHIPPING_AMOUNT and not is_rush:
        shipping = 0.00

    if is_rush:
        shipping += RUSH_FEE
        if zone == 1 or zone == 2:
            days = 1
        else:
            days = 2

    is_heavy = (weight > 50)
    if is_heavy:
        days += 2

    grand_total = order_total + shipping

    print()
    print("--- Shipping Summary ---")
    print(f"Order total:  ${order_total:.2f}")

    if shipping == 0:
        print("Shipping:     FREE")
    else:
        print(f"Shipping:     ${shipping:.2f}")

    print(f"Grand total:  ${grand_total:.2f}")

    day_label = "day" if days == 1 else "days"
    print(f"Arrives in:   {days} {day_label}")

    if is_heavy:
        print("Note: heavy package, 2 extra days added.")
