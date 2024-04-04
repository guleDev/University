public class RegistroContaBancaria {
    public static void main(String[] args) {
        ContaBancaria conta1 = new ContaBancaria("Gustavo", 1500);
        ContaBancaria conta2 = new ContaBancaria("Paulinho", 2500);

        conta1.extrato();
        conta2.extrato();
        conta1.deposito(5500);
        conta2.deposito(200);
        conta1.extrato();
        conta2.extrato();

    }
}

class ContaBancaria {
    private String titular;
    private int saldo;

    public ContaBancaria(String titular, int saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    public void extrato() {
        System.out.println("Titular: " + titular + "\nSaldo: " + saldo);
    }

    public void deposito(int valorDeposito) {
        this.saldo += valorDeposito;
    }
}