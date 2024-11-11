import sys


def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


n = int(sys.argv[1])
k = int(sys.argv[2])

print(f"combination({n}, {k}) = {combination(n, k)}")
