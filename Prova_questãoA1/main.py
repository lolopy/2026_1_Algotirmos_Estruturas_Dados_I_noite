from Pilha import Pilha
from Carro import Carro
from Drone import Drone


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def cadastrar_carro():
    print("\nCadastro de carro")
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    portas = ler_inteiro("Quantidade de portas: ")
    return Carro(marca, modelo, portas)


def cadastrar_drone():
    print("\nCadastro de drone")
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    helices = ler_inteiro("Quantidade de hélices: ")
    return Drone(marca, modelo, helices)


def imprimir_menu():
    print("\n=== Menu Pilha de Veículos ===")
    print("1 - Adicionar carro")
    print("2 - Remover carro")
    print("3 - Adicionar drone")
    print("4 - Remover drone")
    print("5 - Imprimir pilha de carros")
    print("6 - Imprimir pilha de drones")
    print("7 - Sair")


def main():
    pilha_carros = Pilha()
    pilha_drones = Pilha()

    while True:
        imprimir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            carro = cadastrar_carro()
            pilha_carros.empilhar(carro)
            print("Carro adicionado à pilha de carros.")

        elif opcao == '2':
            carro = pilha_carros.desempilhar()
            if carro is None:
                print("A pilha de carros está vazia.")
            else:
                print("Carro removido:")
                carro.imprimir()

        elif opcao == '3':
            drone = cadastrar_drone()
            pilha_drones.empilhar(drone)
            print("Drone adicionado à pilha de drones.")

        elif opcao == '4':
            drone = pilha_drones.desempilhar()
            if drone is None:
                print("A pilha de drones está vazia.")
            else:
                print("Drone removido:")
                drone.imprimir()

        elif opcao == '5':
            print("\n--- Pilha de Carros ---")
            pilha_carros.imprimir()

        elif opcao == '6':
            print("\n--- Pilha de Drones ---")
            pilha_drones.imprimir()

        elif opcao == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
