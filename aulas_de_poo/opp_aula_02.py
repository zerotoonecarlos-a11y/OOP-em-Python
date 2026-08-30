# Abstração e Encapsulamento

class conta:
    def __init__(self, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    
    
    @property
    def saldo(self):
        return self.__saldo
    
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
            
            
    def mostrar_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

c = conta(100)  # Criando uma conta com saldo inicial de 100
# c.depositar(50)  # Depósito de 50
# c.sacar(30)  # Saque de 30
c.mostrar_saldo()  # Mostra o saldo atual