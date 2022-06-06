

class Exemplar():
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade

        
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNome(self,newnome):
        self.nome = newnome
        return

    
    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self,newquantidade):
        self.quantidade = newquantidade
        return

