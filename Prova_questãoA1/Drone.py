from Veiculo import Veiculo

class Drone(Veiculo):

    def __init__(self, marca, modelo, quantidade_helices):
        super().__init__(marca, modelo)
        self.__quantidade_helices = quantidade_helices

    @property
    def quantidade_helices(self):
        return self.__quantidade_helices

    def imprimir(self):
        print("--- Drone ---")
        super().imprimir()
        print(f"Quantidade de hélices: {self.__quantidade_helices}")
