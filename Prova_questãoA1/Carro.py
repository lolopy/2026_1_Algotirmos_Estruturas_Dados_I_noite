from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def imprimir(self):
        print("--- Carro ---")
        super().imprimir()
        print(f"Portas: {self._portas}")
