import vector as v

v1 = v.Vector(3, 4, 5)
v2 = v.Vector(1, 2, 3)

v3 = v1 + v2
assert v3[0] == 4 and v3[1] == 6 and v3[2] == 8, "ベクトルの足し算が正しくありません"
assert v1 * v2 == 26, "ベクトルの内積の計算が正しくありません"
assert str(v1) == "(3, 4, 5)", "ベクトルの文字列表現が正しくありません"
assert len(v1) == 3, "ベクトルの長さが正しくありません"
assert v1.norm() == 50 ** 0.5, "ベクトルのノルム（大きさ）の計算が正しくありません．"

v4 = v.Vector(1, 1, 1, 1, 1)
assert len(v4) == 5, "ベクトルの長さが正しくありません"
assert v4.norm() == 5 ** 0.5, "ベクトルのノルム（大きさ）の計算が正しくありません．"
assert v4 + v1 == None, "要素数の異なるベクトル同士の足し算は計算できないので，None が返るはずです．"
assert v1 * v4 == None, "要素数の異なるベクトル同士の内積は計算できないので，None が返るはずです．"
