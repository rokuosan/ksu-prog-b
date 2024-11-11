def sum_range(until, start=1):
    if start >= until:
        return 0

    # return int(sum(list(range(start, until + 1))))
    return int((until + start) * ((until - start + 1) * 0.5))


assert sum_range(10) == 55, "Error: sum_range(10) が 55 を返しません．"
assert sum_range(10, 3) == 52, "Error: sum_range(10, 3) が 52 を返しません．"
assert sum_range(4, 2) == 9, "Error: sum_range(2, 4) が 9 を返しません．"
assert sum_range(10, 10) == 0, "Error: sum_range(10, 10) が 0 を返しません．"
