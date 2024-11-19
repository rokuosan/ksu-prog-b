# 第7回 課題2: 年齢を当てる
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題07-2-年齢を当てる
import sys

def find_age(age, low, high, step=1) -> int:
    mid = (low + high) // 2

    # 二分探索する
    if age < mid:
        return find_age(age, low, mid - 1, step + 1)
    elif age > mid:
        return find_age(age, mid + 1, high, step + 1)

    return step

for age_string in sys.argv[1:]:
    age = int(age_string)
    step = find_age(age, 0, 100)
    print(f"age = {age}, step = {step}")
