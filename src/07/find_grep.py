# 第7回 課題3: 特定の内容を含むファイルを検索する
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題07-3-特定の内容を含むファイルを検索する
import sys
import os

# file_path というファイルに keyword が含まれているかを判定する関数
# 含まれていれば True を返し，そうでなければ False を返す．
def contains_keyword(file_path, keyword):
    # file_path を読み込みモードで開く．
    with open(file_path) as f:
        # ファイルを一行ずつ読み込む．
        for line in f:
            # line に keyword が含まれているかを判定する．(文字列中に文字列が含まれているか)
            if keyword in line:
                # 含まれていれば True を返す．
                return True
    # 含まれていなければ False を返す．
    return False

# name という名前のファイルを base 以下から探す関数．
# 複数見つかる場合もありうるため，見つかったものをリストで返す．
def find_grep(keyword, base, result = None):
    if result is None:
        result = []

    # base がディレクトリの場合
    if os.path.isdir(base):
        # base の一覧を取得し，それぞれを処理する．
        for child in os.listdir(base):
            if not child.startswith("."): # 隠しファイルは対象外とする．
                # それぞれのアイテムに対して，base と child を join する．
                child_path = os.path.join(base, child)
                # find_grep を再起的に呼び出す．
                find_grep(keyword, child_path, result)
    # そうでない場合
    else:
        if contains_keyword(base, keyword): # base に keyword が含まれているかを判定する．
            # result に base を追加する．
            result.append(base)
    return result

for base in sys.argv[2:]:
    paths = find_grep(sys.argv[1], base)
    if paths:
        print(f"{sys.argv[1]}: {paths}")
