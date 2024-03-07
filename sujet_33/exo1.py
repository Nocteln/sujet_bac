a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def taille(tab):
    if len(tab) == 0:
        return 0
    for el in tab:
        # el = parent
        # tab[el] = enfants
        return 1+taille() + taille()



taille(a)