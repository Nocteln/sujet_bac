def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)] # Crée un tableau du nombre d'éléments avec des 0 
    if indice < len(liste):
        for i in range(indice):
            L[i] = liste[i]
        L[i+1] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[len(liste)] = element
    return L

print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))