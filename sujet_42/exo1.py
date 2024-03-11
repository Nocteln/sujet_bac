def tri_selection(tab):    
    for i in range(len(tab) - 1):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min],tab[i]
    return tab

print(tri_selection([1, 52, 6, -9, 12]))