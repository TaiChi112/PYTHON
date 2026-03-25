from __future__ import annotations

from ecommerce.cart import add_item, apply_discount, calculate_total, remove_item
from converter import kg_to_lbs
from text_utils import clean_text, count_vowels, count_words, highlight


def calculate_stats(*numbers: float) -> dict:
    """Calculate basic statistics from arbitrary numeric arguments.

    Args:
            *numbers: Any count of int or float values.

    Returns:
            dict: A dictionary containing keys 'sum', 'average', 'max', and 'min'.
                      If no number is provided, all values are 0.
    """
    if not numbers:
        return {"sum": 0, "average": 0, "max": 0, "min": 0}

    total = sum(numbers)
    return {
        "sum": total,
        "average": total / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }


def final_price(price: float, tax_rate: float = 0.07, **discounts: float) -> float:
    """Calculate final product price after coupon rules and tax.

    Args:
            price: Base item price.
            tax_rate: Tax rate, default is 0.07.
            **discounts: Coupon-name to discount-value mapping.

    Returns:
            float: Final price rounded to 2 decimal places.
    """
    total_discount = 0.0

    for coupon_name, value in discounts.items():
        if coupon_name.startswith("expired_"):
            continue
        if coupon_name.startswith("special_"):
            total_discount += value * 2
        else:
            total_discount += value

    net_price = max(0, price - total_discount)
    return round(net_price * (1 + tax_rate), 2)


def power_recursive(base: float, exponent: int) -> float:
    """Return base raised to exponent using recursion only.

    Args:
            base: The base value.
            exponent: Non-negative integer exponent.

    Returns:
            float: Result of base^exponent.
    """
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)


def demo_functions() -> None:
    print("=== Assignment 6 Functions ===")
    print(calculate_stats(10, 20, 30, 40, 50))
    print(calculate_stats(5, 5))
    print(calculate_stats())

    print(f"Case 1: {final_price(1000, discount_nov=100, expired_dec=500)}")
    print(f"Case 2: {final_price(2000, special_vip=200)}")
    print(f"Case 3: {final_price(3000, promo=100, special_year=200, expired_old=1000)}")
    print(f"Case 4: {final_price(500, special_clearance=300)}")
    print(f"Case 5: {final_price(2000, tax_rate=0, member=500)}")

    print(f"2^3 = {power_recursive(2, 3)}")
    print(f"5^0 = {power_recursive(5, 0)}")
    print(f"5^2 = {power_recursive(5, 2)}")


def demo_text_utils() -> None:
    print("\n=== Module: text_utils ===")
    raw_text = " Python is Amazing "
    cleaned = clean_text(raw_text)

    print(f"Raw text: '{raw_text}'")
    print(f"1. Cleaned: '{cleaned}'")
    print(f"2. Word count: {count_words(cleaned)}")
    print(f"3. Vowel count: {count_vowels(cleaned)}")
    print(f"4. Highlighted: {highlight(cleaned)}")


def demo_ecommerce() -> None:
    print("\n=== Package: ecommerce ===")
    my_cart: list[dict] = []

    print("--- เริ่มการช้อปปิ้ง ---")
    add_item(my_cart, "Mouse", 500)
    print("เพิ่ม Mouse ราคา 500 บาท")
    add_item(my_cart, "Keyboard", 1500)
    print("เพิ่ม Keyboard ราคา 1500 บาท")
    add_item(my_cart, "Monitor", 4000)
    print("เพิ่ม Monitor ราคา 4000 บาท")

    print("--- เปลี่ยนใจ ---")
    remove_item(my_cart, "Mouse")
    print("ลบ Mouse ออกแล้ว")

    total = calculate_total(my_cart)
    total_after_discount = apply_discount(total, 10)

    print("--- สรุปยอด ---")
    print(f"ราคารวม: {total} บาท")
    print(f"ราคาหลังหักส่วนลด 10%: {total_after_discount} บาท")


def demo_converter() -> None:
    print("\n=== Module: converter ===")
    weight_kg = 70
    weight_lbs = kg_to_lbs(weight_kg)
    print(f"น้ำหนักผม {weight_kg} กิโลกรัม เท่ากับ {weight_lbs:.2f} ปอนด์")


def main() -> None:
    demo_functions()
    demo_text_utils()
    demo_ecommerce()
    demo_converter()


if __name__ == "__main__":
    main()
