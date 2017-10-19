from random import *
from turtle import *
from freegames import floor, vector
import time
import copy


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

def algoritmoGenetico(qtd_populacao, geracoes):
    populacao = gerarPopulacao(qtd_populacao)                       # 12 pessoas
    print 'populacao inicial'       
    for item in range(len(populacao)):
        print populacao[item]

    print 'elitizacao inicial'       
    elitizacao = calcularFitnessGlobal(populacao)
    for item in range(len(elitizacao)):
        print elitizacao[item]
    
    for geracao in range(geracoes):
        elitizacao = calcularFitnessGlobal(populacao)
        
        pais = selecionarPais(elitizacao, populacao)                                # 4 pais
        filhos = crossover(pais)                                                    # 4 filhos
        mutantes = mutacao(filhos)                                                  # 2 mutantes
        aleatorios = gerarPopulacao(2)                                              # 2 inidividuos aleatorios
        populacao = gerarNovaPopulacao(pais, filhos, mutantes, aleatorios)          # 12 pessoas
    
    print '--------------------------------------------------------------'
    
    print 'populacao final'       
    for item in range(len(populacao)):
        print populacao[item]
    
    print 'elitizacao final'       
    elitizacao = calcularFitnessGlobal(populacao)
    menorFitnss = elitizacao[0]
    posicao = 0
    for item in range(len(elitizacao)):
        print elitizacao[item]
        if elitizacao[item] < menorFitnss:
            menorFitnss = elitizacao[item]
            posicao = item
    print '--------------------------------------------------------------'
    resolverPuzzle(populacao[posicao])

def gerarNovaPopulacao(pais, filhos, mutantes, aleatorios):
    populacao = []
    for item in pais:
        populacao.append(item)
    for item in filhos:
        populacao.append(item)
    for item in mutantes:
        populacao.append(item)
    for item in aleatorios:
        populacao.append(item)
    return populacao

#Gerar Mutacao
def mutacao(filhos):
    mutantes = []
    
    # Mutacao 1 ->  filho3 : Troca dos valores 10 e 20, 8 e 25, 3 e 9
    mutante1 = filhos[1]

    aux1 = mutante1[10]
    
    aux2 = mutante1[20]
    mutante1[10] = aux2
    mutante1[20] = aux1

    aux1 = mutante1[8]
    aux2 = mutante1[25]
    mutante1[8] = aux2
    mutante1[25] = aux1

    aux1 = mutante1[3]
    aux2 = mutante1[9]
    mutante1[3] = aux2
    mutante1[9] = aux1

    # Mutacao 2 -> filho5: Troca dos valores 5 e 15, 0 e 29, 7 e 19

    mutante2 = filhos[3]

    aux1 = mutante2[5]
    aux2 = mutante2[15]
    mutante2[5] = aux2
    mutante2[15] = aux1

    aux1 = mutante2[0]
    aux2 = mutante2[29]
    mutante2[0] = aux2
    mutante2[29] = aux1

    aux1 = mutante2[10]
    aux2 = mutante2[20]
    mutante2[7] = aux2
    mutante2[19] = aux1
    
    mutantes.append(mutante1)
    mutantes.append(mutante2)

    return mutantes

#Cruzamento
def crossover(pais):
    filhos = []

    #Filho 1
    filho1 = []
    for item in range(15):
        filho1.append(pais[0][item])
    for item in range(15, 30):
        filho1.append(pais[1][item])
    
    #Filho 2
    filho2 = []
    for item in range(15):
        filho2.append(pais[1][item])
    for item in range(15, 30):
        filho2.append(pais[0][item])

    #Filho 3
    filho3 = []
    for item in range(15):
        filho3.append(pais[2][item])
    for item in range(15, 30):
        filho3.append(pais[3][item])

    #Filho 4
    filho4 = []
    for item in range(15):
        filho4.append(pais[3][item])
    for item in range(15, 30):
        filho4.append(pais[2][item])

    filhos.append(filho1)
    filhos.append(filho2)
    filhos.append(filho3)
    filhos.append(filho4)

    return filhos

#Gerar Populacao
def gerarPopulacao(num):
    populacao = []
    for pessoa in range(num):
        cromossomo = []
        for cromo in range(30):
            #Definindo Movimentos Aleatorios
            movimento = choice([1,2,3,4])
            cromossomo.append(movimento)
        populacao.append(cromossomo)
    return populacao

#Selecionar os Pais
def selecionarPais(elitizacao, populacao):
    elitizacaoAux = copy.copy(elitizacao)
    for elite in range(8):
        pais = populacao
        fitnessAuxiliar = 0
        indice = 0
        for pessoa in range(len(elitizacaoAux)):
            aux = elitizacaoAux[pessoa]
            if aux > fitnessAuxiliar:
                fitnessAuxiliar = aux
                indice = pessoa
        pais.pop(indice)
        elitizacaoAux.pop(indice)
    return pais

#Funcao Fitness
def calcularFitnessGlobal(populacao):
    elitizacao = []
    for pessoa in range(len(populacao)):
        #print populacao[pessoa]
        aux = calcularFitness(populacao[pessoa])
        #print aux
        elitizacao.append(aux)
        #print aux
    #selecionarElite(elitizacao)
    return elitizacao

#Calcular Fitness do Cromossomo
def calcularFitness(cromo):
    #auxiliar = list(tiles)
    auxiliar = copy.copy(tiles)
    fitness = 0
    #print auxiliar
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
        #print 'matriz'
        #print auxiliar
        for telha in auxiliar:
            spot = telha + neighbor

            if spot in auxiliar and auxiliar[spot] is None:
                number = auxiliar[telha]
                auxiliar[telha] = None
                auxiliar[spot] = number
                movimento = True
                break
            if not movimento:
                #print 'movimento invalido'
                fitness+=1

    fitness += foraDoLugar(auxiliar) * 36 + inversoes(auxiliar) * 2
    return fitness
    
#Funcao de Fitness
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

#def distanciaManhatan(auxiliar):
    
def inversoes(auxiliar):

    fitness = 0;

    posicao_atual = vector(-100, 0)
    posicao_anterior = vector(-200, 0)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(0, 0)
    posicao_anterior = vector(-100, 0)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-200, -100)
    posicao_anterior = vector(0, 0)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-100, -100)
    posicao_anterior = vector(-200, -100)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(0, -100)
    posicao_anterior = vector(-100, -100)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-200, -200)
    posicao_anterior = vector(0, -100)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-100, -200)
    posicao_anterior = vector(-200, -200)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(0, -200)
    posicao_anterior = vector(-100, -200)
    if auxiliar[posicao_atual] > auxiliar[posicao_anterior]:
        fitness+=1

    return fitness

def resolverPuzzle(movimentos):
    for item in range(30):
        time.sleep(.500)
        change(movimentos[item])
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
onkey(lambda: algoritmoGenetico(12, 2000), 'g')


#onscreenclick(tap)
done()
#-------------------------------------------------------------------------------------------------------------#