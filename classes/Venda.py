from turtle import Vec2D
from classes.Produto import Produto

global vendas
vendas = []


class Venda:
    def __init__(self, id=None, produto=None, quantidade=None, valor_total=None):
        self.__id = id
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor_total = valor_total

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = self.validar_produto(produto)

    def get_valor_total(self):
        return self.__valor_total

    def set_valor_total(self, valor_total):
        self.__valor_total = valor_total

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = self.validar_quantidade(quantidade)

    def validar_produto(self, id_produto):
         while True:
            try:
                id_produto = int(id_produto)
                return id_produto
            except ValueError:
                id_produto = input(
                    "Por favor, digite um valor inteiro válido:")

    def validar_quantidade(self, quantidade):
        while True:
            try:
                quantidade = int(quantidade)
                if quantidade >= 0:
                    return quantidade
            except ValueError:
                quantidade = input(
                    "Por favor, digite um valor inteiro válido:")

    def processar_venda(self, estoque, controle):
        self.__produto = estoque.buscar_produto(self.__produto)
        if self.__produto is not None and isinstance(self.__produto, Produto):
            if self.__quantidade > self.__produto.get_quantidade():
                print("\nQuantidade insuficiente em estoque.")
            else:
                estoque.atualizar_produto((self.__produto.get_id(
                )), quantidade=self.__produto.get_quantidade() - self.__quantidade)

                self.__valor_total = self.__quantidade * self.__produto.get_valor()

                controle.adicionar_venda(self)

                print(f"\nVenda realizada com sucesso!\n"
                      f"Produto: {self.__produto.get_nome()}\n"
                      f"Quantidade vendida: {self.__quantidade}\n"
                      f"Valor total: R${self.__valor_total:.2f}")
                return True
        else:
            print("\nProduto não encontrado. Por favor, tente novamente.")
            return False


class ControleDeVendas:
    def __repr__(self):
        linhas = ["{:<10} | {:<10} | {:<9} ".format(
            "Produto", "Quantidade", "Valor total")]
        linhas.append("-" * 40)

        for venda in self.__vendas:
            produto = venda.get_produto()
            nome_do_produto = produto.get_nome()
            quantidade = venda.get_quantidade()
            valor_total = venda.get_valor_total()

            linhas.append("{:<10} | {:<10} | R${:<7.2f}".format(
                nome_do_produto, quantidade, valor_total))

        return "\n".join(linhas)
        
    def __init__(self):
        self.__vendas = []
    
    def adicionar_venda(self, venda):
        if venda is not None and isinstance(venda, Venda):
            self.__vendas.append(venda)
    
    def gerar_relatorio_de_vendas(self):
        return self.__repr__()




# lista produtos para que o usuário possa ver o código
# recebe a entrada com o código do produto
# verifica se a entrada é válida (int) | se n: opção para reenviar ou desistir
# verifica se o código do produto existe na lista | se n: avisa e opção reenviar ou desistir
# recebe a quantidade solicitada
# verifica se a entrada é válida (int) |se n: opção para reenviar ou desistir
# verifica se é válida (>= quantidade) | se n: opção para reenviar ou desistir
# atualiza a qunatidade do produto
# adiciona produto a lista de venda
# nova adição de produto para venda
