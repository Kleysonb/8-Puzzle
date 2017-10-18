from random import *
from turtle import *
from freegames import floor, vector
import time


tiles = {}
neighbors = [
    vector(100, 0), #Direita
    vector(-100, 0), #Esquerda
    vector(0, 100), #Sobir
    vector(0, -100) #Descer
]

telhas = [
    vector(-200, 0),        #1
    vector(-100, 0),        #2
    vector(0, 0),           #3
    vector(-200, -100),     #4
    vector(-100, -100),     #5
    vector(0, -100),        #6
    vector(-200, -200),     #7
    vector(-100, -200),     #8
    vector(0, -200)         #none
]


#-------------------------------------------------------------------------------------------------------------#
#                                           Algoritmo Genetico                                                #

populacao = []
#cromossomo = []
elitizacao = []

#Gerar Populacao
def gerarPopulacao(num):
    #populacao = []
    for pessoa in range(num):
        cromossomo = []
        for cromo in range(30):
            #Definindo Movimentos Aleatorios
            movimento = choice([1,2,3,4])
            cromossomo.append(movimento)
        populacao.append(cromossomo)

    #print populacao[0]
    #print calcularFitness(populacao[0])
    '''
    print populacao[0]
    print calcularFitness(populacao[0])
    print "--------------------------------------------"
    print populacao[1]
    print calcularFitness(populacao[1])
    print "--------------------------------------------"
    print populacao[2]
    print calcularFitness(populacao[2])
    print "--------------------------------------------"
    print populacao[3]
    print calcularFitness(populacao[3])
    print "--------------------------------------------"
    '''
    print "--------------------------------------------"
    for pessoa in range(len(populacao)):
        print calcularFitness(populacao[pessoa])
    print "--------------------------------------------"
    for pessoa in range(len(populacao)):
        print calcularFitness(populacao[pessoa])
    print "--------------------------------------------"
    for pessoa in range(len(populacao)):
        print calcularFitness(populacao[pessoa])
    print "--------------------------------------------"
    #selecionarElite()

def selecionarElite():
    #print range(len(populacao))
    
    for elite in range(8):
        populacaoAux = populacao
        fitnessAuxiliar = 0
        indice = 0
        for pessoa in range(len(populacaoAux)):
            aux = calcularFitness(populacaoAux[pessoa])
            if aux > fitnessAuxiliar:
                fitnessAuxiliar = aux
                indice = pessoa
        
        print 'removeu'
        print indice
        populacaoAux.pop(indice)

        
    for pessoa in range(len(populacaoAux)):
        print populacaoAux[pessoa]
        print calcularFitness(populacaoAux[pessoa])
    print "--------------------------------------------"

#Funcao Fitness
def calcularFitness(cromo):
    auxiliar = tiles
    #fitness = 0
    for item in range(30):    
        x = cromo[item]
        #time.sleep(0.300)
        #change(x)
        if x == 1:
            #Direita
            #print 'direita'
            neighbor = neighbors[0]
        elif x == 2:
            #Esquerda
            #print 'esquerda'
            neighbor = neighbors[1]
        elif x == 3:
            #Sobir
            #print 'sobir'
            neighbor = neighbors[2]
        elif x == 4:
            #Descer
            #print 'descer'
            neighbor = neighbors[3]

    movimento = False
    for telha in auxiliar:
        spot = telha + neighbor

        if spot in auxiliar and auxiliar[spot] is None:
            number = auxiliar[telha]
            auxiliar[telha] = None
            auxiliar[spot] = number
            movimento = True
            break
    '''if not movimento:
        print 'movimento invalido'
        #fitness-=1'''

    return foraDoLugar(auxiliar)
    

def foraDoLugar(auxiliar):
    posicao = vector(-200, 0)
    fitness = 0;
    if auxiliar[posicao] != 1:
        fitness+=1
    posicao = vector(-100, 0)
    if auxiliar[posicao] != 2:
        fitness+=1
    posicao = vector(0, 0)
    if auxiliar[posicao] != 3:
        fitness+=1
    posicao = vector(-200, -100)
    if auxiliar[posicao] != 4:
        fitness+=1
    posicao = vector(-100, -100)
    if auxiliar[posicao] != 5:
        fitness+=1
    posicao = vector(0, -100)
    if auxiliar[posicao] != 6:
        fitness+=1
    posicao = vector(-200, -200)
    if auxiliar[posicao] != 7:
        fitness+=1
    posicao = vector(-100, -200)
    if auxiliar[posicao] != 8:
        fitness+=1
    posicao = vector(0, -200)
    if auxiliar[posicao] != None:
        fitness+=1
    
    return fitness

#-------------------------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------------------------#
#                                            Montagem do Jogo                                                 #

def load():
    #Carregar telhas e arrumar
    count = 1

    for y in range(-200, 100, 100):
        for x in range(-200, 100, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    #Criar Aleatoriedade
    '''
    for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor
    
        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot
    '''

def square(mark, number):
    #Desenhe o quadrado branco com contorno e numero preto
    up()
    goto(mark.x, mark.y)
    down()

    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(99)
        left(90)
    end_fill()

    if number is None:
        return
    elif number < 10:
        forward(20)

    write(number, font=('Arial', 60, 'normal'))

def tap(x, y):
    #Troque a telha e o quadrado vazio
    print x
    print y
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)
    print mark
    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)
    #print tiles

def change(x):
    if x == 1:
        #Direita
        neighbor = neighbors[0]
    elif x == 2:
        #Esquerda
        neighbor = neighbors[1]
    elif x == 3:
        #Sobir
        neighbor = neighbors[2]
    elif x == 4:
        #Descer
        neighbor = neighbors[3]

    movimento = False
    for telha in telhas:
        spot = telha + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[telha]
            tiles[telha] = None
            square(telha, None)

            tiles[spot] = number
            square(spot, number)
            
            movimento = True
            break
    if not movimento:
        print 'movimento invalido'

def draw():
    #Desenhe todos os azulejos
    for mark in tiles:
        square(mark, tiles[mark])
    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

load()
draw()

listen()
onkey(lambda: change(1), 'Right')
onkey(lambda: change(2), 'Left')
onkey(lambda: change(3), 'Up')
onkey(lambda: change(4), 'Down')
onkey(lambda: gerarPopulacao(12), 'g')


#onscreenclick(tap)
done()
#-------------------------------------------------------------------------------------------------------------#