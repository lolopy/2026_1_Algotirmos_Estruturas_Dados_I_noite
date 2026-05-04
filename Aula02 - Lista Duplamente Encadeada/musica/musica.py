class musica:
    
    def __init__(self,titulo,autor,duracao):
        self.titulo = titulo
        self.autor = autor
        self.duracao = duracao
        self.anterior = None
        self.proxima = None


    def __str__(self):
        txt =  self.titulo + "\n" + self.autor
        txt += "\nDuração:" + str(self.duracao)
        return txt 

    