grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                     "Eggs": ("Dairy", 5.50, 30),
                     "Bread": ("Bakery", 2.99, 15),
                     "Apples": ("Produce", 1.50, 50)}

category, price, stock = grocery_inventory["Eggs"]
if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price = price - 1
    grocery_inventory["Eggs"] = (category, price, stock)
else:
    print("The price of Eggs is reasonable")

print(f"eggs_price: {price}")
print(f"eggs_price: {grocery_inventory["Eggs"]}")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

category, price, stock = grocery_inventory["Milk"]
if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    stock = stock + 20
    grocery_inventory.update({"Milk": (category, price, stock)})
else:
    print ("Milk has sufficient stock.")

category, price, stock = grocery_inventory["Apples"]
if price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")



