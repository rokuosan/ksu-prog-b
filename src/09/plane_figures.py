from typing import Optional

TOLERANCE = 1e-10


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def distance(self, other: Optional["Point"] = None) -> float:
        if other is None:
            other = Point(0, 0)
        # √((x2-x1)^2 + (y2-y1)^2)
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def __str__(self):
        return f"({self._x}, {self._y})"


class Line:
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    def distance(self) -> float:
        return self._p1.distance(self._p2)

    def is_on(self, p: Point) -> bool:
        """p がこの線分上にあるかどうかを判定する"""
        # p1 から p までの距離 + p2 から p までの距離 と p1 から p2 までの距離が等しいか
        return (
            abs(self._p1.distance(p) + self._p2.distance(p) - self.distance())
            < TOLERANCE
        )

    def __str__(self):
        return f"({self._p1}, {self._p2})"
