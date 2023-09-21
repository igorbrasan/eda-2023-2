class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.vetor = [None] * tamanho
        self.topo_pilha1 = -1
        self.topo_pilha2 = tamanho
    
    def empilhar(self,pilha,valor):

