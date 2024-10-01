# 第2回 課題3: 素因数分解
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=161168
# 教材: https://ksubpb.github.io/2024/lesson02/assignments/#課題02-3-素因数分解
# 作成: 2454575 / 松本 紘輝

import sys

for v in sys.argv[1:]:
    num = int(v) # コマンドライン引数を整数に変換する．
    factors = [] # 素因数を格納するリストを初期化する．
    value = num  # 素因数分解する値を初期化する．
    factor = 2   # 素因数
    # factor が value より小さい間繰り返す．
    while factor < value:
        # value が factor で割り切れたら
        if value % factor == 0:
            # value を factors に追加する．
            factors.append(factor)
            # value を factor で割り，value に再代入する．
            value //= factor
        # そうでなければ
        else:
            # factor を 1 増加させてループを繰り返す．
            factor += 1
    # ループ後，value が 1 でない場合
    if value != 1:
        # value を factors に追加する．
        factors.append(value)
    # 結果を出力する．num を 8桁右寄せで表示する．
    # join は文字列を結合するメソッドで，リストの要素を文字列に変換して，"*" で結合する．
    print(f"{num:>8}: {' * '.join(map(str, factors))}")
