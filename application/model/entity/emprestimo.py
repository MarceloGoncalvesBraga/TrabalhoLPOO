

class Emprestimo:
    def __init__(self, id, idLivro, idUsuario, datainit, datadev, devolvido,reservado, encerrado):
        self.id = id
        self.idLivro = idLivro
        self.idUsuario = idUsuario
        self.datainit = datainit
        self.datadev = datadev
        self.devolvido = devolvido
        self.reservado = reservado
        self.encerrado = encerrado


    def getId(self):
        return self.id

    def getidLivro(self):
        return self.idLivro

    def getIdUsuario(self):
        return self.idUsuario
    
    def getDatainit(self):
        return self.datainit
    
    def getDatadev(self):
        return self.datadev

    def getDevolvido(self):
        return self.devolvido

    def setDevolvido(self, newdevolvido):
        self.devolvido = newdevolvido
        return

    def getReservado(self):
        return self.reservado

    def setReservado(self, newreservado):
        self.reservado = newreservado
        return
    def getEncerrado(self):
        return self.encerrado

    def setEncerrado(self, newencerrado):
        self.encerrado = newencerrado
        return

        

