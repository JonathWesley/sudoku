"""
Enunciado: Resolver o problema do Sudoku, utilizando coloração de grafos
Disciplina: Grafos
Professor: Rudimar
Alunos: Jonath e Matheus
"""

from Grafo import Grafo
import turtle

def retornaCor(numero):
    cores = {
        1: "#404040",
        2: "green",
        3: "blue",
        4: "fuchsia",
        5: "orange",
        6: "yellow",
        7: "lime",
        8: "maroon",
        9: "navy",
        10: "olive",
        11: "purple",
        12: "red",
        13: "silver",
        14: "teal",
        15: "white",
        16: "aqua"}
    
    return cores.get(numero, "black")

def draw_board(dimension, x_coord, y_coord, side, sudoku):
    i = 0
    for vertices in sudoku.vertices:
        
        if i % dimension == 0:
            y_coord -= side
            turtle.penup()
            turtle.setpos(x_coord, y_coord)
            turtle.pendown()
                
        turtle.fillcolor(retornaCor(sudoku.vertices[vertices].getvalor()))
        turtle.begin_fill()
        
        for j in range(4):
            if j == 3:
                turtle.write(" "+str(sudoku.vertices[vertices].getvalor()),align='left',font=('Arial',25,'normal'))
            turtle.forward(side)
            turtle.right(90)
            
        turtle.end_fill()
            
        turtle.forward(side)
        
        i += 1

if __name__ == "__main__":
    sair = "n"
    while sair == "n":
        ordem = int(input("Ordem do sudoku: "))
        while ordem != 2 and ordem != 4 and ordem != 9 and ordem != 16:
            print("Ordem deve possuir uma raiz quadrada inteira.")
            ordem = int(input("Ordem do sudoku: "))
            
        verticeInicial = int(input("Vertice inicial: "))
        while verticeInicial < 0 or verticeInicial >= (ordem*ordem):
            print("Vertice deve estar entre 0 e " + str(ordem*ordem-1) + ".")
            verticeInicial = int(input("Vertice inicial: "))
        
        vertices = (ordem*ordem) * ['N']
        vertices[verticeInicial] = 1
        sudoku = Grafo(vertices)
        sudoku.dSatur()
        sudoku.mostraGrafo()
        
        turtle.speed(0)

        turtle.pensize(5)

        draw_board(ordem, -470, 450, 50, sudoku)
        
        turtle.done()
        
        sair = input("Deseja sair? s/n: ")
