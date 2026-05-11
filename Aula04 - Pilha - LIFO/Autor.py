class Autor:

    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def __repr__(self):
        return f"Autor(nome='{self.nome}', ano nascimento={self.ano_nascimento})"
