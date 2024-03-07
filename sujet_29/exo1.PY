class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
    def taille(self):
        pass
    
a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)