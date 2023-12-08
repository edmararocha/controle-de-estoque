from classes.Estoque import Estoque
from classes.Produto import Produto
from classes.Venda import ControleDeVendas, Venda

def exibir_menu():
    print("\n[1] Adicionar Produto")
    print("[2] Listar Produtos")
    print("[3] Cadastrar Venda")
    print("[4] Gerar Relatório de Vendas")
    print("[5] Mostrar Controle dos Perecíveis")
    print("[0] Sair")
    opcao = input("\nEscolha uma opção:")

    def adicionar_produto():
        print("\nAdicionar Produtos\n")

        produto = Produto()
        produto.set_nome(input("Digite o nome do produto:"))
        produto.set_valor(input("Digite o valor do produto:"))
        produto.set_quantidade(input("Digite a quantidade do produto:"))
        print("\n** Caso o alimento for perecível digite sua data de vencimento, se não for clique ENTER **\n")
        produto.set_data_de_vencimento(input("Digite a data de vencimento:"))
        
        estoque.adicionar_produto(produto)

        print("\nProduto adicionado com sucesso!")

    def listar_produtos():
        print("\nLista de Produtos\n")
        print(estoque.__repr__())

    def cadastrar_venda():
        print(estoque.__repr__())
        
        venda = Venda()
        venda.set_produto(input("\nDigite o ID do produto que deseja vender:"))
        venda.set_quantidade(input("\nDigite a quantidade do produto:"))

        venda.processar_venda(estoque, controle)


    def gerar_relatorio_vendas():
        print("\nRelatório de Vendas\n")
        print(controle.gerar_relatorio_de_vendas())
    
    def mostrar_controle_pereciveis():
        print("\nControle dos Perecíveis\n")

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
        print("\nSaindo do programa. Até mais!")
    else:
        print("\nOpção inválida. Tente novamente.")
    if opcao != '0':
        exibir_menu()

global estoque
estoque = Estoque()
controle = ControleDeVendas()

exibir_menu()
