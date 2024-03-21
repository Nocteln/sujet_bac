def nbrOccurences(str):
    res = {}
    for k in range(len(str)):
        if str[k] in res:
            res[str[k]] += 1
        else:
            res[str[k]] = 1
    return res

print(nbrOccurences('Hello world !'))