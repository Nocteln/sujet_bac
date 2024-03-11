def recherche(char, chaine):
    i = 0
    for el in chaine:
        if el == char:
            i += 1
    return i

print(recherche('e', "sciences"))
print( recherche('i', "mississippi"))
print(recherche('a', "mississippi"))