a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def taille(a, lettre):
    if lettre == "":
        return 0
    return 1 + taille(a, a[lettre][0]) + taille(a, a[lettre][1])



print(taille(a,"F"))