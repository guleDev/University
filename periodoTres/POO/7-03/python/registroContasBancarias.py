class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def printSaldo(self):
        print(f"O saldo do titular {self.titular} é de {self.saldo}")

conta1 = ContaBancaria("Gustavo", 1000)
conta1.deposito(1500)
conta1.printSaldo()
