class Livro:
    def __init__(self, titulo, autor, numeroDePaginas):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas

    def detalhesLivro(self):
        print(f"O livro {self.titulo} do autor {self.autor} tem {self.numeroDePaginas} páginas")

livro1 = Livro("Diario de um Banana", "Jeff Kinney", 50)
livro1.detalhesLivro()