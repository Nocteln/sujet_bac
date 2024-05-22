def enumere(tab):
    res = {}
    for k in range(len(tab)):
        if tab[k] in res:
            res[tab[k]].append(k)
        else:
            res[tab[k]] = [k]
    return res

print(enumere([1, 2, 3, 1, 2, 3, 4]))