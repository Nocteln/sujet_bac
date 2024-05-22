ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) )
