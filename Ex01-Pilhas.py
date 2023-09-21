
#Para implementar duas pilhas em um único vetor e fornecer algoritmos para inclusão (empilhar) e exclusão (desempilhar) em ambas as pilhas, 
#você pode usar um vetor e dois índices para rastrear a parte superior de cada pilha. 
#Um índice será para a pilha 1 e o outro para a pilha 2. Aqui estão os algoritmos em Python:


#A complexidade é O(1), pois as operações de empilhar e desempilhar não dependem do tamanho do vetor.
class DuasPilhasEmUmVetor:
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
            return None

# Exemplo de uso
duas_pilhas = DuasPilhasEmUmVetor(10)

duas_pilhas.empilhar(1, 5)
duas_pilhas.empilhar(2, 10)
duas_pilhas.empilhar(1, 15)
duas_pilhas.empilhar(2, 20)

print(duas_pilhas.desempilhar(1))  # Saída: 15
print(duas_pilhas.desempilhar(2))  # Saída: 20
