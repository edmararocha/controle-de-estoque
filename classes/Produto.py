from datetime import datetime

class Produto:
    def __str__(self):
        return f"Nome: {self.__nome}\nValor: {self.__valor}\nQtd: {self.__quantidade}\nData de Vencimento: {self.__data_de_vencimento}"

    def __repr__(self):
        return f"Nome: {self.__nome}\nValor: {self.__valor}\nQtd: {self.__quantidade}\nData de Vencimento: {self.__data_de_vencimento}"

    def __init__(self, id=None, nome=None, valor=None, quantidade=None, data_de_vencimento=None):
        self.__id = id
        self.__nome = nome
        self.__valor = valor
        self.__quantidade = quantidade
        self.__data_de_vencimento = data_de_vencimento

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = self.validar_valor(valor)

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = self.validar_quantidade(quantidade)

    def get_data_de_vencimento(self):
        return self.__data_de_vencimento

    def set_data_de_vencimento(self, data_de_vencimento):
        self.__data_de_vencimento = self.validar_data(data_de_vencimento)

    def validar_quantidade(self, quantidade):
        while True:
            try:
                quantidade = int(quantidade)
                if quantidade >= 0:
                    return quantidade
            except ValueError:
                quantidade = input(
                    "Por favor, digite um valor inteiro válido: ")

    def validar_valor(self, valor):
        while True:
            try:
                valor = float(valor) or int(valor)
                return valor
            except ValueError:
                valor = input("Por favor, digite um valor válido: ")                

    def validar_data(self, data):
        while True:
            try:
                if data is not None:
                    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
                    data_atual = datetime.now().date()
                    if data_formatada > data_atual:
                        return data_formatada
                    else:
                        data = input("Por favor, digite uma data posterior à data atual. ")
                else:
                    return None
            except ValueError:
                data = input("Por favor, digite a data em um formato válido. (Ex: 20/10/2024) ")
