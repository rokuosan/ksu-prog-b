#!/bin/python3
# 第1回 課題3: ヒストグラムの作成
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=145510
# 教材: https://ksubpb.github.io/2024/lesson01/assignments/#課題01-3-ヒストグラムの作成

import sys
from typing import List
from matplotlib import pyplot as plt

data: List[int] = []
with open(sys.argv[1]) as f:
    for line in f:
        striped_line = line.strip()  # 読み込んだ行の前後の空白を削除する．
        items = striped_line.split(" ")  # 行を空白で分割する．
        loc = int(items[0])  # 行数を整数に変換する．
        data.append(loc)  # 名前と行数のペアを data に追加する．

# ヒストグラムを作成する．
plt.hist(
    data, bins=100, range=(0, 1000)
)  # ビン（棒）数を100に設定して，0〜1000行の範囲でヒストグラムを描画する．
plt.title("File Lines (bins=100)")  # グラフのタイトルを設定する．
plt.show()
