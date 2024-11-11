# 第5回 課題1: デフォルト引数を持つ Hello World
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題05-1-デフォルト引数を持つ-hello-world


def hello(text: str = None) -> str:
    if text is None:
        return "Hello World"
    elif text == "Python":
        return "Hi! Python"
    else:
        return f"Hello {text}".strip()


assert hello() == "Hello World", "Error: hello() が 'Hello World' を返しません．"
assert (
    hello("Python") == "Hi! Python"
), "Error: hello('Python') が 'Hi Python' を返しません．"
assert (
    hello("Tamada") == "Hello Tamada"
), "Error: hello('Tamada') が 'Hello Tamada' を返しません．"
