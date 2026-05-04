class Apartamento:
    def __init__(self, id, numero, torre, vaga):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Apartamento ID: {self.id}, Numero: {self.numero}, Torre: {self.torre.nome}, Vaga: {self.vaga}")