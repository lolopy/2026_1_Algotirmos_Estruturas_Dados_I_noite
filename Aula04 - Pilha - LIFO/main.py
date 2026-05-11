from Pilha import Pilha
from Autor import Autor
from Livro import Livro

pilha = Pilha()

# Criar autores
autor1 = Autor(nome='Machado de Assis', ano_nascimento=1839)
autor2 = Autor(nome='Clarice Lispector', ano_nascimento=1920)
autor3 = Autor(nome='Machado de Assis', ano_nascimento=1839)

# Adicionar livros na pilha
pilha.add(Livro('Dom Casmurro', 256, autor1))
pilha.add(Livro('A Hora da Estrela', 96, autor2))
pilha.add(Livro('Memórias Póstumas de Brás Cubas', 288, autor3))

# Imprimir pilha de livros
pilha.imprimir()

# Contar livros por autor
pilha.contar_por_autor('Machado de Assis')
pilha.contar_por_autor('Clarice Lispector')

# Remover livros da pilha
pilha.remover()
pilha.remover()

# Imprimir pilha após remoções
pilha.imprimir()

# Contar novamente depois de remover
pilha.contar_por_autor('Machado de Assis')









