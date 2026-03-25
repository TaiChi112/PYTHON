def cm_to_inch(cm: float) -> float:
    """Convert centimeters to inches."""
    return cm / 2.54


def inch_to_cm(inch: float) -> float:
    """Convert inches to centimeters."""
    return inch * 2.54


def kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462


def lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms."""
    return lbs / 2.20462


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15


if __name__ == "__main__":
    print("=== TEST MODE Checking Formulas ===")
    print(f"2.54 cm to Inch: {cm_to_inch(2.54):.1f}")
    print(f"1 Inch to cm: {inch_to_cm(1):.2f}")
    print(f"10 kg to lbs: {kg_to_lbs(10):.2f}")
    print(f"10 lbs to kg: {lbs_to_kg(10):.2f}")
    print(f"0 C to Kelvin: {celsius_to_kelvin(0):.2f}")
    print("=== End of Tests ===")
