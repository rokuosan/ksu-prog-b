# 第4回 課題3: 文字列に含まれる文字の出現頻度を数える関数を作成する
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題04-3-文字列に含まれる文字の出現頻度を数える関数を作成する

import sys


def count_chars(str):
    freq = dict()
    for c in str.lower():
        freq[c] = freq.get(c, 0) + 1
    return freq


for arg in sys.argv[1:]:
    print(f"{arg}: {count_chars(arg)}")
