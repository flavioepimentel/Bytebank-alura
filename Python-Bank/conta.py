
class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("Saldo disponível: {}".format(str(self.saldo)))

    def saque(self, valor):
        if self.saldo - valor < 0:
            print('Valor não disponível')
        else:
            self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor