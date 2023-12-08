import datetime
from classes.Produto import Produto


# Lista com dados base para utilizar as funções do sistema
data = [
    Produto(1, "Maçã", 2.5, 10, datetime.date(2023, 12, 31)),
    Produto(2, "Banana", 1.5, 15, datetime.date(2023, 12, 25)),
    Produto(3, "Uva", 4.0, 8, datetime.date(2023, 12, 20)),
    Produto(4, "Abacaxi", 3.0, 12, datetime.date(2023, 12, 28)),
    Produto(5, "Laranja", 2.0, 20, datetime.date(2023, 12, 15))
]

class Estoque:

    def __init__(self):
        self.__produtos = data
        self.ordenar_estoque(self.__produtos)

    def __repr__(self):
        linhas = ["{:<3} | {:<10} | {:<9} | {:<10} | {:<10}".format(
            "ID", "Produto", "Valor", "Quantidade", "Data")]
        linhas.append("-" * 55)

        for produto in self.__produtos:
            id = produto.get_id()
            nome = produto.get_nome()
            valor = produto.get_valor()
            quantidade = produto.get_quantidade()
            data = produto.get_data_de_vencimento()

            if data is not None and data != "": 
                data = data.strftime("%d/%m/%Y")
            else:
                data = "----------"

            linhas.append("{:<3} | {:<10} | R${:<7.2f} | {:<10} | {:<10}".format(
                id, nome, valor, quantidade, data))

        return "\n".join(linhas)

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            produto.set_id(len(self.__produtos)+1)
            self.__produtos.append(produto)
            self.ordenar_estoque(self.__produtos)

    def ordenar_estoque(self, produtos):
        if len(produtos) > 1:
            mid = len(produtos) // 2
            left = produtos[0:mid]
            right = produtos[mid:]

            self.ordenar_estoque(left)
            self.ordenar_estoque(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].get_nome() <= right[j].get_nome():
                    produtos[k] = left[i]
                    i += 1
                else:
                    produtos[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                produtos[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                produtos[k] = right[j]
                j += 1
                k += 1

    def listar_produtos(self):
        return self.__repr__()

    def buscar_produto(self, id, inicio=0, fim=None):
        for produto in self.__produtos:
            if produto.get_id() == id:
                return produto

        if fim is None:
            fim = len(self.__produtos) - 1

        if inicio > fim:
            # O produto não foi encontrado
            return None

        meio = (inicio + fim) // 2
        produto_meio = self.__produtos[meio]
        id_meio = produto_meio.get_id()

        if id == id_meio:
            # Produto encontrado
            return produto_meio
        elif id < id_meio:
            # Busca na metade à esquerda
            return self.buscar_produto(id, inicio, meio - 1)
        else:
            # Busca na metade à direita
            return self.buscar_produto(id, meio + 1, fim)

    def atualizar_produto(self, id, nome=None, valor=None, quantidade=None, data_de_vencimento=None):
        produto = self.buscar_produto(id)
        if nome is not None: produto.set_nome(nome)
        if valor is not None: produto.set_valor(valor)
        if quantidade is not None: produto.set_quantidade(quantidade)
        if data_de_vencimento is not None: produto.set_data_de_vencimento(data_de_vencimento)

    def excluir_produto(self, id):
        produto = self.buscar_produto(id)

        if produto is not None:
            self.__produtos.remove(produto)
            print(f"Produto com ID {id} excluído com sucesso.")
        else:
            print(f"Produto com ID {id} não encontrado.")
