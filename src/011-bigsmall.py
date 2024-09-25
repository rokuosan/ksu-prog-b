# 第1回 課題1: bigsmall
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=144514
# 教材: https://ksubpb.github.io/2024/lesson01/assignments/#課題01-1-bigsmall

import random

num = random.randint(1, 10)  # 1 以上 10 以下の乱数を生成する．

# num が 5 以上なら Big，5 未満なら Small を出力する．
if num >= 5:
    print("Big")
else:
    print("Small")
