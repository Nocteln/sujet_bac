def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i+1, j, val)

    # l'element Ãƒ  gauche fait partie de la composante
    if j-1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)

    # l'element Ãƒ  droite fait partie de la composante
    if j+1 < len(M) and M[i][j+1] == 1:
        propager(M, i, j+1, val)
    return M

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]

print(propager(M, 2, 1, 3 ))