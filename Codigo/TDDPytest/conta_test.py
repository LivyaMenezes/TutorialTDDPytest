import pytest
from conta import Conta
from saldo_insuficiente_exception import SaldoInsuficienteException

def test_consulta_saldo():
    conta = Conta(100)
    assert conta.consultar_saldo() == 100

def test_deposito():
    conta = Conta(100)
    conta.deposito(10)
    assert conta.consultar_saldo() == 110

def test_saque():
    conta = Conta(100)
    conta.saque(10)
    assert conta.consultar_saldo() == 90

def test_saque_exception():
    conta = Conta(100)
    with pytest.raises(SaldoInsuficienteException):
           conta.saque(500)