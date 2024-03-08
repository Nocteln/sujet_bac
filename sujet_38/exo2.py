def est_cyclique(plan):
    '''
    Prend en paramÃƒÂ¨tre un dictionnaire `plan` correspondant Ãƒ  un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 
'D':'C'}))