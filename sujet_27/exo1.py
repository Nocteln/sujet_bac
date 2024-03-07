def recherche_min(tab):
    min = 0
    if len(tab) == 1:
        return tab[0]
    else:
        for k in range(len(tab)):
            if tab[k] < tab[k-1]:
                min=k
        return min
    
print(recherche_min([2, 4, 1, 4, -3]))