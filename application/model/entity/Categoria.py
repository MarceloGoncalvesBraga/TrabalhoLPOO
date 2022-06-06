

class Categoria():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNome(self,newnome):
        self.nome = newnome
        return
    

