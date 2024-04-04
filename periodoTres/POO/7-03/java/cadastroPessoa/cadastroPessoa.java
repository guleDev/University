// Classe principal que contém o método main (ponto de entrada do programa)
public class cadastroPessoa {
    public static void main(String[] args) {
        // Criando objetos (intâncias) da classe Pessoa
        Pessoa pessoa1 = new Pessoa ("Alice", 25);
        Pessoa pessoa2 = new Pessoa ("Bob", 30);

        // Vhamando método da classe Pessoa para apresentar as informações
        pessoa1.apresentar();
        pessoa2.apresentar();
    }
}

// Definição da classe Pessoa
class Pessoa {
    // Atributos privados da classe Pessoa
    private String nome;
    private int idade;

    // Construtor da classe Pessoa que é chamado ao criar uma nova instância
    public Pessoa(String nome, int idade) {
        // Inicializando os atributos com os valores passados como argumento
        this.nome = nome;
        this.idade = idade;
    }

    // Método da classe Pessoa para apresentar informações
    public void apresentar() {
        // Imprime uma mensagem formatada com o nome e idade da pessoa
        System.out.println("Olá, meu nome é " + nome + " e tenho " + idade + " anos.");
    }

    // Método getter para obter o nome
    public String getNome() {
        return nome;
    }

    // Método setter para definir um novo nome
    public void setNome(String novoNome) {
        nome = novoNome;
    }
}
