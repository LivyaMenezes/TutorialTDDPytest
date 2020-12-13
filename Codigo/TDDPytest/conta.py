from saldo_insuficiente_exception import SaldoInsuficienteException

class Conta:

   def __init__(self, saldo):
       self.saldo = saldo

   def consultar_saldo(self):
       return self.saldo

   def deposito(self, valor):
       self.saldo = self.saldo + valor

   def saque(self, valor):
       if self.saldo >= valor:
           self.saldo = self.saldo - valor
       else:
           raise SaldoInsuficienteException("Você não possui saldo suficiente")