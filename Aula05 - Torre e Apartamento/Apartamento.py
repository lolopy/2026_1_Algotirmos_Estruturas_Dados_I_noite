from Torre import Torre

class Apartamento:

    def __init__(self, id, numero, torre: Torre, vaga=None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.prox = None

    def __repr__(self):
        vaga_texto = self.vaga if self.vaga is not None else 'sem vaga'
        return (
            f"Apartamento(id={self.id}, numero='{self.numero}', vaga={vaga_texto}, "
            f"torre='{self.torre.nome}')"
        )
