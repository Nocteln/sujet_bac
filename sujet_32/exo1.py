def min_et_max(tab):
    res = {"min": tab[0], "max": tab[0]}
    for k in range(len(tab)):
        if tab[k] < res["min"]:
            res["min"] = tab[k]
        if tab[k] > res["max"]:
            res["max"]= tab[k]
    return res

assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {"min": -2, "max": 9}
assert min_et_max([0, 1, 2, 3]) == {"min": 0, "max": 3}
assert min_et_max([3]) == {"min": 3, "max": 3}