def moyenne(tab):
    if len(tab) == 0:
        return "Tableau vide"
    else:
        return sum(tab)/ len(tab)
    
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))