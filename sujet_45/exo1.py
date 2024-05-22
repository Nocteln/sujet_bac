def compte_occurrences(x, tab):
    res = 0
    for element in tab:
          if element == x:
               res += 1
    return res

print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print(compte_occurrences('a', ['a','b','c','a','d','e','a']))