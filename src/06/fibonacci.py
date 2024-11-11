# 第6回 課題1: フィボナッチ数列
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson06/assignments/#課題06-1-フィボナッチ数列
import sys


def fibonacci(n):
    # この中を実装してください．
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main(argv):
    for arg in argv[1:]:
        n = int(arg)
        print(f"fibonacci({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main(sys.argv)
