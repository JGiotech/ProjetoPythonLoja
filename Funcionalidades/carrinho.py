
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_roupas(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            self.itens.append((produto, quantidade))
            produto.quantidade -= quantidade
            print(f"{quantidade} '{produto.nome_produto}' adicionado(s) ao carrinho.\n")
            print(f"Quantidade restante no estoque: {produto.quantidade}\n") 
        else:
            print("Quantidade indisponível no estoque.\n")

    def exibir_itens(self, mostrar_titulo=True):
        if not self.itens:
            print("O carrinho está vazio.")
            return

        if mostrar_titulo:
            print("\n--- Itens no Carrinho ---")

        for produto, quantidade in self.itens:
            print(f"{quantidade} - {produto.nome_produto} | R$ {produto.preco_produto:.2f} cada\n")

    def calcular_total(self):
        return sum(produto.preco_produto * quantidade for produto, quantidade in self.itens)

    def esvaziar(self):
        self.itens.clear()

