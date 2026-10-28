# AI Electricity Bill Forecaster
print("=" * 45)
print("     AI ELECTRICITY BILL FORECASTER")
print("=" * 45)

bills = []
units = []
print("\nEnter your last 6 months' electricity details:")
for i in range(1, 7):
    bills.append(float(input(f"Enter bill for month {i} (Rs.): ")))
    units.append(float(input(f"Enter units for month {i} (kWh): ")))

rate = float(input("\nEnter electricity rate per unit (Rs.): "))
n = len(bills)
x = list(range(1, n + 1))
mean_x = sum(x) / n
mean_y = sum(bills) / n
numerator = sum((x[i] - mean_x) * (bills[i] - mean_y) for i in range(n))
denominator = sum((value - mean_x) ** 2 for value in x)
slope = numerator / denominator
intercept = mean_y - slope * mean_x
predicted_bill = intercept + slope * (n + 1)

print("\n--- BILL PREDICTION ---")
print(f"Predicted next month's bill: Rs. {predicted_bill:.2f}")

appliances = {}
print("\n--- APPLIANCE DETAILS ---")
count = int(input("How many appliances do you want to analyze? "))
for i in range(count):
    name = input(f"\nEnter appliance {i + 1} name: ")
    power = float(input("Enter power in kW: "))
    hours = float(input("Enter daily usage hours: "))
    appliances[name] = {"power": power, "hours": hours}

def appliance_cost(power, hours, days=30):
    return power * hours * days * rate

print("\n--- APPLIANCE USAGE ANALYSIS ---")
for name, data in appliances.items():
    cost = appliance_cost(data["power"], data["hours"])
    print(f"{name}: Rs. {cost:.2f} per month")

print("\n--- SMART SAVINGS RECOMMENDATION ---")
ac_power = float(input("\nEnter AC power in kW: "))
ac_hours = float(input("Enter current daily AC usage hours: "))
reduce_hours = float(input("Reduce AC usage by how many hours daily? "))
if 0 <= reduce_hours <= ac_hours:
    old_cost = appliance_cost(ac_power, ac_hours)
    new_cost = appliance_cost(ac_power, ac_hours - reduce_hours)
    savings = old_cost - new_cost
    print("\nEstimated monthly savings: Rs.", round(savings, 2))
    print("Estimated yearly savings: Rs.", round(savings * 12, 2))
else:
    print("Invalid reduction hours!")

print("\nNote: These are estimates, not guarantees.")
print("Actual bills may include fixed charges and taxes.")
print("=" * 45)
