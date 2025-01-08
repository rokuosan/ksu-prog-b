from sklearn import linear_model
import sys

def read_csv(filename):
    x, y = ([], [])
    with open(filename, "r") as f:
        f.readline()    # ヘッダ行を読み飛ばす．
        for line in f:
            c = line.strip().split(",")
            x.append([int(c[0])])
            y.append(float(c[1]))

    return x, y

x, y = read_csv(sys.argv[1]) # ファイル名はコマンドライン引数で指定する．
# モデル（LinearRegression）のインスタンスを構築する．
model = linear_model.LinearRegression()
# 読み取ったデータを使ってモデルを学習する．
model.fit(x, y)
# x_test を 2024 にして，2024年12月の気温を予測する．
y_pred = model.predict([[2024]])

print(f"2024年12月の平均気温は {y_pred[0]} 度（予測）です．")
