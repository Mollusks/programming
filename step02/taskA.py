# Name: Michael McCarty
# Date: 2026-11-11
# Program: Pizza Party Planner 
# Description: helps plan a pizza party.

# Output: prints the plan

slices_per_pizza = 8
pizza_price = 12.99
slices_price = 2.25

name = input("Host name: ")
people_ask = input("Number of people: ")
people = float(people_ask)

slices_ask = input("Slices needed: ")
slices = float(slices_ask)

total_slices = people * slices
whole_pizza = slices // slices_per_pizza
pizza_slices = slices % slices_per_pizza

total_cost = (whole_pizza * pizza_price) + (pizza_slices * slices_price)
person_cost = total_cost / people

print()
print(f"=== Pizza Plan for {name}'s Party ===")
print(f"Slices needed: {slices}")
print(f"Whole pizzas: {whole_pizza}")
print(f"Extra slices: {pizza_slices}")
print(f"Total cost: ${total_cost:.2}")
print(f"Cost per person: ${person_cost:.2}")
