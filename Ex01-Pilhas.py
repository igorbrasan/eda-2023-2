
#A complexidade é O(1), pois as operações de empilhar e desempilhar não dependem do tamanho do vetor.


class Pilha_Dupla:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None] * tamanho
        self.topo_pilha1 = -1
        self.topo_pilha2 = tamanho

    def empilhar(self, pilha, valor):
        if pilha == 1:
            if self.topo_pilha1 < self.topo_pilha2 - 1:
                self.topo_pilha1 += 1
                self.vetor[self.topo_pilha1] = valor
            else:
                print("Pilha 1 está cheia.")
        elif pilha == 2:
            if self.topo_pilha2 > self.topo_pilha1 + 1:
                self.topo_pilha2 -= 1
                self.vetor[self.topo_pilha2] = valor
            else:
                print("Pilha 2 está cheia.")
        else:
            print("Pilha inválida.")

    def desempilhar(self, pilha):
        if pilha == 1:
            if self.topo_pilha1 >= 0:
                valor = self.vetor[self.topo_pilha1]
                self.topo_pilha1 -= 1
                return valor
            else:
                print("Pilha 1 está vazia.")
        elif pilha == 2:
            if self.topo_pilha2 < self.tamanho:
                valor = self.vetor[self.topo_pilha2]
                self.topo_pilha2 += 1
                return valor
            else:
                print("Pilha 2 está vazia.")
        else:
            print("Pilha inválida.")

pilha_dupla = Pilha_Dupla(10)
pilha_dupla.empilhar(1, 5)
pilha_dupla.empilhar(2, 10)
pilha_dupla.empilhar(1, 15)
pilha_dupla.empilhar(2, 20)

print(pilha_dupla.desempilhar(1)) 
print(pilha_dupla.desempilhar(2))  


p2 = Pilha_Dupla(6)
p2.empilhar(1,3)
p2.empilhar(2,2)
p2.empilhar(2,3)
p2.empilhar(2,5)
p2.empilhar(2,6)
p2.empilhar(2,9)
print(p2.empilhar(2,0))

