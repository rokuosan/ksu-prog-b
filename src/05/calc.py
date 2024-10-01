# 第5回 課題2: 四則演算を行う関数をテストする処理
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題05-2-四則演算を行う関数をテストする処理

import operator as op


def calc(value1, operator, value2):
    # operator の値に応じて，value1 と value2 の演算結果を返します．
    # return eval(f"{value1} {operator} {value2}")
    operators = {
        "+": op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
    }
    return operators[operator](value1, value2)

assert calc(4, "+", 2) == 6
assert calc(4, "-", 2) == 2
assert calc(4, "*", 2) == 8
assert calc(4, "/", 2) == 2

