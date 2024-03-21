n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

def insertion_abr(abr, val):
    if abr == None:
        return (None, val, None)
    f = [abr]
    noeud_actuel = f.pop(0)
    print(noeud_actuels)
    g, v, d = noeud_actuel
    if val < v:
        n = insertion_abr(g, val)
        return (n, v, d)
    elif val > v:
        n= insertion_abr(d, val)
        return (g, v, n)
    return abr
    
print(insertion_abr(abr1, 4))
