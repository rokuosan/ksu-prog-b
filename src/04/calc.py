# 第4回 課題2: 四則演算を行う関数を作成する
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=
# 教材: https://ksubpb.github.io/2024/lesson04/assignments/#課題04-2-四則演算を行う関数を作成する

import sys
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

if len(sys.argv) != 4:
    print('Usage: python3 calc.py <value1> <operator> <value2>')
    sys.exit(1)
value1 = int(sys.argv[1])
operator = sys.argv[2]
value2 = int(sys.argv[3])
print(calc(value1, operator, value2))
