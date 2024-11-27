class MyRandom:
    def __init__(
        self, seed=0, modulus=2**32, multiplier=1664525, increment=1013904223
    ):  # 引数（seed，modulus, multiplier, increment）を追加してください．
        # seed, modulus, multiplier, increment はデフォルト引数を持つようにしてください．
        self.seed = seed
        self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment

    def next(self, count=0):  # count が指定された場合，count 回乱数を生成します．
        result = self._next_impl()
        if count > 0:
            return self.next(count - 1)
        return result

    def _next_impl(self):
        # 線形合同法による乱数生成
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        return self.seed / self.modulus
