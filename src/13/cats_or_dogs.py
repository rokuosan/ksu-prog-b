from PIL import Image
from sklearn import tree # 決定木を用いるには，tree モジュールをインポートする．
import numpy as np
import os
import sys

# basepath 直下の cats と dogs 以下に猫，犬の画像があるとする．
def read_image(basepath): # 画像を読み込む．
    x = []
    y = []
    for file in os.listdir(os.path.join(basepath, "cats")):
        if file.endswith(".jpg"): # jpgファイルのみを対象とする．
            img = Image.open(os.path.join(basepath, "cats", file))
            img2 = img.resize((128, 128))      # 画像の大きさを 128x128に統一する．
            x.append(np.array(img2).flatten()) # 画像を1次元配列に変換し，xに追加する．
            y.append("cats")
    for file in os.listdir(os.path.join(basepath, "dogs")):
        if file.endswith(".jpg"): # jpgファイルのみを対象とする．
            img = Image.open(os.path.join(basepath, "dogs", file))
            img2 = img.resize((128, 128))      # 画像の大きさを 128x128に統一する．
            x.append(np.array(img2).flatten()) # 画像を1次元配列に変換し，xに追加する．
            y.append("dogs")
    return x, y

def learn_data(x, y):
    # 決定木（DecisionTree）のモデルを構築する．
    model = tree.DecisionTreeClassifier(
        max_depth=5,
        random_state=0,
    )
    # 構築したモデルを使って，学習する．
    model.fit(x, y)
    return model

x, y = read_image(sys.argv[1])
model = learn_data(x, y)
for file in sys.argv[2:]:
    img = Image.open(file)
    img2 = img.resize((128, 128)) # 画像の大きさを 128x128に統一する．
    x = np.array(img2).flatten()  # 画像を1次元配列に変換する．
    print(f"{file}: {model.predict([x])}")
