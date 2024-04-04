public class Animal {
    private String tipo;
    private String cor;
    private String somPadrao;
    private String comida;
    private String producao;

    public Animal(String tipo, String cor, String somPadrao, String comida, String producao) {
        this.tipo = tipo;
        this.cor = cor;
        this.somPadrao = somPadrao;
        this.comida = comida;
        this.producao = producao;
    }

    public void som() {
        System.out.println("Som padrão: " + somPadrao);
    }

    public void producao(){
        System.out.println("Produção: " + producao);
    }

    public void comida(){
        System.out.println("Comida: " + comida);
    }

    public void exibirInfo(){
        System.out.println("Tipo: " + tipo);
        System.out.println("Cor: " + cor);
        System.out.println();
    }

    public static void main(String[] args) {
        Animal meuCachorro = new Animal("Mamíferro", "Marrom", "Au au!", "Ração, Churrasco", "Sem Produção");
        meuCachorro.som();
        meuCachorro.comida();
        meuCachorro.producao();
        meuCachorro.exibirInfo();

        Animal minhaAbelha = new Animal("Invertebrado", "Amarela e Preta", "Zumbido", "Polem", "Mel");
        minhaAbelha.som();
        minhaAbelha.comida();
        minhaAbelha.producao();
        minhaAbelha.exibirInfo();
    }
}