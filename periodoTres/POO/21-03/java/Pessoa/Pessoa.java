public class Pessoa {
    public static void main(String[] args) {
        Pessoas[] pessoas = {new Pessoas("Prof Paulo", 12), new Pessoas("Prof Sandro", 20), new Pessoas("Prof Elton", 35)};

        int indice = 1;
        Pessoas pessoa = pessoas[indice];
        System.out.println("Nome da pessoa no índice " + indice + ": " + pessoa.nome);
        System.out.println("Idade da pessoa no índice " + indice + ": " + pessoa.idade);
    }
}

public class Pessoas {
    String nome;
    int idade;
    
    public Pessoas(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
}
