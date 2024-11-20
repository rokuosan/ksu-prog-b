class RingBuffer:
    """リングバッファを表すクラス

    リングバッファは固定長の配列で、要素を追加するとラウンドロビン式に古い要素を上書きする。

    容量が3のリングバッファに、1,2,3の順でデータを入れたとする。
    その後に、4を追加すると、1が上書きされて、4,2,3のデータが格納される。
    続いて、5を追加すると、2が上書きされて、4,5,3のデータが格納される。

    Methods:
        add: 要素を追加する
        get: 指定したインデックスの要素を取得する
        len: リングバッファの要素数を取得する

    Attributes:
        data: リングバッファのデータを格納するリスト
    """

    def __init__(self, n: int = 12):
        self.capacity = n
        self.data = [None] * self.capacity

    def get(self, i: int):
        """指定したインデックスの要素を取得する

        Args:
            i: 取得する要素のインデックス

        Returns:
            指定したインデックスの要素
        """
        if i < 0 or i >= self.capacity:
            return None
        return self.data[i]

    def len(self):
        """リングバッファの要素数を取得する

        Returns:
            リングバッファの要素数
        """
        return len([x for x in self.data if x is not None])

    def add(self, element):
        """要素を追加する

        Args:
            element: 追加する要素
        """
        index = self.len() % self.capacity
        self.data[index] = element


rb1 = RingBuffer(3)
assert rb1.get(0) == None, "何も要素が入っていないため，None であるはずです"
rb1.add(1)
assert rb1.get(0) == 1, "0番目の要素は 1 であるはずです"
rb1.add(2)
rb1.add(3)
rb1.add(4)  # 最初の要素である 1 が上書きされる．
assert rb1.get(0) == 4, "0番目の要素は 4 であるはずです"
assert rb1.get(1) == 2, "0番目の要素は 2 であるはずです"
assert rb1.get(2) == 3, "0番目の要素は 3 であるはずです"
assert rb1.len() == 3, "3つの要素が入っているため，長さは3であるはずです"

rb2 = RingBuffer()
assert rb2.get(0) == None, "何も要素が入っていないため，None であるはずです"
rb2.add("item1")
rb2.add("item2")
assert rb2.len() == 2, "2つの要素が入っているため，長さは2であるはずです"
assert rb2.get(5) == None, "5番目の要素は存在しないため，None であるはずです"
