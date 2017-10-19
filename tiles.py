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
    populacao = gerarPopulacao(qtd_populacao)                       # 20 pessoas
    
    print 'populacao inicial'       
    for item in range(len(populacao)):
        print populacao[item]
    
    print 'elitizacao inicial'       
    elitizacao = calcularFitnessGlobal(populacao)
    for item in range(len(elitizacao)):
        print elitizacao[item]
    menorFitnss = melhorFitnss(elitizacao)
    posicao = 0
    '''
    for geracao in range(geracoes):
        elitizacao = calcularFitnessGlobal(populacao)
        
        pais = selecionarPais(elitizacao, populacao)                                # 12 pais
        filhos = crossover(pais)                                                    # 4 filhos
        mutantes = mutacao(filhos)                                                  # 2 mutantes
        aleatorios = gerarPopulacao(2)                                              # 2 inidividuos aleatorios
        populacao = gerarNovaPopulacao(pais, filhos, mutantes, aleatorios)          # 20 pessoas
        print 1000 - geracao
    '''
    geracao = 1
    while(menorFitnss > 3 and geracao < 100000):
        elitizacao = calcularFitnessGlobal(populacao)
        
        pais = selecionarPais(elitizacao, populacao)                                # 6 pais
        filhos = crossover(pais)                                                    # 6 filhos
        mutantes = mutacao(filhos)                                                  # 4 mutantes
        aleatorios = gerarPopulacao(2)                                              # 2 inidividuos aleatorios
        pais_aleatorios = crossover2(pais, aleatorios)                              # 2 filhos
        populacao = gerarNovaPopulacao(pais, filhos, mutantes, aleatorios, pais_aleatorios)          # 20 pessoas
        menorFitnss, posicao = melhorFitnss(elitizacao)
        print '\nGeracao'
        print geracao
        print menorFitnss
        geracao+=1

    print '--------------------------------------------------------------'
    
    print 'populacao final'       
    for item in range(len(populacao)):
        print populacao[item]
    
    print 'elitizacao final'       
    elitizacao = calcularFitnessGlobal(populacao)
    for item in range(len(elitizacao)):
        print elitizacao[item]
    print '--------------------------------------------------------------'
    resolverPuzzle(populacao[posicao])
    
def crossover2(pais, aleatorios):
    filhos = []
    
    #Filho 1
    filho1 = []
    for item in range(0, 5):
        filho1.append(pais[0][item])
    for item in range(5, 10):
        filho1.append(aleatorios[0][item])
    for item in range(10, 15):
        filho1.append(pais[0][item])
    for item in range(15, 20):
        filho1.append(aleatorios[0][item])
    for item in range(20, 25):
        filho1.append(pais[0][item])
    for item in range(25, 30):
        filho1.append(aleatorios[0][item])

    #Filho 2
    filho2 = []
    for item in range(0, 5):
        filho2.append(pais[1][item])
    for item in range(5, 10):
        filho2.append(aleatorios[1][item])
    for item in range(10, 15):
        filho2.append(pais[1][item])
    for item in range(15, 20):
        filho2.append(aleatorios[1][item])
    for item in range(20, 25):
        filho2.append(pais[1][item])
    for item in range(25, 30):
        filho2.append(aleatorios[1][item])

    filhos.append(filho1)
    filhos.append(filho2)

    return filhos

def melhorFitnss(elitizacao):
    menorFitnss = elitizacao[0]
    posicao = 0
    for item in range(len(elitizacao)):
        if elitizacao[item] < menorFitnss:
            menorFitnss = elitizacao[item]
            posicao = item
    return menorFitnss, posicao
    
def movimentosPossiveis(cromossomo):
    auxiliar = copy.copy(tiles)
    movimentos = []
    
    for item in tiles:
        if tiles[item] == None:
            posicao = item
            break
    if len(cromossomo) == 0:
        if neighbors[0] + posicao in tiles:
            movimentos.append(2)
        if neighbors[1] + posicao in tiles:
            movimentos.append(1)
        if neighbors[2] + posicao in tiles:
            movimentos.append(4)
        if neighbors[3] + posicao in tiles:
            movimentos.append(3)    
        return movimentos
    else:
        for item in range(len(cromossomo)):    
            x = cromossomo[item]
            if x == 1:
                neighbor = neighbors[0]
            elif x == 2:
                neighbor = neighbors[1]
            elif x == 3:
                neighbor = neighbors[2]
            elif x == 4:
                neighbor = neighbors[3]
            for telha in auxiliar:
                spot = telha + neighbor
                if spot in auxiliar and auxiliar[spot] is None:
                    number = auxiliar[telha]
                    auxiliar[telha] = None
                    auxiliar[spot] = number
                    break

        for item in auxiliar:
            if auxiliar[item] == None:
                posicao = item
                break
        #print posicao

        if neighbors[0] + posicao in tiles:
            movimentos.append(2)
        if neighbors[1] + posicao in tiles:
            movimentos.append(1)
        if neighbors[2] + posicao in tiles:
            movimentos.append(4)
        if neighbors[3] + posicao in tiles:
            movimentos.append(3)    
        return movimentos            

