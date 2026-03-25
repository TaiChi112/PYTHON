from __future__ import annotations

import math


def distance1(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the Euclidean distance between points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance2(p1: list[float], p2: list[float]) -> float:
    """Return the Euclidean distance between two points represented by lists."""
    return distance1(p1[0], p1[1], p2[0], p2[1])


def distance3(c1: list[float], c2: list[float]) -> tuple[float, bool]:
    """Return center distance and overlap/touch status for two circles.

    Each circle is represented as [x, y, r].
    """
    center_distance = distance1(c1[0], c1[1], c2[0], c2[1])
    overlap = center_distance <= (c1[2] + c2[2])
    return center_distance, overlap


def perimeter(points: list[list[float]]) -> float:
    """Return perimeter of a polygon defined by ordered corner points."""
    total = 0.0
    for i in range(len(points)):
        current_point = points[i]
        next_point = points[(i + 1) % len(points)]
        total += distance2(current_point, next_point)
    return total


def main() -> None:
    print(distance1(0, 0, 3, 4))
    print(distance2([0, 0], [3, 4]))

    a, b = distance3([0, 0, 1], [5, 0, 2])
    print(a, b)

    print(perimeter([[0, 0], [0, 2], [2, 2], [2, 0]]))


if __name__ == "__main__":
    main()
