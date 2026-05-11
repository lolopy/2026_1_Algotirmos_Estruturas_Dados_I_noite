from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, valor):
        nodo = No(valor)
        nodo.prox = self.topo
        self.topo = nodo
        print(f"Livro adicionado: {valor}")
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Pilha de Livros - LIFO")
        if self.topo is None:
            print("Pilha Vazia")
            return
        aux = self.topo
        while aux:
            print(aux.dado)
            aux = aux.prox

    def remover(self):
        if self.topo is None:
            print("A pilha já está vazia. Nenhum livro para remover.")
            return None
        livro_removido = self.topo.dado
        self.topo = self.topo.prox
        print(f"Livro removido: {livro_removido}")
        return livro_removido

    def contar_por_autor(self, nome_autor):
        if self.topo is None:
            print(f"Nenhum livro na pilha para o autor '{nome_autor}'.")
            return 0

        contador = 0
        nome_autor_normalizado = nome_autor.strip().lower()
        aux = self.topo
        while aux:
            livro = aux.dado
            if hasattr(livro, 'autor') and livro.autor is not None:
                if livro.autor.nome.strip().lower() == nome_autor_normalizado:
                    contador += 1
            aux = aux.prox

        print(f"Livros na pilha do autor '{nome_autor}': {contador}")
        return contador
