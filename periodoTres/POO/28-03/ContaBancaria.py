class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def exibir_info(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.2f}'
    
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def exibir_info(self):
        return f'Conta Corrente - {super().exibir_info()}, Limite: R${self.limite:.2f}'
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        self.juros = juros

    def exibir_info(self):
        return f'Conta Poupanca - {super().exibir_info()}, Juros: {self.juros}%'

#Exemplo de uso
corrente1 = ContaCorrente('João', 5000.00, 1000.00)
print(corrente1.exibir_info())

poupanca1 = ContaPoupanca('Maria', 10000.00, 2.5)
print(poupanca1.exibir_info())
