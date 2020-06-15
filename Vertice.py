"""
Classe Vertice
"""

class Vertice:
    # inicializa o vertice
    def __init__(self,indice,valor):
        self.indice = indice
        self.valor = valor
        self.adjacentes = []
        self.grauSaturacao = 0
        self.grau = 0

    # calcula o valor de saturacao do vertice
    def calculaSaturacao(self):
        for adjacente in self.adjacentes:   # percorre os vertices adjacentes
            if adjacente.getvalor() != "N": # caso o vertice esteja colorido
                self.grauSaturacao += 1     # aumenta o grau de saturacao

    def getvalor(self):
        return self.valor

    def setvalor(self,valor):
        self.valor = valor

    def aumentaSaturacao(self):
        self.grauSaturacao += 1

    def diminuiSaturacao(self):
        self.grauSaturacao -= 1

    def getSaturacao(self):
        return self.grauSaturacao

    # adiciona um vertice ao vetor de adjacentes
    def addAdjacente(self,vertice):
        self.adjacentes.append(vertice)
        self.grau += 1

    # encontra as cores possiveis para o vertice
    def cores(self,ordem):
        possibilidades = list(range(1,ordem+1))          # todas as cores possiveis
        setPossibilidades = set(possibilidades)
        jaExiste = set()
        for adjacente in self.adjacentes:                # percorre os vertices adjacentes
            if adjacente.getvalor() != "N":              # caso o vertice adjacente esteja colorido
                jaExiste.add(int(adjacente.getvalor()))  # guarda a cor q ja existe
        setPossibilidades = setPossibilidades - jaExiste # tira as cores ja usadas das cores possiveis
        if (len(setPossibilidades) == 0):                # caso nao sobre nenhuma cor
            return -1                                    # retorna -1
        return list(setPossibilidades)                   # retorna as cores possiveis

    # aumenta a saturacao de todos os vertices adjacentes
    def aumentaSaturacaoAdjacentes(self):
        for adjacente in self.adjacentes:
            adjacente.aumentaSaturacao()

    # diminui a saturacao de todos os vertices adjacentes
    def diminuiSaturacaoAdjacentes(self):
        for adjacente in self.adjacentes:
            adjacente.diminuiSaturacao()