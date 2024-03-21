def recherche_min(tab):
    mini = tab[0]
    for k in range(len(tab) - 1):
        if tab[k] < mini:
            mini = tab[k]
    return mini

print(recherche_min([5, 3, 2, 2, 4]))
print(recherche_min([-1, -2, -3, -3]))