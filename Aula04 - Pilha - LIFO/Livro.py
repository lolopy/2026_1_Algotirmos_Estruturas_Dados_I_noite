from Autor import Autor

class Livro:

    def __init__(self, titulo, paginas, autor: Autor):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor

    def __repr__(self):
        return (
            f"Livro(titulo='{self.titulo}', paginas={self.paginas}, "
            f"autor={self.autor.nome}, ano={self.autor.ano_nascimento})"
        )
