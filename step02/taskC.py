# Name: Michael McCarty
# Date: 2026-11-11
# Program: Paycheck Calculator
# Description: Calculates your paycheck with taxes.

# Output: prints the calculation results

federal_tax_rate = 0.10
state_tax_rate = 0.035
social_security_rate = 0.062
medicare_rate = 0.0145
weeks_per_year = 52


employee_name = input("Employee name: ")
hourly_rate = float(input("Hourly pay rate: "))
hours_worked = float(input("Hours worked this week: "))

gross_pay = hourly_rate * hours_worked
federal_tax = gross_pay * federal_tax_rate
state_tax = gross_pay * state_tax_rate
social_security = gross_pay * social_security_rate
medicare = gross_pay * medicare_rate

total_taken_out = federal_tax + state_tax + social_security + medicare
net_pay = gross_pay - total_taken_out
percent_kept = (net_pay / gross_pay) * 100

yearly_gross = gross_pay * weeks_per_year
yearly_net = net_pay * weeks_per_year


print("=" * 32)
print(f"PAY STUB: {employee_name}")
print("=" * 32)
print(f"Hours worked:\t{hours_worked:.1f}")
print(f"Hourly rate:\t${hourly_rate:.2f}")
print(f"Gross pay:\t${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%):\t${federal_tax:.2f}")
print(f"State tax (3.5%):\t${state_tax:.2f}")
print(f"Social Security:\t${social_security:.2f}")
print(f"Medicare:\t${medicare:.2f}")
print(f"Total taken out:\t${total_taken_out:.2f}")
print("-" * 32)
print(f"NET PAY:\t${net_pay:.2f}")
print("=" * 32)
print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross:\t${yearly_gross:.2f}")
print(f"Yearly net:\t${yearly_net:.2f}")
