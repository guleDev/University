public class Pessoa {
    private String nome;
    private String sobrenome;
    private int idade;
    private double altura;
    private boolean trabalha;

    // Construtor da classe
    public Pessoa(String nome, String sobrenome,int idade, double altura, boolean trabalha) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = idade;
        this.altura = altura;
        this.trabalha = trabalha;
    }
    
    // Método para exibir informações da pessoa
    public void exibirInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Sobrenome: " + sobrenome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
        System.out.println("Está trabalhando: " + trabalha);
        System.out.println();
    }

    public static void main(String[] args) {
        // Criando duas instâncias da classe Pessoa
        Pessoa pessoa1 = new Pessoa("João", "Kleber", 30, 1.78, true);
        Pessoa pessoa2 = new Pessoa("Maria", "Clara", 25, 1.65, false);
    
        // Chamando o método exibirInfo() para cada instâncica
        pessoa1.exibirInfo();
        pessoa2.exibirInfo();
    }
}
