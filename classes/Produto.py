class Produto:
    def __repr__(self):
        return str(self.__nome + " | " + self.__valor + " | " + self.__quantidade)

    def __str__(self):
        return f"Nome: {self.__nome}\nValor: {self.__valor}\nQtd: {self.__quantidade}\nPerecível: {self.__perecivel}"

    # def __init__(self):  # data: date
        # self.__nome
        # self.__valor
        # self.__quantidade
        # self.__perecivel
        # self.data = data

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        if self.validar_valor(valor):
            self.__valor = float(valor)

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        if self.validar_quantidade(quantidade):
            self.__quantidade = int(quantidade)

    def get_perecivel(self):
        return self.__perecivel

    def set_perecivel(self, perecivel):
        self.__perecivel = perecivel

    def validar_quantidade(self, quantidade):
        while True:
            try:
                quantidade = int(quantidade)
                if quantidade >= 0:
                    return True
            except ValueError:
                quantidade = input("Por favor, digite um valor inteiro válido: ")

    def validar_valor(self, valor):
        while True:
            try:
                valor = float(valor) or int(valor)
                return True
            except ValueError:
                valor = input("Por favor, digite um valor válido: ")

    # def get_data(self):
    #     return self.data

    # def set_data(self, data):
    #     self.data = dataclass
