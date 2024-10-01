# 第2回 課題2: 約数の列挙
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=課題ID
# 教材: https://ksubpb.github.io/2024/lesson02/assignments/#課題02-2-約数の列挙
# 作成: 2454575 / 松本 紘輝
import sys  # コマンドライン引数を取得するためのライブラリ

for value in sys.argv[1:]:  # コマンドライン引数を順に処理する．
    num = int(value)  # コマンドライン引数を整数に変換する．
    divisors = []  # 約数を格納するリストを初期化する．
    # 2 から num/2 まで繰り返す．
    for i in range(2, int(num / 2) + 1):
        # num が i divisors に i を追加する．
        if num % i == 0:
            divisors.append(i)

    divisors.append(num)
    print(f"{num}: {divisors}")  # num（数値）と divisors（約数一覧）を出力する．
