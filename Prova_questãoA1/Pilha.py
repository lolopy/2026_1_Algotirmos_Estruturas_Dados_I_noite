from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, valor):
        no = No(valor)
        no.prox = self.topo
        self.topo = no

    def desempilhar(self):
        if self.esta_vazia():
            return None
        no = self.topo
        self.topo = self.topo.prox
        return no.dado

    def imprimir(self):
        if self.esta_vazia():
            print("Pilha vazia.")
            return

        atual = self.topo
        while atual is not None:
            atual.dado.imprimir()
            print()
            atual = atual.prox
