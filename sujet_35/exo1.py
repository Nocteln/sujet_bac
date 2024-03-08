def ou_exclusif(a, b):
    tab= []
    for i in range(len(a)):
        if a[i]== b[i]:
            tab.append(0)
        else:
            tab.append(1)
    return tab

a = [1, 0, 1, 0, 1, 1, 0, 1] 
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

print(ou_exclusif(a, b))
print(ou_exclusif(c, d))