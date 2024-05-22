def max_dico(dico):
    max = 0
    nom = ""
    for k, v in dico.items():
        if v > max:
            max = v
            nom = k
    return (max, nom)

print(max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }))