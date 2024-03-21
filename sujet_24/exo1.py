arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )

def parcours_largeur(arbre):
    if arbre == None:
        return []
    f = [arbre]
    res = []
    while len(f)> 0:
        noeud_actuel = f.pop(0)
        g, x, d = noeud_actuel

        res.append(x)
        if g!= None:
            f.append(g)
        if d!= None:
            f.append(d)
    return res

print(parcours_largeur(arbre))

