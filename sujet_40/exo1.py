def nombre_de_mots(phrase):
    if phrase[len(phrase) - 2] == " ":
        count = 0
    else:
        count = 1
    for k in range(len(phrase)):
        if phrase[k] == " ":
            count += 1
    return count

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))