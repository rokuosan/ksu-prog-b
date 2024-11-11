# 第6回 課題2: たらい回し関数
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson06/assignments/#課題06-2-たらい回し関数
import time

count = 0


def tarai(x, y, z):
    global count
    count = count + 1
    print(f"tarai({x}, {y}, {z})")
    # ここに関数を実装してください
    if x <= y:
        return y
    else:
        return tarai(tarai(x - 1, y, z), tarai(y - 1, z, x), tarai(z - 1, x, y))


def call_tarai(x, y, z):
    global count
    count = 0
    start = time.time()
    result = tarai(x, y, z)
    end = time.time()
    print(
        f"tarai({x}, {y}, {z}) = {result} (呼び出し回数: {count}, 経過時間: {end - start})"
    )


call_tarai(10, 5, 0)
call_tarai(10, 5, 1)
call_tarai(12, 6, 0)
