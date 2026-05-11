class Torre:

    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f"Torre(id={self.id}, nome='{self.nome}', endereco='{self.endereco}')"
