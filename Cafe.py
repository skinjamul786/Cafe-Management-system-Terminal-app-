# CAFE MANAGEMENT SYSTEM
# WITH ITEM-WISE BILL RECEIPT
# -------------------------------

# Menu dictionary
menu = {
    "pizza": 120,
    "pasta": 60,
    "burger": 60,
    "coffee": 40,
    "chicken lolipop": 55,
    "biriyani": 150,
    "salad": 70
}

# Dictionary to store ordered items
order_items = {}

print("=" * 40)
print("      Welcome to Tasty Cafe ☕")
print("=" * 40)

# Display menu
print("\n----------- MENU -----------")
for item, price in menu.items():
    print(f"{item.title():20} : ₹{price}")

# Order loop
while True:
    item = input("\nEnter item to order: ").lower()

    if item in menu:
        qty = int(input(f"Enter quantity for {item.title()}: "))

        if item in order_items:
            order_items[item] += qty
        else:
            order_items[item] = qty

        print(f"{item.title()} x {qty} added successfully ✅")

    else:
        print("Sorry! Item not available ❌")

    choice = input("Do you want to order another item? (Yes/No): ").lower()
    if choice != "yes":
        break

# -------------------------------
# BILL RECEIPT
# -------------------------------

print("\n" + "=" * 45)
print("           TASTY CAFE BILL")
print("=" * 45)
print(f"{'Item':15} {'Qty':5} {'Price':7} {'Total'}")
print("-" * 45)

grand_total = 0

for item, qty in order_items.items():
    price = menu[item]
    total = price * qty
    grand_total += total
    print(f"{item.title():15} {qty:<5} ₹{price:<6} ₹{total}")

print("-" * 45)
print(f"{'Grand Total':30} ₹{grand_total}")
print("=" * 45)
print("Thank you for visiting Tasty Cafe ❤️")
