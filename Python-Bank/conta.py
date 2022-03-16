
from operator import truediv


class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo disponível: {}".format(str(self.__saldo)))

    def saldo_disponivel(self, valor):
        if self.__saldo - valor < 0:
            return False
        else:
            return True

    def saque(self, valor):
        if self.saldo_disponivel(valor):
            self.__saldo -= valor
        else:
            print('Valor não disponível')

    def deposito(self, valor):
        self.__saldo += valor
    
    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor

