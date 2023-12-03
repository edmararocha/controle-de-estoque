from classes.Estoque import Estoque
from classes.Produto import Produto


global estoque
estoque = Estoque()


def menu():
    print("\n[1] Adicionar Produto")
    print("[2] Listar Produtos")
    print("[3] Cadastrar Venda")
    print("[4] Gerar Relatório de Vendas")
    print("[5] Mostrar Controle dos Perecíveis")
    print("[0] Sair")
    opcao = input("\nEscolha uma opção:")

    def adicionar_produto():
        print("Adicionar Produtos")
        produto = Produto()
        produto.set_nome(input("Digite o nome do produto:"))
        produto.set_valor(input("Digite o valor do produto:"))
        produto.set_quantidade(input("Digite a quantidade do produto:"))
        produto.set_perecivel(input("Digite a data de vencimento:"))
        estoque.adicionar_produto(produto)
        print("\nProduto adicionado com sucesso!")

    def listar_produtos():
        print("Função Listar Produtos\n")
        print(estoque)

    def cadastrar_venda():
        print("Função Cadastrar Venda")

    def gerar_relatorio_vendas():
        print("Função Gerar Relatório de Vendas")
    # Chama recursivamente o menu em caso de opção inválida.    menu()if __name__ == '__main__':    menu()

    def mostrar_controle_pereciveis():
        print("Função Mostrar Controle dos Perecíveis")

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        cadastrar_venda()
    elif opcao == '4':
        gerar_relatorio_vendas()
    elif opcao == '5':
        mostrar_controle_pereciveis()
    elif opcao == '0':
        print("Saindo do programa. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")

    menu()


menu()
