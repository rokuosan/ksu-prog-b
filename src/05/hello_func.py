# 第5回 課題1: デフォルト引数を持つ Hello World
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題05-1-デフォルト引数を持つ-hello-world

# ここに hello 関数を定義してください．
def hello(text: str = None) -> str:
    if text is None:
        return "Hello World"
    elif text == "World":
        return "Hi! World"
    else:
        return f"Hello {text}".strip()

# 以下のテストコードは変更しないでください．
assert hello() == "Hello World",          "Error: hello() が 'Hello World' を返しません．"
assert hello("Python") == "Hello Python", "Error: hello('Python') が 'Hello Python' を返しません．"
assert hello("World") == "Hi! World",     "Error: hello('World') が 'Hi! World' を返しません．"
