class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quantidade):
        if quantidade > 0:
            self.saldo += quantidade
            print("Foi depositado: ", quantidade)
        else:
            print("Erro no deposito")


    def consulta_saldo(self):
        return self.saldo

    def sacar(self, quantidade):
        if self.saldo - quantidade < self.limite:
            print("Saldo insuficiente")
        else:
          self.saldo -= quantidade
          print("Foi sacado: ", quantidade)
