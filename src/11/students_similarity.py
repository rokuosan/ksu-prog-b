import sys
import numpy as np

def open_csv(filename):
    students = dict()
    with open(filename, "r") as f:
        f.readline()    # ヘッダ行を読み飛ばす．
        for line in f:
            scores = []
            cols = line.strip().split(",") # 改行を削除し，コンマで分割する．
            for item in cols[1:]:
                scores.append(float(item))       # 文字列を整数に変換して scores に追加する．
            students[cols[0]] = np.array(scores) # scores を numpy 配列に変換して students に追加する．
    return students

def similarity(v1, v2):
    # ベクトル v1 のノルムを計算する．
    norm1 = np.linalg.norm(v1)
    # ベクトル v2 のノルムを計算する．
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 and norm2 == 0:  # どちらも0の場合は一致するので，1.0を返す．
        return 1.0
    elif norm1 == 0 or norm2 == 0: # どちらかが0の場合は一致しないので，0.0を返す．
        return 0.0
    return # ベクトル v1 と v2 のコサイン類似度を計算する（norm1, norm2 のどちらかが0の場合は0除算が発生するため，計算できない）．

students = open_csv(sys.argv[1]) # コマンドライン引数のファイルを読み込む．
ids = list(students.keys())      # 学生の ID を取得する．
similarities = np.zeros((len(ids), len(ids))) # 類似度を格納する行列を作成する．

for i, id1 in enumerate(ids):
    for j, id2 in enumerate(ids):
        if id1 == id2: # 右上と左下で同じ結果になるので，左下だけ計算する．
            break      # 右上の場合は計算しない．
        similarities[i, j] = similarity(students[id1], students[id2]) # 類似度を計算して格納する．

for id in ids:
    print(f",{id}", end="") # ヘッダを表示する．
print()
for i, id1 in enumerate(ids):
    print(f"{id1}", end="")
    for j, id2 in enumerate(ids):
        if id1 == id2:
            break
        print(f",{similarities[i, j]:.2f}", end="")
    print()
