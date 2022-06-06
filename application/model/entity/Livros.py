

class Livros():
    def __init__(self, id, titulo, isbn, autor, editora, ano, assunto, status):
       # super().__init__(nome)
        self.id = id
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.assunto = assunto
        self.status = status
        
    def getId(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def setTitulo(self,newtitulo):
        self.titulo = newtitulo
        return 
    
    def getIsbn(self):
        return self.isbn

    def setIsbn(self,newisbn):
        self.isbn = newisbn
        return
        
    def getAutor(self):
        return self.autor

    def setAutor(self,newautor):
        self.autor = newautor
        return
    def getEditora(self):
        return self.editora

    def setEditora(self,neweditora):
        self.editora = neweditora
        return

    def getAno(self):
        return self.ano

    def setAno(self,newano):
        self.ano = newano
        return

    def getAssunto(self):
        return self.assunto

    def setAssunto(self,newassunto):
        self.assunto = newassunto
        return
    def getStatus(self):
        return self.status

    def setStatus(self,newstatus):
        self.status = newstatus
        return