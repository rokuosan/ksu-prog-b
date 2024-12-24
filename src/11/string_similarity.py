import sys
import numpy as np

def build_array(str):
    vector = [0] * 26      # 各要素に 0 が代入された長さ 26 のリストを作成する．
    s = str.lower()        # str を小文字に変換する．
    for i, c in enumerate(range(ord('a'), ord('z') + 1)): # 'a' から 'z' までの各文字 c に対して処理を行う．
        # ord は文字を Unicode に変換する関数である．
        # 'a' を ascii コードに変換し，c を足して，文字に変換する．
        # str に含まれる c の数を数えて，vector の対応する要素に代入する．
        vector[i] = s.count(chr(c))
    return np.array(vector)

def cossim(v1, v2):
    # ここで，ベクトル v1, v2 のコサイン類似度を計算して返す．
    return v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

for i, str1 in enumerate(sys.argv[1:]): # コマンドライン引数の文字列を総当たりで比較する．
    for str2 in sys.argv[i + 2:]:
        v1 = build_array(str1) # 文字列 str1 のベクトルを作成する．
        v2 = build_array(str2) # 文字列 str2 のベクトルを作成する．
        print(f'cossim({str1:15}, {str2:15}) = {cossim(v1, v2)}') # 類似度を計算し，表示する．
