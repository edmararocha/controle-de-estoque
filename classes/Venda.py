class Venda:
    controleID = 0
    def __init__(self):
        self.__vendas = {}
        self.__valor_total = 0
        
    def cadastrar_venda(self, produtos):
        pass

    def inserir_produtos(self, produto):
        if produto is None:
            return None
        else:
            pass

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