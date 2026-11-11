# Name: Michael McCarty
# Date: 2026-11-11
# Program: Road Trip Calculator
# Description: Calculates cost, gas, and driving time for a road trip.

# Output: prints the calculation results

average_speed = 55

destination = input("Destination: ")
distance = float(input("Trip distance (miles): "))
mpg = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))

gallons = distance / mpg
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people

total_minutes = int(distance / average_speed * 60)
hours = total_minutes // 60
minutes = total_minutes % 60

round_trip_gas = gas_cost * 2

print()
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas: {gallons:.1f}")
print(f"Gas cost: ${gas_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
print(f"Driving time: {hours} hr {minutes} min (at {average_speed} mph)")
print(f"Round trip gas: ${round_trip_gas:.2f}")
