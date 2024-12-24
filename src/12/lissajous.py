import math
import matplotlib.pyplot as plt

A = 1
B = 1

a = 3
b = 4
delta = math.pi / 4

x = []
y = []
for i in range(0, 361): # 0〜360度まで．
    t = i * (math.pi / 180)       # ラジアンに変換する．
    # x に値を追加する（x.append(...)）．
    # x = A * cos(a*t)
    x.append(A * math.cos(a * t))
    # y に値を追加する（y.append(...)）．
    # y = B * sin(b*t + δ)
    y.append(B * math.sin(b * t + delta))

plt.plot(x, y)
plt.text(0, 1.15, f"A={A}, B={B}, a={a}, b={b}, δ={delta}", fontsize=12, ha="center")
plt.axis("equal") # グラフの縦横比を 1:1 にする．
plt.show()
