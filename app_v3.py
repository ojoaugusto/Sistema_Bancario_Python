from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        

class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(conta, transacao):
        pass

    def adicionar_conta(conta):
        pass


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def mostrar_saldo(self, saldo):
        self.saldo = saldo

    def nova_conta(self, cliente, numero, conta):
        pass
        

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite


class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass
