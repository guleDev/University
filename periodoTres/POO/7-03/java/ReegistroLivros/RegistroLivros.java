public class RegistroLivros {
    public static void main(String[] args) {
        Livro livro1 = new Livro ("Diario de um Banana", "Jeff Kinney", 50);
        Livro livro2 = new Livro ("Diario de um Banana 2", "Jeff Kinney", 60);

        livro1.detalhes();
        livro2.detalhes();
    }    
}

class Livro {
    private String titulo;
    private String autor;
    private int nPaginas;

    public Livro(String titulo, String autor, int nPaginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.nPaginas = nPaginas;
    }

    public void detalhes(){
        System.out.println("Titulo: " + titulo + "\nAutor: " + autor + "\nPáginas: " + nPaginas);
    }
}