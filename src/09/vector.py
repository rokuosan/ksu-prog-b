from typing import Optional


class Vector:
    def __init__(self, *args):
        self._data = list(args)

    def __add__(self, other: "Vector") -> Optional["Vector"]:
        # ベクトルの和を求める（配列の各要素を足し合わせる）
        if len(self) != len(other):
            return None
        return Vector(*[x + y for x, y in zip(self._data, other._data)])

    def __mul__(self, other: int) -> int | None:
        # ベクトルの内積を求める（配列の各要素を掛け合わせたものを足し合わせる）
        if len(self) != len(other):
            return None
        return sum([x * y for x, y in zip(self._data, other._data)])

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data).replace("[", "(").replace("]", ")")

    def norm(self):
        # ベクトルのノルムを計算する
        return sum([x ** 2 for x in self._data]) ** 0.5
