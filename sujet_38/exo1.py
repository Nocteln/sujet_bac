def correspond(mot, mot_a_trous):
    s = []
    if len(mot) != len(mot_a_trous):
        return False
    for k in range(len(mot) - 1):
        if mot[k] == mot_a_trous[k] or mot_a_trous[k] == "*":
            s.append(1)
        else:
            s.append(0)
    return sum(s) / len(mot) > 0.5
print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))

# je me suis compliqué la vie pour rien