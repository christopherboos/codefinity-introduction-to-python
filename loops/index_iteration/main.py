prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if index == 0:
        prices[index] = prices[index] * 0.9
    elif index == 1:
        prices[index] = prices[index] * 0.8
    elif index == 2:
        prices[index] = prices[index] * 0.85
    elif index == 3:
        prices[index] = prices[index] * 0.95
    print(f"Update price for item {index}: {prices[index]:.2f}")

