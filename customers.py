# Reflection 1:
# I would use .get() when a key might not exist because it lets the
# program return a default value instead of crashing. I would use
# bracket notation when I know the key exists and need its value.

# Reflection 2:
# This pattern reminds me of using SUMIF in Excel because both
# organize and total information based on categories. Python can
# be more useful for large datasets because loops can process many
# records automatically without manually setting up formulas.
# Exercise 1: One customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# Exercise 2: Update and add

customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# Exercise 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys,
# not both the keys and their values.

for key in customer:
    print(key)
# Exercise 5: Lookup table

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

purchase = 200
final_price = purchase * (1 - discount)

print("Tier:", tier)
print("Discount rate:", discount)
print("Final price:", final_price)


# Exercise 6: List of dictionaries

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{person['name']}: {tier}, "
        f"Discount: ${discount_amount:.2f}"
    )


# Exercise 7: Nested catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# Exercise 8: Sales by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")
