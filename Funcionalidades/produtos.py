
class Produtos:
    def __init__(self, nome_produto='', preco_produto=0.0, tamanho='', tipo='', cor ='', quantidade = 0):
        self.nome_produto = nome_produto
        self.preco_produto = float(preco_produto)
        self.tamanho = tamanho
        self.tipo = tipo
        self.cor = cor
        self.quantidade = int(quantidade)

    def __str__(self):
        return f'Produto: {self.nome_produto} | Valor: R$ {self.preco_produto:.2f} | Tamanho: {self.tamanho} | Tipo: {self.tipo} | Cor: {self.cor} | Quantidade: {self.quantidade}'

class Blusas(Produtos):
    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', material='', quantidade=0):
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade)
        self.material = material

    def __str__(self):
        return super().__str__() + f' | Material: {self.material}'

class Calcas(Produtos):
    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', modelo='', quantidade=0):
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade)
        self.modelo = modelo

    def __str__(self):
        return super().__str__() + f' | Modelo: {self.modelo}'

class Sapatos(Produtos):
    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', estilo='', quantidade=0):
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade)
        self.estilo = estilo

    def __str__(self):
        return super().__str__() + f' | Estilo: {self.estilo}'



blusa1 = Blusas('blusa cropped', 65.90, 'M, P e G', 'casual', 'preta', 'Algodão', 20)
blusa2 = Blusas('blusa Estampada', 78.49, 'M e G', 'praiana', 'colorida', 'Esportiva', 20)
blusa3 = Blusas('blusa Social', 149.99, 'M, G, P', 'social', 'azul e preta', 'Seda', 20)
blusa4 = Blusas('blusa lisa', 55.90, 'GG, M, G, P, PP','casual', 'azul, branca, vermelha, preta', 'Algodão', 20)

calca1 = Calcas('calça jeans', 120.00, 'P, M, G', 'casual', 'azul', 'Jeans', 20)
calca2 = Calcas('calca moletom', 98.90, 'M, G, GG', 'esportiva', 'cinza', 'Moletom', 20)
calca3 = Calcas('calça social', 140.00, 'P, M, G, GG', 'social', 'preta', 'Poliéster', 20)
calca4 = Calcas('calça legging', 75.50, 'PP, P, M, G', 'fitness', 'preta e cinza', 'Elastano', 20)

sapato1 = Sapatos('tenis esportivo', 210.00, '39, 40, 41, 42', 'esportivo', 'preto e vermelho', 'Sintético', 20)
sapato2 = Sapatos('sandalia rasteira', 89.90, '35, 36, 37, 38, 39', 'casual', 'bege', 'Couro', 20)
sapato3 = Sapatos('sapato social', 299.90, '39, 40, 41, 42, 43', 'social', 'preto', 'Couro legítimo', 20)
sapato4 = Sapatos('bota', 259.00, '36, 37, 38, 39, 40, 41', 'casual', 'marrom', 'Camurça', 20)

blusas = [blusa1, blusa2, blusa3, blusa4]
calcas = [calca1, calca2, calca3, calca4]
sapatos = [sapato1, sapato2, sapato3, sapato4]
