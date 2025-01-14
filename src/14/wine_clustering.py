#
# == なぜうまくクラスタリングされないのかについての考察
#
# 今回はワインのデータセットのうち、0列目と11列目を用いてクラスタリングを行ったが、
# この2つの特徴量だけでは、情報量が少なすぎるため、うまくクラスタリングができなかったのではないかと考えた。
# また、クラスタリングの際には、データのスケールを揃える必要があると予測する。
# 今回使用した2つのデータは、それぞれが異なるスケールであるため、データが正しく分類されなかったのではないだろうか。
#
from sklearn import datasets
from sklearn import cluster
import numpy as np


wine = datasets.load_wine() # ワインのデータセットをロードする．

# kMeans を行うオブジェクトを生成する（クラスタ数は3）．
model = cluster.KMeans(n_clusters=3)
# wine.data を対象にクラスタリングを行う．
model.fit(wine.data)

# 試しに各データの名前と最大・最小・平均値・中央値を表示してみる
for i in range(0, 13):
    M = np.max(wine.data[:, i])
    m = np.min(wine.data[:, i])
    mean = np.mean(wine.data[:, i])
    median = np.median(wine.data[:, i])

    print(f"{wine.feature_names[i]}\t{M}\t{m:.5}\t{mean:.5}\t{median:.2}")

import matplotlib.pyplot as plt
# wine.data の0列目，11列目で散布図を描画する．
plt.scatter(wine.data[:, 0], wine.data[:, 11],c=model.labels_)
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 11], marker="x", c="red")
plt.xlabel(wine.feature_names[0]) # x軸のラベルを設定する．
plt.ylabel(wine.feature_names[11]) # y軸のラベルを設定する．
plt.show() # 表示する．