def gerarNovaPopulacao(pais, filhos, mutantes, aleatorios, pais_aleatorios):
    populacao = []
    for item in pais:
        populacao.append(item)
    for item in filhos:
        populacao.append(item)
    for item in mutantes:
        populacao.append(item)
    for item in aleatorios:
        populacao.append(item)
    for item in pais_aleatorios:
        populacao.append(item)
    return populacao

#Gerar Mutacao
def mutacao(filhos):
    mutantes = []
    
    # Mutacao 1 ->  filho1 : Troca dos valores 10 e 20, 8 e 25, 3 e 9, 0 e 29, 1 e 28, 2 e 27
    mutante1 = filhos[0]

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

    aux1 = mutante1[0]    
    aux2 = mutante1[29]
    mutante1[0] = aux2
    mutante1[29] = aux1

    aux1 = mutante1[1]
    aux2 = mutante1[28]
    mutante1[1] = aux2
    mutante1[28] = aux1

    aux1 = mutante1[2]
    aux2 = mutante1[27]
    mutante1[2] = aux2
    mutante1[27] = aux1

    # Mutacao 2 -> filho2: Troca dos valores 5 e 15, 3 e 26, 7 e 19, 0 e 29, 1 e 28, 2 e 27

    mutante2 = filhos[1]

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

    aux1 = mutante2[3]    
    aux2 = mutante2[26]
    mutante2[3] = aux2
    mutante2[26] = aux1

    aux1 = mutante2[1]
    aux2 = mutante2[28]
    mutante2[1] = aux2
    mutante2[28] = aux1

    aux1 = mutante2[2]
    aux2 = mutante2[27]
    mutante2[2] = aux2
    mutante2[27] = aux1

    # Mutacao 3 -> filho3: Troca dos valores 5 e 15, 0 e 29, 7 e 19, 0 e 29, 1 e 28, 2 e 27

    mutante3 = filhos[2]

    aux1 = mutante3[5]
    aux2 = mutante3[15]
    mutante3[5] = aux2
    mutante3[15] = aux1

    aux1 = mutante3[0]
    aux2 = mutante3[29]
    mutante3[0] = aux2
    mutante3[29] = aux1

    aux1 = mutante3[10]
    aux2 = mutante3[20]
    mutante3[7] = aux2
    mutante3[19] = aux1

    aux1 = mutante3[3]    
    aux2 = mutante3[26]
    mutante3[3] = aux2
    mutante3[26] = aux1

    aux1 = mutante3[1]
    aux2 = mutante3[28]
    mutante3[1] = aux2
    mutante3[28] = aux1

    aux1 = mutante3[2]
    aux2 = mutante3[27]
    mutante3[2] = aux2
    mutante3[27] = aux1

    # Mutacao 4 ->  filho4 : Troca dos valores 10 e 20, 8 e 25, 3 e 9, 0 e 29, 1 e 28, 2 e 27
    mutante4 = filhos[3]

    aux1 = mutante4[10]
    aux2 = mutante4[20]
    mutante4[10] = aux2
    mutante4[20] = aux1

    aux1 = mutante4[8]
    aux2 = mutante4[25]
    mutante4[8] = aux2
    mutante4[25] = aux1

    aux1 = mutante4[3]
    aux2 = mutante4[9]
    mutante4[3] = aux2
    mutante4[9] = aux1

    aux1 = mutante4[3]    
    aux2 = mutante4[26]
    mutante4[3] = aux2
    mutante4[26] = aux1

    aux1 = mutante4[1]
    aux2 = mutante4[28]
    mutante4[1] = aux2
    mutante4[28] = aux1

    aux1 = mutante4[2]
    aux2 = mutante4[27]
    mutante4[2] = aux2
    mutante4[27] = aux1
    
    mutantes.append(mutante1)
    mutantes.append(mutante2)
    mutantes.append(mutante3)
    mutantes.append(mutante4)

    return mutantes

