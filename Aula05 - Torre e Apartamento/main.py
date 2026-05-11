from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera
from ListaVagas import ListaVagas

class Condominio:

    def __init__(self):
        self.fila_espera = FilaEspera()
        self.lista_vagas = ListaVagas()

    def adicionar_apartamento_com_vaga(self, apartamento: Apartamento):
        self.lista_vagas.add(apartamento)
        print(f"Apartamento {apartamento.numero} cadastrado com vaga {apartamento.vaga}.")

    def adicionar_apartamento_sem_vaga(self, apartamento: Apartamento):
        apartamento.vaga = None
        self.fila_espera.add(apartamento)
        print(f"Apartamento {apartamento.numero} cadastrado na fila de espera.")

    def liberar_vaga(self, id_apartamento):
        apartamento = self.lista_vagas.remover_por_id(id_apartamento)
        if apartamento is None:
            print(f"Apartamento com id {id_apartamento} não encontrado na lista de vagas.")
            return

        vaga_liberada = apartamento.vaga
        apartamento.vaga = None
        self.fila_espera.add(apartamento)
        print(f"Apartamento {apartamento.numero} liberou a vaga {vaga_liberada} e entrou na fila de espera.")

        if self.fila_espera.inicio is not None:
            próximo = self.fila_espera.remover(vaga_liberada)
            if próximo is not None:
                self.lista_vagas.add(próximo)

    def imprimir_estado(self):
        self.lista_vagas.imprimir()
        self.fila_espera.imprimir()


if __name__ == '__main__':
    torre_a = Torre(1, 'Torre A', 'Rua das Acácias, 100')
    torre_b = Torre(2, 'Torre B', 'Rua das Palmeiras, 50')

    apto101 = Apartamento(1, '101', torre_a, vaga=1)
    apto102 = Apartamento(2, '102', torre_a, vaga=2)
    apto103 = Apartamento(3, '103', torre_a)
    apto104 = Apartamento(4, '104', torre_b)
    apto105 = Apartamento(5, '105', torre_b)

    condominio = Condominio()

    condominio.adicionar_apartamento_com_vaga(apto101)
    condominio.adicionar_apartamento_com_vaga(apto102)
    condominio.adicionar_apartamento_sem_vaga(apto103)
    condominio.adicionar_apartamento_sem_vaga(apto104)
    condominio.adicionar_apartamento_sem_vaga(apto105)

    print('\nEstado inicial:')
    condominio.imprimir_estado()

    print('\nLiberação de vaga pelo apartamento 101:')
    condominio.liberar_vaga(1)
    condominio.imprimir_estado()

    print('\nLiberação de vaga pelo apartamento 102:')
    condominio.liberar_vaga(2)
    condominio.imprimir_estado()
