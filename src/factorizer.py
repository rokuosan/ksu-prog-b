# 第2回 課題2: 素因数分解
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=161168
# 教材: https://ksubpb.github.io/2024/lesson02/assignments/#課題02-2-素因数分解
# 作成: 2454575 / 松本 紘輝

import sys   # コマンドライン引数を取得するためのライブラリ

for value in sys.argv[1:]:     # コマンドライン引数を順に処理する．
    num = int(value)           # コマンドライン引数を整数に変換する．
    factors = []               # 素因数を格納するリストを初期化する．
    # 2 から num まで繰り返す．
    for i in range(1, num+1):
        # num が i で割り切れるとき，factors に i を追加する．
        if num % i == 0:
            factors.append(i)
    print(f"{num}: {factors}") # num（数値）と factors（素因数一覧）を出力する