#Cruzamento
def crossover(pais):
    filhos = []

    #Filho 1
    filho1 = []
    for item in range(0, 5):
        filho1.append(pais[0][item])
    for item in range(5, 10):
        filho1.append(pais[1][item])
    for item in range(10, 15):
        filho1.append(pais[0][item])
    for item in range(15, 20):
        filho1.append(pais[1][item])
    for item in range(20, 25):
        filho1.append(pais[0][item])
    for item in range(25, 30):
        filho1.append(pais[1][item])

    #Filho 2
    filho2 = []
    for item in range(0, 5):
        filho2.append(pais[1][item])
    for item in range(5, 10):
        filho2.append(pais[0][item])
    for item in range(10, 15):
        filho2.append(pais[1][item])
    for item in range(15, 20):
        filho2.append(pais[0][item])
    for item in range(20, 25):
        filho2.append(pais[1][item])
    for item in range(25, 30):
        filho2.append(pais[0][item])

    
    #Filho 3
    filho3 = []
    for item in range(0, 5):
        filho3.append(pais[2][item])
    for item in range(5, 10):
        filho3.append(pais[3][item])
    for item in range(10, 15):
        filho3.append(pais[2][item])
    for item in range(15, 20):
        filho3.append(pais[3][item])
    for item in range(20, 25):
        filho3.append(pais[2][item])
    for item in range(25, 30):
        filho3.append(pais[3][item])

    #Filho 4
    filho4 = []
    for item in range(0, 5):
        filho4.append(pais[3][item])
    for item in range(5, 10):
        filho4.append(pais[2][item])
    for item in range(10, 15):
        filho4.append(pais[3][item])
    for item in range(15, 20):
        filho4.append(pais[2][item])
    for item in range(20, 25):
        filho4.append(pais[3][item])
    for item in range(25, 30):
        filho4.append(pais[2][item])


    #Filho 5
    filho5 = []
    for item in range(0, 5):
        filho5.append(pais[4][item])
    for item in range(5, 10):
        filho5.append(pais[5][item])
    for item in range(10, 15):
        filho5.append(pais[4][item])
    for item in range(15, 20):
        filho5.append(pais[5][item])
    for item in range(20, 25):
        filho5.append(pais[4][item])
    for item in range(25, 30):
        filho5.append(pais[5][item])

    #Filho 6
    filho6 = []
    for item in range(0, 5):
        filho6.append(pais[5][item])
    for item in range(5, 10):
        filho6.append(pais[4][item])
    for item in range(10, 15):
        filho6.append(pais[5][item])
    for item in range(15, 20):
        filho6.append(pais[4][item])
    for item in range(20, 25):
        filho6.append(pais[5][item])
    for item in range(25, 30):
        filho6.append(pais[4][item])
    
    '''
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

    #Filho 5
    filho5 = []
    for item in range(15):
        filho5.append(pais[4][item])
    for item in range(15, 30):
        filho5.append(pais[5][item])

    #Filho 6
    filho6 = []
    for item in range(15):
        filho6.append(pais[5][item])
    for item in range(15, 30):
        filho6.append(pais[4][item])
    '''
    filhos.append(filho1)
    filhos.append(filho2)
    filhos.append(filho3)
    filhos.append(filho4)
    filhos.append(filho5)
    filhos.append(filho6)

    return filhos

#Gerar Populacao
def gerarPopulacao(num):
    populacao = []
    for pessoa in range(num):
        cromossomo = []
        for cromo in range(30):
            #Definindo Movimentos Aleatorios
            m = movimentosPossiveis(cromossomo)
            movimento = choice(m)
            cromossomo.append(movimento)
        populacao.append(cromossomo)
    return populacao

#Selecionar os Pais
def selecionarPais(elitizacao, populacao):
    elitizacaoAux = copy.copy(elitizacao)
    for elite in range(14):
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
            #if not movimento:
                #print 'movimento invalido'
            #    fitness+=1

    fitness += foraDoLugar(auxiliar) * 36 + inversoes(auxiliar) * 2 + distanciaManhatan(auxiliar) * 10
    return foraDoLugar(auxiliar)
    
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

def distanciaManhatan(auxiliar):
    fitness = 0;
    
    posicao = vector(-200, 0)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 1)
    
    posicao = vector(-100, 0)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 2)
    
    posicao = vector(0, 0)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 3)
    
    posicao = vector(-200, -100)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 4)
    
    posicao = vector(-100, -100)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 5)
    
    posicao = vector(0, -100)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 6)
    
    posicao = vector(-200, -200)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 7)
    
    posicao = vector(-100, -200)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 8)
    
    posicao = vector(0, -200)
    if auxiliar[posicao] == None: aux = 9
    else: aux = auxiliar[posicao]
    fitness += abs(aux - 9)
    
    return fitness
    
def inversoes(auxiliar):

    fitness = 0;

    posicao_atual = vector(-100, 0)
    posicao_anterior = vector(-200, 0)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(0, 0)
    posicao_anterior = vector(-100, 0)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-200, -100)
    posicao_anterior = vector(0, 0)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-100, -100)
    posicao_anterior = vector(-200, -100)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(0, -100)
    posicao_anterior = vector(-100, -100)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-200, -200)
    posicao_anterior = vector(0, -100)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
        fitness+=1

    posicao_atual = vector(-100, -200)
    posicao_anterior = vector(-200, -200)
    if auxiliar[posicao_atual] < auxiliar[posicao_anterior]:
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
onkey(lambda: algoritmoGenetico(20, 1000), 'g')


#onscreenclick(tap)
done()
#-------------------------------------------------------------------------------------------------------------#