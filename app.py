from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

def mostrar_restaurantes(restaurantes):
    for restaurante in restaurantes:
        status = "Ativo" if restaurante.ativo else "Inativo"
        print(f"{restaurante.nome} - Categoria: {restaurante.categoria} - Status: {status} - Média de Avaliações: {restaurante.media_avaliacoes()}")

def cadastrar_restaurante(restaurantes):
    nome = input("Nome do Restaurante: ")
    categoria = input("Categoria do Restaurante: ")
    restaurante = Restaurante(nome, categoria)
    restaurantes.append(restaurante)
    print("Restaurante cadastrado com sucesso!")

def ativar_desativar_restaurante(restaurantes):
    nome = input("Nome do Restaurante para ativar/desativar: ")
    for restaurante in restaurantes:
        if restaurante.nome == nome:
            restaurante.ativo = not restaurante.ativo
            status = "Ativo" if restaurante.ativo else "Inativo"
            print(f"Restaurante {restaurante.nome} agora está {status}.")
            return
    print("Restaurante não encontrado.")

def deixar_avaliacao(restaurantes):
    nome = input("Nome do Restaurante para avaliar: ")
    for restaurante in restaurantes:
        if restaurante.nome == nome:
            nota = float(input("Nota da Avaliação (0 a 5): "))
            avaliacao = Avaliacao(nota)
            restaurante.adicionar_avaliacao(avaliacao)
            print("Avaliação adicionada com sucesso!")
            return
    print("Restaurante não encontrado.")

def main():
    restaurantes = []

    while True:
        print("\nOpções:")
        print("1. Mostrar Restaurantes")
        print("2. Cadastrar Restaurante")
        print("3. Ativar/Desativar Restaurante")
        print("4. Deixar Avaliação")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_restaurantes(restaurantes)
        elif opcao == "2":
            cadastrar_restaurante(restaurantes)
        elif opcao == "3":
            ativar_desativar_restaurante(restaurantes)
        elif opcao == "4":
            deixar_avaliacao(restaurantes)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
