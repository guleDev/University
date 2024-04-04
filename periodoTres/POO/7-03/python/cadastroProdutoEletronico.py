class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def produtoInfos(self):
        print(f"o produto {self.nome} da marca {self.marca} custa {self.preco}")

produto1 = ProdutoEletronico("celular", "motorola", 1500)
produto1.produtoInfos()