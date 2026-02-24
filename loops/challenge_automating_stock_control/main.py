# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item in inventory:
    print("Processing", item)
    current_stock, minimum_stock, restock_qty, sale_status = inventory[item]
    while current_stock < minimum_stock:
        current_stock = current_stock + restock_qty
        inventory[item] = [current_stock, minimum_stock, restock_qty, sale_status]
    if current_stock > discount_threshold:
        sale_status = True
    inventory[item] = [current_stock, minimum_stock, restock_qty, sale_status]
print("Processing completed")



