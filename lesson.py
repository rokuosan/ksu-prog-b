import random
import math
import matplotlib.pyplot as plt


hit = 0
n = 10000
red_x = []  # ヒットした点のx座標を格納するリスト
red_y = []  # ヒットした点のy座標を格納するリスト
blue_x = []  # ヒットしなかった点のx座標を格納するリスト
blue_y = []  # ヒットしなかった点のy座標を格納するリスト

for i in range(n):
    x = random.random()
    y = random.random()
    if math.sqrt(x * x + y * y) <= 1:
        hit = hit + 1
        red_x.append(x)
        red_y.append(y)
    else:
        blue_x.append(x)
        blue_y.append(y)

pi = 4 * hit / n
print("pi = ", pi)

plt.figure(figsize=(6, 6))  # グラフの大きさを正方形に設定する．
plt.title(f"Monte Carlo Simulation (pi={pi}, n={n})")
plt.scatter(red_x, red_y, color="red", s=1)  # ヒットした点を赤でプロットする．
plt.scatter(blue_x, blue_y, color="blue", s=1)  # ヒットしなかった点を青でプロットする．
plt.show()
