def add_item(cart_list: list, item_name: str, price: float) -> None:
    """Add an item dictionary to the cart list."""
    cart_list.append({"name": item_name, "price": price})


def remove_item(cart_list: list, item_name: str) -> None:
    """Remove the first matching item by name from the cart list."""
    for idx, item in enumerate(cart_list):
        if item.get("name") == item_name:
            cart_list.pop(idx)
            break


def calculate_total(cart_list: list) -> float:
    """Return the total price of all items in the cart."""
    return sum(item.get("price", 0) for item in cart_list)


def apply_discount(total_price: float, percent: float) -> float:
    """Return the discounted total price by percentage."""
    return total_price * (1 - percent / 100)
