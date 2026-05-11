from Apartamento import Apartamento

class ListaVagas:

    def __init__(self):
        self.inicio = None

    def add(self, apartamento: Apartamento):
        apartamento.prox = None
        if self.inicio is None or apartamento.vaga < self.inicio.vaga:
            apartamento.prox = self.inicio
            self.inicio = apartamento
            return

        ant = self.inicio
        aux = self.inicio.prox
        while aux is not None and aux.vaga < apartamento.vaga:
            ant = aux
            aux = aux.prox

        apartamento.prox = aux
        ant.prox = apartamento

    def remover_por_id(self, id_apartamento):
        if self.inicio is None:
            return None

        if self.inicio.id == id_apartamento:
            removido = self.inicio
            self.inicio = self.inicio.prox
            removido.prox = None
            return removido

        ant = self.inicio
        aux = self.inicio.prox
        while aux is not None:
            if aux.id == id_apartamento:
                ant.prox = aux.prox
                aux.prox = None
                return aux
            ant = aux
            aux = aux.prox

        return None

    def imprimir(self):
        print("\n----------------------")
        print("Apartamentos com vaga")
        if self.inicio is None:
            print("Nenhum apartamento com vaga")
            return

        aux = self.inicio
        while aux:
            print(aux)
            aux = aux.prox
