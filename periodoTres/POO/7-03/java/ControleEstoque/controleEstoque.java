public class controleEstoque {
    public static void main(String[] args) {
        Produto produto1 = new Produto ("Lego Velozes e Furiozos - Nissan GT R34 ", 15);
        Produto produto2 = new Produto ("Lego Velozes e Furiozos - Toyota Supra", 12);

        produto1.detalhes();
        produto2.detalhes();
        produto2.atualizarEstoque(19);
        produto1.atualizarEstoque(17);
        produto1.detalhes();
        produto2.detalhes();
    }
}

class Produto {
    private String nome;
    private int estoque;

    public Produto(String nome, int quantidadeEstoque) {
        this.nome = nome;
        this.estoque = quantidadeEstoque;
    }

    public void detalhes() {
        System.out.println("Produto: " + nome + "\nQuantidade: " + estoque);
    }

    public void atualizarEstoque(int novoEstoque) {
        this.estoque = novoEstoque;
    }
}