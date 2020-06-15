"""
Classe Grafo
"""

import math
from Vertice import Vertice

class Grafo:
    # inicializa o grafo a partir de uma lista com o valor de cada vertice
    def __init__(self,vertices):
        self.numeroDeVertices = len(vertices)
        self.vertices = self.geraVertices(vertices,self.numeroDeVertices)
        self.ordem = int(math.sqrt(self.numeroDeVertices))
        self.dimensaoQuadro = int(math.sqrt(self.ordem))
        self.quadros = self.geraQuadros(self.numeroDeVertices, self.dimensaoQuadro, self.ordem)
        self.todosAdjacentes(self.ordem)
    
    # cria vertices
    def geraVertices(self,listaVertices,numeroDeVertices):
        vertices = {}                                       # cria lista para armazenar todos os vertices
        for i in range(numeroDeVertices):   
            vertices[i] = Vertice(i,listaVertices[i])       # inicializa cada vertice com seu respectivo indice e valor, e adiciona o mesmo na lista
        return vertices                                     # retorna a lista de vertices
     
    # cria os quadros do sudoku 
    def geraQuadros(self,numeroDeVertices,dimensaoQuadro,ordem):
        listaQuadros = []                                                                                                # cria uma lista para armazenar todos os quadros
        for primeiroQuadroVertical in range (0,numeroDeVertices,dimensaoQuadro*ordem):                                   # percorre os quadros verticalmente 
            for primeiroQuadroHorizontal in range(primeiroQuadroVertical, primeiroQuadroVertical+ordem, dimensaoQuadro): # percorre os quadros horizontalmente
                quadro = set()                                                                                           # cria um set para o quadro (individual)
                for vertical in range(primeiroQuadroHorizontal,primeiroQuadroHorizontal + ordem*dimensaoQuadro-1,ordem): # percorre os vertices verticalmente dentro do quadro
                    for horizontal in range(vertical,vertical+dimensaoQuadro):                                           # percorre os vertices horizontalmente dentro do quadro
                        quadro.add(horizontal)                                                                           # adiciona o vertice ao quadro
                listaQuadros.append(quadro)                                                                              # adiciona o quadro a lista de quadros
        return listaQuadros                                                                                              # retorna a lista de quadros

    # encontra os vertices adjacentes por linha
    def linhaAdjacentes(self,indice,ordem): 
        limSuperior = indice + (ordem - (indice % ordem)) # define ate onde a linha vai
        limInferior = indice - (indice % ordem)           # define onde a linha comeca

        adjacentes = set()                                # cria um set de adjacentes
        for i in range(limInferior,limSuperior):
            adjacentes.add(i)                             # adiciona todos os adjacentes dentro dos limites da linha
        return adjacentes

     # encontra os vertices adjacentes por coluna
    def colunaAdjacentes(self,indice,ordem):
        adjacentes = set()                                          # cria um set de adjacentes
        for subindo in range(indice,0,-ordem):
            adjacentes.add(subindo)                                 # adiciona todos os adjacentes acima
        for descendo in range(indice,self.numeroDeVertices,ordem):
            adjacentes.add(descendo)                                # adiciona todos os adjacentes abaixo
        return adjacentes
    
    # encontra os vertices adjacentes por quadro 
    def quadroAdjacentes(self,indice):
        for quadro in self.quadros:     # percorre todos os quadros
            if indice in quadro:        # se o vertice esta no quadro
                return quadro           # retorna o quadro

    # encontra todos os vertices adjacentes ( junta linha, coluna e quadro)
    def todosAdjacentes(self,ordem):
        for vertice in self.vertices:                                           # percorres todos os vertices
            linhaAdjacentes = self.linhaAdjacentes(vertice,ordem)               # pega as linhas adjacentes
            colunaAdjacentes = self.colunaAdjacentes(vertice,ordem)             # pega as colunas adjacentes
            quadroAdjacentes = self.quadroAdjacentes(vertice)                   # pega os quadros adjacentes
            adjacentes = linhaAdjacentes | colunaAdjacentes | quadroAdjacentes  # junta ambos
            self.adicionaAdjacentes(vertice,adjacentes)                         # aloca todos os vertices adjacentes

    # aloca todos os vertices adjacentes
    def adicionaAdjacentes(self,vertice,adjacentes):
        for adjacente in adjacentes:                                            # percorres todos os vertices
            if (vertice != adjacente):                                          
                self.vertices[vertice].addAdjacente(self.vertices[adjacente])   # adiciona o vertice adjacente para a lista de vertices adjacentes
        self.vertices[vertice].calculaSaturacao()                               # calcula a saturacao do vertice

    # encontra o vertice de maior saturacao
    def maiorSaturacao(self):
        maiorSaturacao = 0
        maiorIndice = 0
        for vertice in self.vertices:                                                                               # percorre todos os vertices
            if self.vertices[vertice].getSaturacao() > maiorSaturacao and self.vertices[vertice].getvalor() == "N": # se a saturacao for maior e o vertice nao for colorido
                maiorSaturacao = self.vertices[vertice].getSaturacao()                                              # atualiza os valores
                maiorIndice = vertice
        return maiorIndice                                                                                          # retorna o indice do vertice com maior saturacao

    # verifica se todos os vertices estao coloridos
    def todosColoridos(self):
        for vertice in self.vertices:
            if self.vertices[vertice].getvalor() == "N":
                return False
        return True

    # algoritmo de coloracao dSatur
    def dSatur(self):
        if self.todosColoridos():                                           # se todos os vertices estao coloridos
            return True                                                     # retorna verdadeiro
        maiorSaturacao = self.maiorSaturacao()                              # pega o vertice com maior saturacao
        coresPossiveis = self.vertices[maiorSaturacao].cores(self.ordem)    # pega as cores possiveis para este vertice
        if coresPossiveis == -1:                                            # se nao existem cores possiveis
            return False                                                    # retorna falso
        if not coresPossiveis:
            return False
        for cor in coresPossiveis:                                          # percorre as cores possiveis
            self.vertices[maiorSaturacao].setvalor(cor)                     # adiciona a cor para o vertice
            self.vertices[maiorSaturacao].aumentaSaturacaoAdjacentes()      # aumenta a saturacao dos vertices adjacentes
            if self.dSatur():                                               # repete o algoritmo
                return True
            else:                                                           # caso receba um retorno falso
                self.vertices[maiorSaturacao].diminuiSaturacaoAdjacentes()  # diminui a saturacao dos vertices adjacentes
                self.vertices[maiorSaturacao].setvalor("N")                 # tira a cor do vertice
        return False

    # exibe o grafo
    def mostraGrafo(self):
        for vertices in self.vertices:                          # percorre todos os vertices
            if(vertices % self.ordem == 0 and vertices != 0):   # caso seja um fim de linha
                print("")                                       # pula a linha
            print(self.vertices[vertices].getvalor(),"",end="") # mostra o valor do vertice