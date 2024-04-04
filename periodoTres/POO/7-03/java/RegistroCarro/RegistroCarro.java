public class RegistroCarro {
    public static void main(String[] args) {
        Carro carro1 = new Carro("Honda Civic", "Amarelo", 1998);

        carro1.detalhes();
    }
}

class Carro {
    private String modelo;
    private String cor;
    private int ano;

    public Carro(String modelo, String cor, int ano) {
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
    }

    public void detalhes() {
        System.out.println("Carro: " + modelo + "\nCor: " + cor + "\nAno: " + ano);
    }
}