class RingBuffer:
    def __init__(self, n: int = 12):
        self.counter = 0
        self.data = [None] * n

    def get(self, i: int):
        return self.data[i % len(self.data)]

    def len(self):
        return len([x for x in self.data if x is not None])

    def add(self, element):
        self.data[self.counter % len(self.data)] = element
        self.counter = (self.counter + 1) % len(self.data)

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
