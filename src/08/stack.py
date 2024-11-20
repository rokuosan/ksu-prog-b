class Stack:
    """Stack はスタックを表すクラス"""

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def push(self, element):
        """push はスタックに要素を追加します

        Args:
            element: 追加する要素
        """
        self.data.append(element)

    def pop(self):
        """pop はスタックから要素を取り出します"""
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        """peek はスタックの最後の要素を返します"""
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def len(self):
        """len はスタックの要素数を返します"""
        return len(self.data)


s1 = Stack()
s1.push("This")
s1.push("is")
s1.push("stack")
s1.push("test")

assert s1.len() == 4, "スタックの長さは4になっているはずです"
assert s1.peek() == "test", "peek() は最後の要素である test を返すべきです"
assert s1.len() == 4, "peek() は要素の長さを変更しません"

assert s1.pop() == "test", "pop() は最後の要素である test を返すべきです"
assert s1.pop() == "stack", "pop() は最後の要素である stack を返すべきです"
assert s1.pop() == "is", "pop() は最後の要素である is を返すべきです"
assert s1.pop() == "This", "pop() は最後の要素である This を返すべきです"
assert s1.len() == 0, "スタックの長さは0になっているはずです"

s2 = Stack([1, 2, 3, 4, 5])  # コンストラクタで要素を指定できる．
assert s2.len() == 5, "スタックの長さは5になっているはずです"
s2.pop()
s2.pop()
s2.pop()
s2.pop()
s2.pop()
assert s2.len() == 0, "スタックの長さは0になっているはずです"

s3 = Stack()
assert s3.pop() == None, "空のスタックから pop() すると None が返るべきです"
