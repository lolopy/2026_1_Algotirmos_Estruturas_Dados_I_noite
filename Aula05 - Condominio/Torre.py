class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Torre ID: {self.id}, Nome: {self.nome}, Endereco: {self.endereco}")