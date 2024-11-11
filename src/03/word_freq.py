# 第3回 課題1: 単語数の分布
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=課題ID
# 教材: https://ksubpb.github.io/2024/lesson03/assignments/#課題03-1-単語数の分布
# 作成: 2454575 / 松本 紘輝

import sys  # コマンドライン引数を受け取るためのライブラリ
import re  # 正規表現を使うためのライブラリ

dic = {}  # 単語の出現回数を格納する辞書
for file in sys.argv[1:]:
    with open(file, "r") as f:
        for line in f:  # ファイルを1行ずつ読み込む
            for word in re.split(r"[, :.'\"“()\r\n\s]", line):  # 正規表現で区切る
                # 単語が辞書にあれば，カウントを1増やす．なければ，1を代入する．
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
print(dic)
