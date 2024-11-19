# 第7回 課題1: 特定の名前のファイルを見つける
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題07-1-特定の名前のファイルを見つける
import os
import sys


# name という名前のファイルを base 以下から探す関数．
# 複数見つかる場合もありうるため，見つかったものをリストで返す．
def find_file(name, base, result=None):
    if result is None:
        result = []

    # base がディレクトリの場合
    if os.path.isdir(base):
        # base の一覧を取得し，それぞれを処理する．
        for item in os.listdir(base):
            # それぞれのアイテムに対して，base と item を join する．
            path = os.path.join(base, item)
            # find_file を再起的に呼び出す．
            find_file(name, path, result)

    # そうでない場合
    else:
        filename = os.path.basename(base)  # base から ファイル名部分を取り出す．
        # base が name と一致する場合
        if filename == name:
            # result に base を追加する．
            result.append(base)

    return result


for base in sys.argv[2:]:
    paths = find_file(sys.argv[1], base)
    if paths:
        print(f"{sys.argv[1]}: {paths}")
