def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numer":numero,
        "titular":titular,
        "saldo":saldo,
        "limite":limite
    }
    return conta

def deposito(conta, valor):
    conta['saldo'] += valor

def saque(conta, valor):
    if (conta['saldo'] - valor) < 0:
        print('Valor não disponível')
    else:
        conta['saldo'] -= valor

def saldo(conta):
    print("Saldo disponível: {}".format(conta['saldo']))