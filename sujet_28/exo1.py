def moyenne(tab):
    res = 0
    if len(tab) == 1:
        return tab[0]
    for k in range(len(tab)):
        res+=tab[k]
    return res / len(tab)

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5