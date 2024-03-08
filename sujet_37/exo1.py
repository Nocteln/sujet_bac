def recherche(elt, tab):
    i = -1
    for k in range(len(tab) - 1):
        if tab[k] == elt:
            i = k
    return i

print(recherche(1, [2,3,4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))