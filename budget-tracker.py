import csv

total = 0
category_totals = {}

with open("budget.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = int(row["amount"])
        total += amount

        category = row["category"]
        category_totals[category] = category_totals.get(category, 0) + amount

print("TOTAL SPENDING:", total)
print("\nBY CATEGORY:")
for cat, amt in category_totals.items():
    print(cat, ":", amt)
