def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = fin - 1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))