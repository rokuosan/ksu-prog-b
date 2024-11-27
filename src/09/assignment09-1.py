import plane_figures as pf

p1 = pf.Point(3, 4)
assert p1.distance() == 5.0, "原点からの距離が正しくありません"
assert p1.distance(p1) == 0.0, "同じ点からの距離が正しくありません"
assert str(p1) == "(3, 4)", "文字列表現が正しくありません"

p2 = pf.Point(1, 1)
assert p2.distance() == 2**0.5, "原点からの距離が正しくありません"

l1 = pf.Line(p2, pf.Point(5, 5))
assert l1.distance() == 32**0.5, "線分の長さが正しくありません"
assert str(l1) == "((1, 1), (5, 5))", "文字列表現が正しくありません"
assert l1.is_on(pf.Point(3, 3)), "点 (3, 3) は線分上にあります"
assert not l1.is_on(pf.Point(0, 0)), "点 (0, 0) は線分上にありません"
