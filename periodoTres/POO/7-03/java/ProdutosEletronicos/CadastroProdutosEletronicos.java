public class CadastroProdutosEletronicos {
    public static void main(String[] args) {
        ProdutosEletronicos produto1 = new ProdutosEletronicos ("celular", "motorola", 1500);

        produto1.detalhes();
    }    
}

class ProdutosEletronicos {
    private String nome;
    private String marca;
    private float preco;

    public ProdutosEletronicos(String nome, String marca, float preco) {
        this.nome = nome;
        this.marca = marca;
        this.preco = preco;
    }

    public void detalhes() {
        System.out.println("Produto: " + nome + "\nMarca: " + marca + "\nPreco: " + preco);
    }
}