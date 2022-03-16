
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

    def autorization(self, valor):
        if self.__saldo + self.__limite - valor < 0:
            return False
        else:
            return True

    def saque(self, valor):
        if self.autorization(valor):
            self.__saldo -= valor
        else:
            print('Valor não disponível')

    def deposito(self, valor):
        self.__saldo += valor
    
    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
    @property
    def numero(self):
        return self.__numero
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

