

class Professor:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula
    
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNome(self,newnome):
        self.nome = newnome
        return

    def getMatricula(self):
        return self.matricula

    def setMatricula(self,newmatricula):
        self.matricula = newmatricula
        return

    def toString(self):
        return f'Nome  :',self.getNome()
