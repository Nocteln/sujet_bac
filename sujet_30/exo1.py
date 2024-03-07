def moyenne(tab):
    s = 0
    for k in range(len(tab)):
        s += tab[k]
    return s/len(tab)

print(moyenne([1.0, 2.0, 4.0]))
print(moyenne([1.0]))