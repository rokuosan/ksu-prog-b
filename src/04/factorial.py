# 第4回 課題1: 階乗を計算する関数を作成する
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題04-1-階乗を計算する関数を作成する

import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


for arg in sys.argv[1:]:
    n = int(arg)
    print(f"{n}! = {factorial(n)}")
