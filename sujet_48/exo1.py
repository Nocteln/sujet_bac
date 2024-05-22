def voisins_entrants(adj, x):
    t = []
    for i in range(len(adj)):
        if x in adj[i]:
            t.append(i)
    return t