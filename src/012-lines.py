#!/bin/python3
# 第1回 課題2: lines コマンドの実装
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=145511
# 教材: https://ksubpb.github.io/2024/lesson01/assignments/#課題01-2-lines-コマンドの実装

import sys

for i in range(1, len(sys.argv)):
    with open(sys.argv[i]) as f:
        lines = f.readlines()
        print(f"{len(lines):5}  {f.name}")
