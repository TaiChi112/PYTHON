from __future__ import annotations

import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_input_file(filename: str) -> Path:
    candidate = Path(filename.strip())
    candidates: list[Path] = []

    if candidate.is_absolute():
        candidates.append(candidate)
    else:
        candidates.append(BASE_DIR / candidate)

    # Support input without extension, e.g. "move1" -> "move1.txt".
    if candidate.suffix == "":
        no_ext = Path(f"{candidate}.txt")
        candidates.append(no_ext if no_ext.is_absolute() else BASE_DIR / no_ext)

    # Support both problem<n>.txt and problems<n>.txt naming patterns.
    name = candidate.name
    if "problems" in name:
        alt_name = name.replace("problems", "problem")
        alt_path = candidate.with_name(alt_name)
        candidates.append(alt_path if alt_path.is_absolute() else BASE_DIR / alt_path)
    elif "problem" in name:
        alt_name = name.replace("problem", "problems")
        alt_path = candidate.with_name(alt_name)
        candidates.append(alt_path if alt_path.is_absolute() else BASE_DIR / alt_path)

    for path in candidates:
        if path.exists():
            return path

    # Fall back to the first candidate so caller can handle FileNotFoundError.
    return candidates[0]


def run_robot_movement() -> None:
    movefile = input("Choose your movefile: ").strip()
    position_input = input("Initial position : ").strip()

    try:
        x_str, y_str = position_input.split(",")
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        print("Invalid initial position")
        return

    path = resolve_input_file(movefile)
    try:
        commands = [
            line.strip().upper()
            for line in path.read_text().splitlines()
            if line.strip()
        ]
    except FileNotFoundError:
        print("File not found")
        return

    moves = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }

    for cmd in commands:
        if cmd not in moves:
            print("Invalid command")
            return

        dx, dy = moves[cmd]
        x += dx
        y += dy

    print(f"Robot stops at {x},{y}")


def is_equal(v1: list[float], v2: list[float]) -> bool:
    return len(v1) == len(v2)


def dot(v1: list[float], v2: list[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))


def convert_to_float(v: list[str]) -> list[float]:
    return [float(item) for item in v]


def read_file_vector(filename: str) -> tuple[list[float], list[float]]:
    path = resolve_input_file(filename)
    lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError("Vector file must contain at least 2 lines")

    v1 = convert_to_float(lines[0].split())
    v2 = convert_to_float(lines[1].split())
    return v1, v2


def run_vector_dot_product() -> None:
    filename = input("Choose your vector file: ").strip()

    try:
        v1, v2 = read_file_vector(filename)
    except FileNotFoundError:
        print("File not found")
        return
    except ValueError:
        print("Invalid vector file")
        return

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    if not is_equal(v1, v2):
        print("Incompatible size")
        return

    print(f"v1*v2 = {dot(v1, v2)}")


def quad1(a: float, b: float, c: float) -> float:
    discriminant = b**2 - 4 * a * c
    return (-b + math.sqrt(discriminant)) / (2 * a)


def quad2(a: float, b: float, c: float) -> float:
    discriminant = b**2 - 4 * a * c
    return (-b - math.sqrt(discriminant)) / (2 * a)


def run_quadratic_problems() -> None:
    filename = input("Choose your problem file: ").strip()
    path = resolve_input_file(filename)

    try:
        lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    except FileNotFoundError:
        print("File not found")
        return

    for line in lines:
        try:
            a_str, b_str, c_str = line.split()
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
        except ValueError:
            print("Invalid problem")
            continue

        discriminant = b**2 - 4 * a * c
        if a == 0 or discriminant < 0:
            print("Invalid problem")
            continue

        x1 = quad1(a, b, c)
        x2 = quad2(a, b, c)
        print(x1, x2)


def main() -> None:
    run_robot_movement()
    run_vector_dot_product()
    run_quadratic_problems()


if __name__ == "__main__":
    main()
