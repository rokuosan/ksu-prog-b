# 第2回 課題1: 乱数値100個の統計
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=161167
# 教材: https://ksubpb.github.io/2024/lesson02/assignments/#課題02-1-乱数値100個の統計
# 作成: 2454575 / 松本 紘輝

import random  # 乱数を生成するためのライブラリ

randoms = []
max = 0  # 最大値，
min = float("inf")  # 最小値，
sum = 0  # 合計値の初期値を適切に設定しましょう．

for i in range(100):  # 100 回繰り返す．
    num = random.randint(1, 1000)  # 1 以上 1000 未満の乱数を生成する．
    # randoms に num を追加する．
    randoms.append(num)
    # 最大値，最小値，合計値を更新する．
    if num > max:
        max = num
    if num < min:
        min = num
    sum += num

# 統計値を出力する．
print(f"max: {max:4} min: {min:4} sum: {sum:6} avg: {sum/100:6.2f}")
# randoms に格納された乱数値を順に出力する．
# enumerate 関数を使うと，インデックスを取得できる．
# インデックスを10で割ったときの余りが9のときに開業すると良い．
# 数値の右寄せは {:>4} で指定できる（4桁）．
for i, num in enumerate(randoms):
    print(f"{num:>4}", end=" ")
    if i % 10 == 9:
        print()
