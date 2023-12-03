from classes.Produto import Produto


class Estoque:
    controleID = 0  # controle das chaves a serem adicionadas a cada novo produto

    def __repr__(self):
        linhas = ["{:<3} | {:<10} | {:<7} | {:<10}".format(
            "ID", "Produto", "Valor", "Quantidade")]
        linhas.append("-" * 40)

        for id_produto, produto in self.__produtos.items():
            nome = produto["nome"]
            valor = produto["valor"]
            quantidade = produto["quantidade"]
            linhas.append("{:<3} | {:<10} | R${:<5.2f} | {:<10}".format(
                id_produto, nome, valor, quantidade))

        return "\n".join(linhas)

    def __init__(self):
        self.__produtos = {}  # Usando dicionário para guardar os dados dos produtos

    def adicionar_produto(self, produto):
        Estoque.controleID = Estoque.controleID+1
        if isinstance(produto, Produto):
            self.__produtos[Estoque.controleID] = {"nome": produto.get_nome(
            ), "valor": produto.get_valor(), "quantidade": produto.get_quantidade()}

    def listar_produtos(self):
        return self.__produtos

    def atualizar_produtos(self):
        pass

    def excluir_produtos(self):
        pass