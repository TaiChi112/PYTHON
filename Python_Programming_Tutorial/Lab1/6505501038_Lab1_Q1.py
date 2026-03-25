price = float(input("Enter the price: "))
shipping = float(input("Enter the shipping cost: "))
total_cost = price + shipping
print(f"Price: {price:.2f}")
print(f"Shipping: {shipping:.2f}")
print(f"Total: {total_cost:.2f} Bath ({shipping:.2f} Bath shipping fee)")
