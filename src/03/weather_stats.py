# 第3回 課題2: 猛暑日、真夏日、真冬日，冬日の日数
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=課題ID
# 教材: https://ksubpb.github.io/2024/lesson03/assignments/#課題03-2-猛暑日真夏日真冬日冬日の日数
# 作成: 2454575 / 松本 紘輝
import sys

# 気温バロメータ
barometer = [
    {
        "key": "extremely_hot",
        "name": "猛暑日",
        "condition": lambda max, min: (max >= 35),
    },
    {
        "key": "hot_summer",
        "name": "真夏日",
        "condition": lambda max, min: (max >= 30),
    },
    {
        "key": "summer",
        "name": "夏日",
        "condition": lambda max, min: (max >= 25),
    },
    {
        "key": "ice",
        "name": "真冬日",
        "condition": lambda max, min: (max < 0),
    },
    {
        "key": "frost",
        "name": "冬日",
        "condition": lambda max, min: (min < 0),
    },
]

# 各日の最高気温を保持する
data = {
    "extremely hot day": 0,
    "hot summer day": 0,
    "summer day": 0,
    "ice day": 0,
    "frost day": 0,
}

dic = {}
years = set()

with open(sys.argv[1], "r") as f:
    f.readline()  # 1行目を読み飛ばす．
    for line in f.readlines():
        (date, max_s, min_s, rests) = line.split(
            ","
        )  # 行をコンマで分割し，それぞれを代入する．
        (year, max, min) = (date[:4], float(max_s), float(min_s))
        (extremely_hot, hot, summer, ice, frost) = (0, 0, 0, 0, 0)
        years.add(year)  # 年を集合に追加しておく．

        # 猛暑日，真夏日，夏日，真冬日，冬日を判定する．
        # extermely_hot, hot, summer, ice, frost いずれかを1にする or 0 のままにする．
        y = list(dic.get(year, (extremely_hot, hot, summer, ice, frost, 0)))
        if y[len(y) - 1] == 0:
            dic[year] = tuple(y)
        for i, b in enumerate(barometer):
            if b["condition"](max, min):
                y[i] += 1
                break

        y[len(y) - 1] += 1
        if year in dic:
            # dic[year] からタプルとして，猛暑日，真夏日，夏日，真冬日，冬日，日数を取り出す．
            # dic[year] にタプルとして，猛暑日，真夏日，夏日，真冬日，冬日，日数を格納する．
            # その際，判定とところで得られた extermely_hot, hot, summer, ice, frost をそれぞれに加算する．
            # 日数は1増やす．
            dic[year] = tuple(y)
        else:
            dic[year] = (extremely_hot, hot, summer, ice, frost, 1)

for year in sorted(years):  # 年を昇順にソートして繰り返す．
    (extremely_hot, hot, summer, ice, frost, days) = dic[year]
    print(
        f"{year}  猛暑日 {extremely_hot:>3}, 真夏日 {hot:>2}, 夏日 {summer:>2}, 真冬日 {ice:>2}, 冬日 {frost:>2} ({days:>3}日)"
    )
