class Produto:

    def __init__(self, nome, quantidadeEmEstoque):
        self.nome = nome
        self.quantidadeEmEstoque = quantidadeEmEstoque

    def modificarEstoque(self, novaQuantidadeEmEstoque):
        self.quantidadeEmEstoque = novaQuantidadeEmEstoque

    def infoProduto(self):
        print(f"O item {self.nome} tem {self.quantidadeEmEstoque} unidade em estoque.")

produto1 = Produto("Pão", 25)
produto1.infoProduto()
produto1.modificarEstoque(15)
produto1.infoProduto()
