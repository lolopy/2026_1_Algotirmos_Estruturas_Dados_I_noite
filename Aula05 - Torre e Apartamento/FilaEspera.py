from Apartamento import Apartamento

class FilaEspera:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, apartamento: Apartamento):
        apartamento.prox = None
        if self.inicio is None:
            self.inicio = apartamento
        else:
            self.fim.prox = apartamento
        self.fim = apartamento

    def remover(self, numero_vaga):
        if self.inicio is None:
            print("Fila de espera vazia. Nenhum apartamento para receber vaga.")
            return None

        apartamento = self.inicio
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None

        apartamento.prox = None
        apartamento.vaga = numero_vaga
        print(f"Apartamento {apartamento.numero} recebeu a vaga {numero_vaga}.")
        return apartamento

    def imprimir(self):
        print("\n----------------------")
        print("Fila de Espera")
        if self.inicio is None:
            print("Fila de espera vazia")
            return

        aux = self.inicio
        while aux:
            print(aux)
            aux = aux.prox
