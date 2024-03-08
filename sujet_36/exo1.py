def couples_consecutifs(tab):
    couples = [] # Définition d'un tableau vide qui va contenir tous les couples trouvé
    for k in range(len(tab)-2): # on boucle sur le tableau jusqua la longeur -2 car on cherche des éléments qui se suivent
        if tab[k] + 1 == tab[k+1]: # si l'élément se trouvant à l'index k est égal à l'élément index k+1 on l'ajoute au tableau
            couples.append((tab[k], tab[k+1]))
    return couples # on renvoi le tableau de couples

assert(couples_consecutifs([1, 4, 3, 5]) == [])
assert(couples_consecutifs([1, 4, 5, 3]) == [(4, 5)])
assert(couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)])