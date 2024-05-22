def recherche(tab, n):
    i = 0
    j = len(tab)-1
    while j >= i :
        mil = (i+j)//2
        if tab[mil] == n:
            return mil
        elif tab[mil] > n:
            j = mil - 1
        else :
            i = mil + 1
    return None

